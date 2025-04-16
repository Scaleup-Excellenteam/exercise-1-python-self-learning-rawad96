# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 17:10:05 2025

@author: USER
"""
import os

def thats_the_way(folderPath):
    if not os.path.isdir(folderPath):
        return []
    
    returnedFiles = []
    for fileName in os.listdir(folderPath):
        filePath = os.path.join(folderPath, fileName)
        if os.path.isfile(filePath) and fileName.startswith("deep"):
            returnedFiles.append(fileName)
    
    return returnedFiles
    
    
if __name__ == '__main__':
    print(thats_the_way("C:\\Users\\USER\\git-pull-request-training-rawad96\\Images"))
    