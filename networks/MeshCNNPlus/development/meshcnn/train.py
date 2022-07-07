from tabnanny import verbose
import time
from options.train_options import TrainOptions
from data import DataLoader
from models import create_model
from util.writer import Writer
from test import run_test
import copy
import numpy as np


def getTrainAcc(model, trainDataset):
    
    totalTrainCorrect = 0

    for _, dataitem in enumerate(trainDataset):
        model.set_input(dataitem)
        ncorrect, __, _ = model.test()

        totalTrainCorrect += int(ncorrect)

    return totalTrainCorrect / len(trainDataset)


def validationMetrics(model, opt, hist):

    validationSet = DataLoader(opt)

    # print("Running validation on {} meshes".format(len(validationSet)))
    actValLoss = 0.0    
    totalValCorrect = 0

    for _, vdata in enumerate(validationSet):
        model.set_input(vdata)
        valCorrect, _, valloss = model.test()
        
        actValLoss += len(vdata['mesh']) * valloss.item()
        totalValCorrect  += int(valCorrect)

    avgValLoss = actValLoss / len(validationSet)
    totalValAcc = totalValCorrect / len(validationSet)

    # hist.append(avgValLoss)

    return totalValAcc, avgValLoss


if __name__ == '__main__':
    np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
    
    opt = TrainOptions().parse()

    # If validation is checked, generate options for the validation dataset.
    if(opt.validation):
        # Copy most of them.
        optVal = copy.deepcopy(opt)
        # Change what's needed:
        # - Name of the phase
        # - Turn off data augmentation
        optVal.phase = 'val'
        optVal.num_aug = 1
        optVal.slide_verts = 0
        optVal.flip_edges = 0 

    dataset = DataLoader(opt)
    dataset_size = len(dataset)

    print('#training meshes = %d' % dataset_size)

    model = create_model(opt)
    writer = Writer(opt)

    #print(model.net)

    total_steps = 0

    maxPatience = 5
    actPatience = 0
    prevLoss = float('inf')

    testLossHist  = []
    validLossHist = []

    for epoch in range(opt.epoch_count, opt.niter + opt.niter_decay + 1):
                
        epoch_start_time = time.time()
        iter_data_time = time.time()
        epoch_iter = 0
        trainLoss = 0

        totalTrainCorrect = 0
        totalTrainExamples = 0

        # In each epoch...
        for i, data in enumerate(dataset):
            iter_start_time = time.time()
            if total_steps % opt.print_freq == 0:
                t_data = iter_start_time - iter_data_time
            total_steps += opt.batch_size
            epoch_iter += opt.batch_size
            # - Set the input as the current batch.
            model.set_input(data)
            # - Optimize the network, foward and backpropagation.
            model.optimize_parameters()

            iter_data_time = time.time()

            # Saving the loss of each batch without the average
            trainLoss += len(data['mesh']) * model.loss.item()
            
            if total_steps % opt.print_freq == 0:
                loss = model.loss
                t = (time.time() - iter_start_time) / opt.batch_size
                writer.print_current_losses(epoch, epoch_iter, loss, t, t_data)
                writer.plot_loss(loss, epoch, epoch_iter, dataset_size)

            if i % opt.save_latest_freq == 0:
                print('saving the latest model (epoch %d, total_steps %d)' %
                      (epoch, total_steps))
                model.save_network('latest')


        # Calculating and displaying different metrics:

        # - Getting the training accuracy
        trainAcc = getTrainAcc(model, dataset)

        # - If validation is on, calculate accuracy and loss.
        if(opt.validation): 
            valAcc, valLoss = validationMetrics(model, optVal, validLossHist)

        # - Save the network after n epochs...
        if epoch % opt.save_epoch_freq == 0:
            print('saving the model at the end of epoch %d, iters %d' %
                  (epoch, total_steps))
            model.save_network('latest')
            model.save_network(epoch)

        # - Print to screen different metrics, verbose or not.
        model.update_learning_rate()
        if(opt.verbose_train):
            writer.printTestValidationLoss(epoch, trainAcc, trainLoss / dataset_size, valAcc, valLoss, time.time() - epoch_start_time)
            print("Epoch {}/{} | time: {:.4f} - train_acc: {:.2f}% - train_loss: {:.4f} - val_acc: {:.2f}% - val_loss: {:.4f}".format(epoch, opt.niter + opt.niter_decay, 
            time.time() - epoch_start_time, trainAcc * 100, trainLoss / dataset_size, valAcc * 100, valLoss))
        else:
            print('Epoch %d / %d \t, Time Taken: %d sec, Loss: %.3f' %
                 (epoch, opt.niter + opt.niter_decay, time.time() - epoch_start_time, trainLoss / dataset_size))

        # - If using tensorboard, display model weights.
        if opt.verbose_plot:
            writer.plot_model_wts(model, epoch)

        # - After n epochs, run test.
        if epoch % opt.run_test_freq == 0:
            acc = run_test(epoch)
            writer.plot_acc(acc, epoch)

        # - Early Stopping
        if valLoss >= prevLoss:
            actPatience += 1
            print("Early Stopping: val_loss did not lower, patience {}/{}".format(actPatience, maxPatience))
        else:
            actPatience = max(0, actPatience - 1)
        
        if actPatience > maxPatience:
            print("Validation loss is stagnating, stopping.")
            break

        prevLoss = valLoss

    writer.close()
