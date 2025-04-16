# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 18:31:55 2025

@author: USER
"""

def piece_of_cake(prices, optionals=None, **kwargs):
    if not prices:
        return 0
    
    total_price = 0
    optionals = optionals or []

    for ingredient, grams in kwargs.items():
        if ingredient in optionals:
            continue
        if ingredient in prices:
            price_per_100g = prices[ingredient]
            total_price += (grams / 100) * price_per_100g

    return int(total_price)


if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))