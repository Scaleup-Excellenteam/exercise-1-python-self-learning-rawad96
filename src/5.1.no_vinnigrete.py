# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 17:38:09 2025

@author: USER
"""

import datetime
import random

def no_vinnigrete(startDate, endDate):
    
    startDate_Date = datetime.date.fromisoformat(startDate)
    endDate_Date = datetime.date.fromisoformat(endDate)
    
    startDateInt = startDate_Date.toordinal()
    endDateInt = endDate_Date.toordinal()
    
    random_IntDate = random.randint(startDateInt, endDateInt)
    randomDate = datetime.date.fromordinal(random_IntDate)
    
    if randomDate.weekday() == 0:
        print("No Vinnigrete!")
    
    return randomDate
    
    
if __name__ == '__main__':
    start = input("(YYYY-MM-DD): ")
    end = input("(YYYY-MM-DD): ")
    print(no_vinnigrete(start, end))