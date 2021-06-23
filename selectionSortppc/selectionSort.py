# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:42:08 2021
@author: PPC
"""
import matplotlib
import numpy as np
import time 

def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)-1):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]          




str1 = ''
arr2 = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
# arr2 = [100,200]
canti_data=100000
for canti_data in arr2:
	print(canti_data)
	arr = np.loadtxt(f"./data/archivo{canti_data}.txt", dtype=int)
	inicio = time.time()
	selection_sort(arr)
	fin = time.time()
	result = f'{(fin - inicio)*1000}'
	if canti_data <= 100000:
		str1+= str(canti_data) + ' ' +  str(result) + '\n'


file = open("./SelectionSortPy.txt", "w")
file. write(str1)    
file. close()





