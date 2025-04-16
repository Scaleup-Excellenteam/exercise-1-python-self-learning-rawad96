"""
Created on Sat Apr  5 16:01:14 2025

@author: USER
"""

def group_by(func, iterr):
    """Groups elements from the given iterable based on the result of applying a function to each element.

    Parameters:
    func (callable): A function that takes a single argument and returns a value to group by.
    iterr (iterable): A sequence of elements to be grouped.

    Returns:
    returned_dict (dict): A dictionary where each key is a value returned by `func`, and each value is a list
          of elements from `iterable` for which `func(element)` equals that key.
    """

    returned_dict = {}
    for parametr in iterr:
        result = func(parametr)
        if result not in returned_dict:
            returned_dict[result] = [parametr]
        else:
            returned_dict[result].append(parametr)

    return returned_dict

if __name__ == '__main__':
    """
    Main function
    """
    print(group_by(len, ["hi", "bye", "yo", "try"]))
