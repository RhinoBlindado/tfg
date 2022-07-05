from options.test_options import TestOptions
from data import DataLoader
from models import create_model
from util.writer import Writer


def run_test(epoch=-1):
    print('Running Test')
    opt = TestOptions().parse()
    opt.serial_batches = True  # no shuffle
    dataset = DataLoader(opt)
    model = create_model(opt)
    writer = Writer(opt)
    # test

    writer.reset_counter()
    totalLoss = 0
    for i, data in enumerate(dataset):
        model.set_input(data)
        ncorrect, nexamples, loss = model.test(verbose=opt.verbose, confusion=opt.confusion_matrix)
        writer.update_counter(ncorrect, nexamples)

        # Saving the loss of each batch without the average
        totalLoss += len(data['mesh']) * loss.item()

    # Calculating the average loss of the whole dataset
    totalLoss /= len(dataset)
    model.printMetrics(opt.verbose, opt.confusion_matrix)
    writer.print_acc(epoch, writer.acc, totalLoss)
    return writer.acc


if __name__ == '__main__':
    run_test()
