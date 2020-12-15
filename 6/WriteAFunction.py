'''
Created on 14.12.2020

@author: Joe
'''
from pip._vendor.distlib.compat import raw_input

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True 
            else:
                leap = False
        else:
            leap = True
    return leap 

year = int(raw_input()) 
print(is_leap(year))             