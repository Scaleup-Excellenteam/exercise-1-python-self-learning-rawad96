# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 16:01:14 2025

@author: USER
"""

def group_by(func, Iter):
    """
     Groups elements from the given iterable based on the result of applying a function to each element.

    Parameters:
    func (callable): A function that takes a single argument and returns a value to group by.
    iterable (iterable): A sequence of elements to be grouped.

    Returns:
    returned_dict (dict): A dictionary where each key is a value returned by `func`, and each value is a list
          of elements from `iterable` for which `func(element)` equals that key.
    """
    returned_dict = {}
    for parametr in Iter:
        result = func(parametr)
        if result not in returned_dict:
            returned_dict[result] = [parametr]
        else:
            returned_dict[result].append(parametr)

    return returned_dict

if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
