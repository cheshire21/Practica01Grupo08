import numpy as np
import time


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
            # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1


str1 = ''
list_pruebas = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

for canti_data in list_pruebas:
	print(canti_data)
	arr = np.loadtxt(f"archivo{canti_data}.txt", dtype=int)
	inicio = time.time()
	mergeSort(arr)
	fin = time.time()
	result = f'{(fin - inicio)*1000}'
	if canti_data != 100000:
		str1+= str(canti_data) + ' ' +  str(result) + '\n'
	else:
	    str1+= str(result)
    

file = open("ResMergeSortPython.txt", "w")
file. write(str1)    
file. close()

