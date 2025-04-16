# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 18:21:53 2025

@author: USER
"""

def cup_of_join(*lists, sep='-'):
     if not lists:
        return None
     if len(lists) == 1:
        return lists[0]
    
     result = []
     for i, lst in enumerate(lists):
        if i > 0:
            result.append(sep)
        result.extend(lst)
     return result
 
if __name__ == '__main__':
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))