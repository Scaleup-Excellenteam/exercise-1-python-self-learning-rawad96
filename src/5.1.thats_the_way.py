# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 17:10:05 2025

@author: USER
"""
import os

def thats_the_way(folder_path):
    """
    Returns a list of all filenames in the given directory that start with the prefix 'deep'.

    Parameters:
    folder_path (str): The path to the directory to search in.

    Returns:
    returned_files[str]: A list of filenames (not full paths) that start with 'deep'.

    Notes:
    - Only files (not subdirectories) are considered.
    """
    if not os.path.isdir(folder_path):
        return []

    returned_files = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.startswith("deep"):
            returned_files.append(file_name)

    return returned_files


if __name__ == '__main__':
    print(thats_the_way("C:\\Users\\USER\\git-pull-request-training-rawad96\\Images"))
