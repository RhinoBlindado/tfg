from options.test_options import TestOptions
from data import DataLoader
from models import create_model
from util.writer import Writer


def getTestLoss(model):
    pass

def run_test(epoch=-1):
    print('Running Test')
    opt = TestOptions().parse()
    opt.serial_batches = True  # no shuffle
    dataset = DataLoader(opt)
    model = create_model(opt)
    writer = Writer(opt)
    # test

    if(epoch==-1):
        soleTest=True
    else:
        soleTest=False

    writer.reset_counter()
    totalLoss = 0
    for i, data in enumerate(dataset):
        model.set_input(data)
        ncorrect, nexamples, loss = model.test(soleTest)
        writer.update_counter(ncorrect, nexamples)
        totalLoss += loss
    totalLoss /= len(dataset)
    writer.print_acc(epoch, writer.acc, totalLoss)
    return writer.acc


if __name__ == '__main__':
    run_test()
