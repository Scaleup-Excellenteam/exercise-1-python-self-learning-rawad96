# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 18:37:18 2025

@author: USER
"""

def communicatin_vessels(*iterables):
    for group in zip(*iterables):
        for item in group:
            yield item
            
            
if __name__ == '__main__':
    print(list(communicatin_vessels('abc', [1, 2, 3], ('!', '@', '#'))))