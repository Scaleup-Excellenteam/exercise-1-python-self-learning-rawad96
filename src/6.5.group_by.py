# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 16:01:14 2025

@author: USER
"""

def group_by(func, Iter):
    returnedDict = {}
    for parametr in Iter:
        result = func(parametr)
        if result not in returnedDict:
            returnedDict[result] = [parametr]
        else:
            returnedDict[result].append(parametr)
            
    return returnedDict

if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))