import numpy as np
import time 

def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]


str1 = ''

arr2 = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

for canti_data in arr2:
	print(canti_data)
	arr = np.loadtxt(f"./data/archivo{canti_data}.txt", dtype=int)
	inicio = time.time()
	bubbleSort(arr)
	fin = time.time()
	result = f'{(fin - inicio)*1000}'
	if canti_data != 100000:
		str1+= str(canti_data) + ' ' +  str(result) + '\n'
	else:
	    str1+= str(canti_data) + ' ' + str(result)

file = open("./ResBubbleSortPython1.txt", "w")
file. write(str1)    
file. close()

