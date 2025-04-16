# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 18:37:18 2025

@author: USER
"""

def communicatin_vessels(*iterables):
    """Interleaves multiple iterables by yielding one item at a time from each,
    in the order they are zipped.

    Parameters:
    *iterables: Any number of iterable objects (e.g., strings, lists, tuples) of equal length.

    Yields:
    Elements from the input iterables, interleaved one by one.
    """

    for group in zip(*iterables):
        yield from group


if __name__ == '__main__':
    """
    Main function
    """
    print(list(communicatin_vessels('abc', [1, 2, 3], ('!', '@', '#'))))
