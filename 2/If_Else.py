'''
Created on 13.12.2020

@author: Joe
'''
from builtins import input

if __name__ == '__main__':
    x = int(input('Please enter a natural number! '))
    
    if x % 2 == 0:
        if 2 <= x <= 5:
            print('not weird')
        elif 6 <= x <= 20:
            print('weird')
        elif x > 20:
            print('not weird')
    else:
        print('weird')