'''
Created on 05.01.2021

@author: Joe
'''

if __name__ == '__main__':
    n = 7
    arr = [4, 2, 8, 1, 9, 1]
    runner_up_score = arr[0]
    highest_score = arr[1]
    for i in range(len(arr)):
        if(highest_score < arr[i]):
           runner_up_score = highest_score
           highest_score = arr[i] 
        if(highest_score > arr[i] and runner_up_score < arr[i]):
            runner_up_score = arr[i]
          
    print(runner_up_score)         
        
    
           