"""
 [CASTELLANO]

    Generar un fichero CSV con la característica necesaria.
    Asignatura: Trabajo de Fin de Grado
    Autor: Valentino Lugli (Github: @RhinoBlindado)
    2022

 [ENGLISH]

    Generate a CSV file with the desired characteristic.
    Course: Bachelor's Thesis
    Author: Valentino Lugli (Github: @RhinoBlindado)
    2022
"""

import csv
import argparse 

def balanceClass(dictChar, maxSize):

    for i in dictChar:
        dictChar[i] = dictChar[i][:maxSize]


parser = argparse.ArgumentParser(description='Generate a CSV file for a desired characteristic')

parser.add_argument('--tagPath', required=True, help='Path to the main CSV file.')
parser.add_argument('--characteristic', required=True, type=str, default=None, help='Characteristic to use.')
parser.add_argument('--lat', type=int, required=True, help='Laterality of the bone: 0 is left, 1 is right, 2 is both.')
parser.add_argument('--balanced', type=str, default=None, help='If present, a balanced CSV is generated taking the current attribute as the balance point.')

args = parser.parse_args() 

query = args.characteristic
if 0 <= args.lat and args.lat <= 2:
    lat = str(args.lat)
else:
    print("Error: Wrong laterality")
    exit(-1)

tags = open(args.tagPath, newline='')

balance = False
if(args.balanced is not None):
    balance = True
    balanceAttr = str(args.balanced)

tagsDict = csv.DictReader(tags)

latDict = {     
            '0' : '-Izq',
            '1' : '-Der'
        }

chars = {   
            '0' : [], 
            '1' : []
        }

errVals = 0

for item in tagsDict:
    individual  = item['individuo']
    laterality = item['lateralidad']
    value = item[query]

    if(value != '' and item['Excluidos'] == '' and lat == laterality):
        try:
            chars[value].append(individual+latDict[lat])
        except KeyError:
            errVals += 1
            continue

balanceStr = 'full'
if balance:
    balanceStr = 'balanced'
    balanceClass(chars, len(chars[balanceAttr]))

print("Stats:")
print("Characteristic: {}".format(query))

totSize = 0

for i in chars:
    totSize += len(chars[i])
    print("Char {}: {}".format(i, len(chars[i])))

print("Error valued individuals: {}".format(errVals))

outFile = open('{}_{}.csv'.format(query, balanceStr), 'w')

for i in chars:
    for j in chars[i]:
        outFile.write("{},{}\n".format(j, i))

outFile.close()
