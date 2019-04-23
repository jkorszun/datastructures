#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:51:41 2019

@author: jkorszun
"""

#heapify subtree rooted at index i
# n is size of heap

def heapify(arr, n, i):
    largest = i #initialize largest as root
    l = 2 * i + 1 #left child 
    r = 2 * i + 2 #right child
    
    #see if left child of root exists 
    #see if greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
        
    #see if right child of root exists and is
    #greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
        
    #Change root if necessary
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] #swap
        
        #heapify root
        heapify(arr, n, largest)

#main function //sort array by given size
def heapSort(arr):
    n = len(arr)
    
    #Build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        
    #extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
#start
arr = [12,11,13,5,6,7]
heapSort(arr)
n = len(arr)
print("Sorted array is: ")

for i in range(n):
    print("%d" %arr[i])

    