"""
Created on Fri Apr  4 17:38:09 2025

@author: USER
"""

import datetime
import random

def no_vinnigrete(start_date, end_date):
    """Generates a random date between start_date and end_date.

    Parameters:
    start_date (str): The start date.
    end_date (str): The end date.

    Returns:
    random_date [date]: A random date between start_date and end_date.
    """

    start_date_date = datetime.date.fromisoformat(start_date)
    end_date_date = datetime.date.fromisoformat(end_date)
    start_date_int = start_date_date.toordinal()
    end_date_int = end_date_date.toordinal()
    random_int_date = random.randint(start_date_int, end_date_int)
    random_date = datetime.date.fromordinal(random_int_date)
    if random_date.weekday() == 0:
        print("No Vinnigrete!")
    return random_date


if __name__ == '__main__':
    """
    Main function
    """
    start = input("(YYYY-MM-DD): ")
    end = input("(YYYY-MM-DD): ")
    print(no_vinnigrete(start, end))
