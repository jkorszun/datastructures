#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:05:05 2019

@author: jkorszun
"""

#Recursive Insertion Sort
def insertionSortRec(arr,n):
    #base case
    if n<=1:
        return
    
    #Sort first n-1 elements
    insertionSortRec(arr, n-1)
    
    last = arr[n-1]
    j = n-2
    
    #Move elements that are greater than
    #key to repsectable position
    
    while(j >=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
        
    arr[j+1]= last
    
#main function
arr = [12,11,13,5,6]
n = len(arr)
insertionSortRec(arr, n)
print(arr)