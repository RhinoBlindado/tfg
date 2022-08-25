import argparse 
import pandas as pd
import os
import datetime

parser = argparse.ArgumentParser(description='Main code to run Grid Search with MeshCNN')
parser.add_argument('--tests',  nargs='+', default= [-1], help='Tests to run')
args = parser.parse_args() 

GSParams = pd.read_csv("./scripts/slurm/Nodule-98-30K-GS-Params.csv", sep=',', header=None)

for i in args.tests:

    print(GSParams[0][int(i)])
    currentDT = datetime.datetime.now()
    
    os.system("echo \"{}... @ {}\" >> Nodule-98-30K-GS-Log.txt".format(GSParams[0][int(i)], currentDT.strftime("%Y_%m_%d__%H_%M_%S")))
    out = os.system("{}".format(GSParams[1][int(i)]))
    if out == 0:
        os.system("{}".format(GSParams[2][int(i)]))
    os.system("echo \"Finished @ {} with exit {}\" >> Nodule-98-30K-GS-Log.txt".format(currentDT.strftime("%Y_%m_%d__%H_%M_%S"), out))