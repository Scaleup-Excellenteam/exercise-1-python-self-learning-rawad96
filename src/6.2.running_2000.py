# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 02:38:07 2025

@author: USER
"""
import time

def running_2000(func, *args):
    """
    Measures and returns the execution time of the given function when called with the provided arguments.

    Parameters:
    func (callable): The function to be executed and timed.
    *args: Positional arguments to pass to the function `f`.

    Returns:
    float: The time taken (in seconds) to execute the function `f` with the arguments.
    """
    start = time.time()
    func(*args)
    end = time.time()

    return end - start    

if __name__ == '__main__':
    print(running_2000(print, "Hello"))
