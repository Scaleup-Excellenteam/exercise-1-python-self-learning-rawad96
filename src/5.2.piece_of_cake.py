# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 18:31:55 2025

@author: USER
"""

def piece_of_cake(prices, optionals=None, **kwargs):
    """
    Calculates the total cost of ingredients required for a recipe.

    Parameters:
    prices (dict): A dictionary where each key is the name of an ingredient (as a single word, no spaces or special characters),
                   and the value is the price per 100 grams of that ingredient.
                   Example: {'flour': 3.5, 'milk': 4.0}

    optionals (list, optional): A list of ingredient names (strings) to ignore in the calculation.
                                These ingredients will not be included in the total price.
                                If not provided, all ingredients passed as keyword arguments will be considered.

    **kwargs: Each keyword argument should correspond to an ingredient listed in `prices`.
              The value of each argument should be the quantity (in grams) of that ingredient required for the recipe.

    Returns:
    total_price (int): The total cost (rounded down to the nearest integer) to purchase the specified ingredients,
         excluding any that are marked as optional.
    """
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
