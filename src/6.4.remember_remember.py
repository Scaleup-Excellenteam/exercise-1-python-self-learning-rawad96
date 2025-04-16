# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 15:48:46 2025

@author: USER
"""
from PIL import Image

def remember_remember(imgPath):
    img = Image.open(imgPath)
    
    pixels = img.load()
    width, height = img.size
    
    returnedMessage = ''

    for x in range(width):
        for y in range(height):
            if pixels[x, y] == (0, 0, 0):
                returnedMessage += chr(y)
                break

    return returnedMessage

if __name__ == '__main__':
    print(remember_remember("C:\\Users\\USER\\git-pull-request-training-rawad96\\code.png"))

