'''
Created on 15.12.2020

@author: Joe
'''
from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    NewListOfTupel=[]
    ListOfTupel = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    print("List of all tupel: "  + str(ListOfTupel))
    for c in ListOfTupel:
        if c[0] + c[1] + c[2] != n:
            NewListOfTupel.append(c)
        
    print("final list of tupel: " + str(NewListOfTupel))