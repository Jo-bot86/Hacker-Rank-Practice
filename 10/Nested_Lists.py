'''
Created on 05.01.2021

@author: Joe
'''
from test.datetimetester import SEC

if __name__ == '__main__':
    arr = []
    
    for i in range(int(input())):
        sub_arr = []
        name = input()
        sub_arr.append(name)
        score = float(input())
        sub_arr.append(score)
        arr.append(sub_arr)    
    lowest_score = arr[0][1]
    sec_lowest_sore = arr[1][1]
    lowest_score = min(arr[0][1], arr[1][1])
    sec_lowest_score = max(arr[0][1], arr[1][1])    
    for i in range(len(arr)):
        name=arr[i][0] 
        score=arr[i][1]
        if(score < lowest_score):
            sec_lowest_score = lowest_score
            lowest_score = score
        if(score >lowest_score and score < sec_lowest_score):
            sec_lowest_score = score
        if(lowest_score==sec_lowest_score):
            if(score < lowest_score):
                lowest_score = score
            if(score> lowest_score):
                sec_lowest_score = score        
    arr_name = []        
    for i in range(len(arr)):
        if(arr[i][1]== sec_lowest_score):
            arr_name.append(arr[i][0])
    arr_name.sort()
    for i in range(len(arr_name)):
        print(arr_name[i])               