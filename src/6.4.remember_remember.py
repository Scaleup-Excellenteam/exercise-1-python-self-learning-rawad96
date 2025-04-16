# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 15:48:46 2025

@author: USER
"""
from PIL import Image

def remember_remember(img_path):
    """Extracts a hidden message from an encoded image.

    The image is encoded such that each column contains exactly one black pixel.
    The row index of this black pixel corresponds to the ASCII value of a character.
    Reading the black pixel positions from left to right reveals the hidden message.

    Parameters:
        img_path (str): The file path to the encoded image.

    Returns:
        returned_message (str): The decoded hidden message.
    """

    img = Image.open(img_path)

    pixels = img.load()
    width, height = img.size

    returned_message = ''

    for x in range(width):
        for y in range(height):
            if pixels[x, y] == (0, 0, 0):
                returned_message += chr(y)
                break

    return returned_message

if __name__ == '__main__':
    """
    Main function
    """
    print(remember_remember("C:\\Users\\USER\\git-pull-request-training-rawad96\\code.png"))
