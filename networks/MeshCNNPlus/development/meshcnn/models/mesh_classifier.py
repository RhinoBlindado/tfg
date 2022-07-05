from cProfile import label
import torch
from . import networks
from os.path import join
from util.util import seg_accuracy, print_network
from tabulate import tabulate as tb
import sklearn.metrics as skm
import numpy as np

class ClassifierModel:
    """ Class for training Model weights

    :args opt: structure containing configuration params
    e.g.,
    --dataset_mode -> classification / segmentation)
    --arch -> network type
    """
    def __init__(self, opt):
        self.opt = opt
        self.gpu_ids = opt.gpu_ids
        self.is_train = opt.is_train
        self.device = torch.device('cuda:{}'.format(self.gpu_ids[0])) if self.gpu_ids else torch.device('cpu')
        self.save_dir = join(opt.checkpoints_dir, opt.name)
        self.optimizer = None
        self.edge_features = None
        self.labels = None
        self.mesh = None
        self.soft_label = None
        self.loss = None

        #
        self.nclasses = opt.nclasses

        # For classification statistics...
        self.x_test = []
        self.pred_y_test = []
        self.y_test = []

        # load/define networks
        self.net = networks.define_classifier(opt.input_nc, opt.ncf, opt.ninput_edges, opt.nclasses, opt,
                                              self.gpu_ids, opt.arch, opt.init_type, opt.init_gain)
        self.net.train(self.is_train)
        self.criterion = networks.define_loss(opt).to(self.device)

        if self.is_train:
            if (opt.optimizer == 'adam'):
                self.optimizer = torch.optim.Adam(self.net.parameters(), lr=opt.lr, betas=(opt.beta1, 0.999), amsgrad=opt.amsgrad)
            if (opt.optimizer == 'rmsprop'):
                self.optimizer = torch.optim.RMSprop(self.net.parameters(), lr=opt.lr)
            if (opt.optimizer == 'sgd'):
                self.optimizer = torch.optim.SGD(self.net.parameters(), lr=opt.lr)
            if (opt.optimizer == 'adagrad'):
                self.optimizer = torch.optim.Adagrad(self.net.parameters(), lr=opt.lr)

            self.scheduler = networks.get_scheduler(self.optimizer, opt)
            print_network(self.net)

        if not self.is_train or opt.continue_train:
            self.load_network(opt.which_epoch)

    def set_input(self, data):
        input_edge_features = torch.from_numpy(data['edge_features']).float()
        labels = torch.from_numpy(data['label']).long()
        # set inputs
        self.edge_features = input_edge_features.to(self.device).requires_grad_(self.is_train)
        self.labels = labels.to(self.device)
        self.mesh = data['mesh']
        if self.opt.dataset_mode == 'segmentation' and not self.is_train:
            self.soft_label = torch.from_numpy(data['soft_label'])
        self.classIdx = dict(map(reversed, data['classIdx'][0].items()))
        self.classTags = list(data['classIdx'][0].keys())


    def forward(self):
        out = self.net(self.edge_features, self.mesh)
        return out

    def backward(self, out):
        self.loss = self.criterion(out, self.labels)
        self.loss.backward()

    def optimize_parameters(self):
        self.optimizer.zero_grad()
        out = self.forward()
        self.backward(out)
        self.optimizer.step()


##################

    def load_network(self, which_epoch):
        """load model from disk"""
        save_filename = '%s_net.pth' % which_epoch
        load_path = join(self.save_dir, save_filename)
        net = self.net
        if isinstance(net, torch.nn.DataParallel):
            net = net.module
        print('loading the model from %s' % load_path)
        # PyTorch newer than 0.4 (e.g., built from
        # GitHub source), you can remove str() on self.device
        state_dict = torch.load(load_path, map_location=str(self.device))
        if hasattr(state_dict, '_metadata'):
            del state_dict._metadata
        net.load_state_dict(state_dict)


    def save_network(self, which_epoch):
        """save model to disk"""
        save_filename = '%s_net.pth' % (which_epoch)
        save_path = join(self.save_dir, save_filename)
        if len(self.gpu_ids) > 0 and torch.cuda.is_available():
            torch.save(self.net.module.cpu().state_dict(), save_path)
            self.net.cuda(self.gpu_ids[0])
        else:
            torch.save(self.net.cpu().state_dict(), save_path)

    def update_learning_rate(self):
        """update learning rate (called once every epoch)"""
        self.scheduler.step()
        lr = self.optimizer.param_groups[0]['lr']
        print('learning rate = %.7f' % lr)

    def test(self, verbose=False, confusion=False):
        """tests model
        returns: number correct and total number
        """
        actLoss = 0
        with torch.no_grad():
            out = self.forward()
            actLoss = self.criterion(out, self.labels)
            # compute number of correct
            pred_class = out.data.max(1)[1]
            label_class = self.labels

            if(verbose or confusion):
                for i, mesh in enumerate(self.mesh):
                    self.x_test.append(mesh.filename)
                    self.y_test.append(int(label_class[i]))
                    self.pred_y_test.append(int(pred_class[i]))

            self.export_segmentation(pred_class.cpu())
            correct = self.get_accuracy(pred_class, label_class)
        return correct, len(label_class), actLoss

    def getTestLoss(self):
        out = self.forward()

    def printMetrics(self, verbose, confusion):

        if(verbose):
            meshes = []
            for i, mesh in enumerate(self.x_test):
                meshes.append([mesh, self.classIdx[self.pred_y_test[i]], self.classIdx[self.y_test[i]]])
            print(tb(meshes, headers=["Mesh", "Prediction", "Actual"]))

        if(confusion):   
            #print("Matriz de Confusión: \n")
            #print(skm.confusion_matrix(self.y_test, self.pred_y_test), "\n")

            print("Reporte de clasificación:")
            print(skm.classification_report(self.y_test, self.pred_y_test, target_names=self.classTags))

    def get_accuracy(self, pred, labels):
        """computes accuracy for classification / segmentation """
        if self.opt.dataset_mode == 'classification':
            correct = pred.eq(labels).sum()
        elif self.opt.dataset_mode == 'segmentation':
            correct = seg_accuracy(pred, self.soft_label, self.mesh)
        return correct

    def export_segmentation(self, pred_seg):
        if self.opt.dataset_mode == 'segmentation':
            for meshi, mesh in enumerate(self.mesh):
                mesh.export_segments(pred_seg[meshi, :])
