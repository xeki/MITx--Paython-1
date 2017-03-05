# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 23:53:29 2016

@author:
    
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """


def convert_to_mandarin(us_num):
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
        '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    ans = ""
    if us_num <= 10:
        ans = trans.get(str(us_num))
    elif us_num < 20:
        ones = us_num %10
        ans = trans.get('10') + " " + trans.get(str(ones))
    else:
        tenths = int(us_num/10)
        ones = us_num%10
        ans += trans.get(str(tenths)) + " " + trans.get(str(10))
        if ones!= 0:
            ans += " " + trans.get(str(ones))
    return ans
        
def longestRunExtended(L):
    indexInc = [len(L)-1]
    indexDec = [len(L)-1]
    dicInc = {}
    dicDec = {}
    for i in range(len(L)-1):
        if L[i+1] < L[i]:
            indexInc.append(i)
    for j in range(len(L)-1):
        if L[j+1] > L[j]:
            indexDec.append(j)
    indexInc.sort()
    indexDec.sort()
    index = 0
    maxCount = 0
    for i in range(len(indexInc)):
        tempL = L[:]
        tempL = tempL[index:indexInc[i]+1]
        index = indexInc[i]+1
        if maxCount < len(tempL):
            dicInc = {}
            dicInc[0] = (i,len(tempL),sum(tempL))
            maxCount = len(tempL)
    print(dicInc)
    index = 0
    maxCount = 0
    for i in range(len(indexDec)):
        tempL = L[:]
        tempL = tempL[index:indexDec[i]+1]
        index = indexDec[i]+1
        if maxCount < len(tempL):
            dicDec = {}
            dicDec[0] = (i,len(tempL),sum(tempL))
            maxCount = len(tempL)
    print(dicDec)        
    print(" Increasing {} \n Decreasing{}".format(indexInc,indexDec))
    incIndex,incCount,incSum = dicInc.get(0)
    decIndex,decCount,decSum = dicDec.get(0)
    if incCount > decCount:
        print("Longest Sum: ",incSum)
    elif decCount > incCount:
        print("Longest Sum",decSum)
    elif incIndex < decIndex:
        print("Longest Sum: ",incSum)
    else:
         print("Longest Sum",decSum)
    
L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]     
        
def longest_run(L):
    indexInc = [len(L)-1]
    indexDec = [len(L)-1]
    dicInc = {}
    dicDec = {}
    for i in range(len(L)-1):
        if L[i+1] < L[i]:
            indexInc.append(i)
    for j in range(len(L)-1):
        if L[j+1] > L[j]:
            indexDec.append(j)
    indexInc.sort()
    indexDec.sort()
    index = 0
    maxCount = 0
    for i in range(len(indexInc)):
        tempL = L[:]
        tempL = tempL[index:indexInc[i]+1]
        index = indexInc[i]+1
        if maxCount < len(tempL):
            dicInc = {}
            dicInc[0] = (i,len(tempL),sum(tempL))
            maxCount = len(tempL)
    index = 0
    maxCount = 0
    for i in range(len(indexDec)):
        tempL = L[:]
        tempL = tempL[index:indexDec[i]+1]
        index = indexDec[i]+1
        if maxCount < len(tempL):
            dicDec = {}
            dicDec[0] = (i,len(tempL),sum(tempL))
            maxCount = len(tempL)
    incIndex,incCount,incSum = dicInc.get(0)
    decIndex,decCount,decSum = dicDec.get(0)
    if incCount > decCount:
        return incSum
    elif decCount > incCount:
        return decSum
    elif incIndex < decIndex:
        return incSum
    else:
        return decSum
    
L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]     