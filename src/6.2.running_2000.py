# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 02:38:07 2025

@author: USER
"""
import time

def running_2000(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    
    return end - start

if __name__ == '__main__':
    print(running_2000(print, "Hello"))



