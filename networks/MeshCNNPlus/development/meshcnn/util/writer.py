import os
import time

try:
    from tensorboardX import SummaryWriter
except ImportError as error:
    print('tensorboard X not installed, visualizing wont be available')
    SummaryWriter = None

class Writer:
    def __init__(self, opt):
        self.name = opt.name
        self.opt = opt
        self.save_dir = os.path.join(opt.checkpoints_dir, opt.name)
        self.log_name = os.path.join(self.save_dir, 'loss_log.txt')
        self.testacc_log = os.path.join(self.save_dir, 'testacc_log.txt')
        self.start_logs()
        self.nexamples = 0
        self.ncorrect = 0
        #
        if opt.is_train and not opt.no_vis and SummaryWriter is not None:
            self.display = SummaryWriter(comment=opt.name)
        else:
            self.display = None

    def start_logs(self):
        """ creates test / train log files """
        if self.opt.is_train:
            with open(self.log_name, "a") as log_file:
                now = time.strftime("%c")
                log_file.write('================ Training Loss (%s) ================\n' % now)
                log_file.write('epoch, train_acc, train_loss, val_acc, val_loss\n')
        else:
            with open(self.testacc_log, "a") as log_file:
                now = time.strftime("%c")
                log_file.write('================ Testing Acc (%s) ================\n' % now)

    def print_current_losses(self, epoch, i, losses, t, t_data):
        """ prints train loss to terminal / file """
        message = '(epoch: %d, iters: %d, time: %.3f, data: %.3f) loss: %.3f ' \
                  % (epoch, i, t, t_data, losses.item())
        print(message)
        with open(self.log_name, "a") as log_file:
            log_file.write('%s\n' % message)

    def printTestValidationLoss(self, epoch, trainAcc, trainLoss, valAcc , valLoss, time):
        message = "{}, {}, {}, {}, {}".format(epoch, trainAcc, trainLoss, valAcc, valLoss, time)
        with open(self.log_name, "a") as log_file:
            log_file.write('%s\n' % message)

    def plot_loss(self, loss, epoch, i, n):
        iters = i + (epoch - 1) * n
        if self.display:
            self.display.add_scalar('data/train_loss', loss, iters)

    def plot_model_wts(self, model, epoch):
        if self.opt.is_train and self.display:
            for name, param in model.net.named_parameters():
                self.display.add_histogram(name, param.clone().cpu().data.numpy(), epoch)

    def print_acc(self, epoch, acc, loss, class_acc = None):
        """ prints test accuracy to terminal / file """
        message = 'epoch: {}, TEST ACC: [{:.2f}%], LOSS: {:.3f}\n' \
            .format(epoch, acc * 100, loss)
        print(message)
        with open(self.testacc_log, "a") as log_file:
            log_file.write('%s\n' % message)
            """
            if(class_acc is not None):
                for classIdx in range(len(class_acc)):
                    message = 'TEST ACC CLASS {} ({:.5} %): [{:.5} %]\n' \
                        .format(classIdx, 100 * self.nexamplesPerClass[classIdx] / self.nexamples,
                                class_acc[classIdx] * 100)
                    print(message)
                    log_file.write('%s\n' % message)
            """

    def plot_acc(self, acc, epoch):
        if self.display:
            self.display.add_scalar('data/test_acc', acc, epoch)

    def reset_counter(self):
        """
        counts # of correct examples
        """
        self.ncorrect = 0
        self.nexamples = 0
        self.ncorrectPerClass = None
        self.nexamplesPerClass = None

    def update_counter(self, ncorrect, nexamples,  ncorrectPerClass=None, nexamplesPerClass=None):
        self.ncorrect += ncorrect
        self.nexamples += nexamples

        if (self.ncorrectPerClass == None):
            self.ncorrectPerClass = ncorrectPerClass
            self.nexamplesPerClass = nexamplesPerClass
        else:
            self.ncorrectPerClass += ncorrectPerClass
            self.nexamplesPerClass += nexamplesPerClass


            
    @property
    def acc(self):
        return float(self.ncorrect) / self.nexamples

    @property
    def classAcc(self):
        return self.ncorrectPerClass / self.nexamplesPerClass

    def close(self):
        if self.display is not None:
            self.display.close()