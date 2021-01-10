'''
Created on 07.01.2021

@author: Joe
'''

if __name__ == '__main__':
    n = int(input())
    students = dict()
    for i in range(n):
        inputs = input().split()
        key = inputs[0]
        value = [float(i) for i in inputs[1:]]
        '''   value = []
        for i in inputs[1:]:
            value.append(int(i))'''
        students[key]=value
    query_name = input()
    list_scores = students[query_name]
    sum = 0
    for i in list_scores:
        sum = sum +i
    average = sum / len(list_scores)    
    print('%.2f' % average)
    