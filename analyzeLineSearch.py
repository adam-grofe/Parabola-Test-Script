#!/usr/bin/env python
import numpy as np
from lmfit.models import ParabolicModel
import sys

nArgs = len(sys.argv)
print(sys.argv)

assert nArgs == 2

nPts = 5;
fileName = sys.argv[1]



def computeError(x,y):
    xArr = np.array(x)
    yArr = np.array(y)
    qmodel = ParabolicModel()
    result = qmodel.fit(yArr, x=xArr, a=1, b=2, c=0)
    print(result.fit_report())
    return result.chisqr


def parseFile(fileName, nPts):
    err = []
    with open(fileName) as f:
        for line in f:
            if line.find("Performing Line Search:") != -1:
                print("\n\n")
                x = [];
                y = [];
                for i in range(nPts):
                    [xPt,yPt] = f.readline().split()
                    x.append(xPt)
                    y.append(yPt)
                err.append(computeError(x,y))
    print("\nChi-Squares:")
    for e in err:
        print(e)
            
print("File Name = " + fileName)
print("Number of Points in Line Search = " + str(nPts))
parseFile(fileName,nPts)
