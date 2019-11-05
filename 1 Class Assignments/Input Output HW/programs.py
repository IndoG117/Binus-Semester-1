# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:32:48 2019

@author: gadta
"""

#%%

#1.

filename = r'C:\Users\gadta\Documents\IO assignment\othello_gutenberg.txt'


import re


def findHapax(filename):
    counts = {}
    with open(filename, "r") as handler:
        for y in re.findall("[a-z]+", handler.read().lower()):
            counts[y] = counts.get(y, 0) + 1
    return [key for key, value in counts.items() if value == 1]


print(findHapax(filename))

#%%

#2.

inputFile = r'C:\Users\gadta\Documents\IO assignment\learning_python.txt'
outputFile = r'C:\Users\gadta\Documents\IO assignment\output_file.txt'


def appendLine(inputFile, outputFile):
    _temp = ""
    _acc = 1
    for line in open(inputFile):
        _temp += f"{_acc} | {line}"
        _acc += 1
    with open(outputFile, "w+") as handler:
        handler.write(_temp)


appendLine(inputFile,outputFile)

#%%

#3.
filename = r'C:\Users\gadta\Documents\IO assignment\othello_gutenberg.txt'

import re


def calcAverage(filename):
    counts = {}
    with open(filename, "r") as handler:
        for y in re.findall("[a-z]+", handler.read().lower()):
            counts[y] = counts.get(y, 0) + 1
    total = 0
    totalWords = 0
    for key, val in counts.items():
        total += len(key)*val
        totalWords += val
    return total/totalWords


print(calcAverage(filename))

#%%

#5.

filename = r'C:\Users\gadta\Documents\IO assignment\mrmiyagi.txt'

import re


def sentanceSplitter(filename):
    with open(filename, "r") as handler:
        data = handler.read()
    sentences = re.sub(r"(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])", r".\n\1", data)
    sentences = re.sub(r"!\s", "!\n", sentences)
    sentences = re.sub(r"\?\s", "?\n", sentences)
    return sentences


print(sentanceSplitter(filename))