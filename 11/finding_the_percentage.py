'''
Created on 07.01.2021

@author: Joe
'''

if __name__ == '__main__':
    n = int(input())
    list = []
    for i in range(n):
        inputs = input().split()
        command = inputs[0]

        if(command == "insert"):
            position, value = inputs[1], inputs[2]
            list.insert(int(position), int(value))
        if(command == "append"):
            value = inputs[1]
            list.append(int(value))
        if(command == "sort"):
            list.sort()
        if(command == "pop"):
            list.pop()
        if(command == "remove"):
            list.remove(int(value)) 
        if(command == "print"):
            print(list)                  
        if(command == "reverse"):
            list.reverse()    
    