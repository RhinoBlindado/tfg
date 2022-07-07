import argparse 
import pandas as pd
import os
import datetime

parser = argparse.ArgumentParser(description='Generate train and validation loss and accuracy plot')
parser.add_argument('--tests',  nargs='+', default= [-1], help='Tests to run')
args = parser.parse_args() 

GSParams = pd.read_csv("./scripts/GSParams.csv", sep=',', header=None)

for i in args.tests:

    print(GSParams[0][int(i)])
    currentDT = datetime.datetime.now()
    
    os.system("echo \"{}... @ {}\" >> GS_log.txt".format(GSParams[0][int(i)], currentDT.strftime("%Y_%m_%d__%H_%M_%S")))
    out = os.system("{}".format(GSParams[1][int(i)]))
    if out == 0:
        os.system("{}".format(GSParams[2][int(i)]))
    os.system("echo \"Finished @ {} with exit {}\" >> GS_log.txt".format(currentDT.strftime("%Y_%m_%d__%H_%M_%S"), out))