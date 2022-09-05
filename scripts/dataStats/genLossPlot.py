"""
 [CASTELLANO]

    Pintar las curvas de aprendizaje de Accuracy y Loss de un modelo.
    Asignatura: Trabajo de Fin de Grado
    Autor: Valentino Lugli (Github: @RhinoBlindado)
    2022

 [ENGLISH]

    Draw the learning curves for accuracy and loss for a model.
    Course: Bachelor's Thesis
    Author: Valentino Lugli (Github: @RhinoBlindado)
    2022
"""

import matplotlib.pyplot as plt
import pandas as pd
import argparse 


def plotLearningCurve(sizes, train, test, ylabel, outPath, filename, title=False):
    """
    Helper function to print the learning curves.

    """
    plt.figure()
    epochs = range(1, sizes+1)
    plt.plot(epochs, train, '-', color='g', label="Entrenamiento")
    plt.plot(epochs, test, '-', color='r', label="Validación")
    
    plt.legend()

    plt.ylabel(ylabel)
    plt.xlabel("Época")
    
    if title:
        plt.title('{}: {}'.format(filename, ylabel))
    plt.savefig('{}{}_{}'.format(outPath, filename, ylabel), dpi=300, bbox_inches='tight')


parser = argparse.ArgumentParser(description='Generate train and validation loss and accuracy plot')

parser.add_argument('--file', required=True, help='Path to loss_log.txt file.')
parser.add_argument('--title', action='store_true', help='If true, filename is also title')
parser.add_argument('--filename', required=True, type=str, default=None, help='Base filename')
parser.add_argument('--out', type=str, default=None, help='Optional, output path')

args = parser.parse_args() 

trainLog = pd.read_csv(args.file, sep=',', header=1)

logLen = len(trainLog)

outputPath = './' if args.out is None else args.out

plotLearningCurve(logLen, trainLog[' train_acc'] * 100, trainLog[' val_acc'] * 100, 
                  'Accuracy', outputPath, args.filename, title=args.title)

plotLearningCurve(logLen, trainLog[' train_loss'], trainLog[' val_loss'], 
                  'Loss', outputPath, args.filename, title=args.title)