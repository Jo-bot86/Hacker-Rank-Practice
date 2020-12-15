'''
Created on 14.12.2020

@author: Joe
'''
#from __future__ import print_function
from pip._vendor.distlib.compat import raw_input


if __name__ == '__main__':
    n = int(raw_input())
    print(*range(1,n+1),sep = "")
    
    # We can use argument-unpacking operator i.e. *.
    val = [*range(1,5)]
    print(val)
    
    
    

    
