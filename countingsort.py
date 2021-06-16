import numpy as np
import time 

def countingSort(arr):
	max_element = int(max(arr))
	min_element = int(min(arr))
	range_of_elements = max_element - min_element + 1
	# Create a count array to store count of individual
	# elements and initialize count array as 0
	count_arr = [0 for _ in range(range_of_elements)]
	output_arr = [0 for _ in range(len(arr))]

	# Store count of each character
	for i in range(0, len(arr)):
		count_arr[arr[i]-min_element] += 1

	# Change count_arr[i] so that count_arr[i] now contains actual
	# position of this element in output array
	for i in range(1, len(count_arr)):
		count_arr[i] += count_arr[i-1]

	# Build the output character array
	for i in range(len(arr)-1, -1, -1):
		output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
		count_arr[arr[i] - min_element] -= 1

	# Copy the output array to arr, so that arr now
	# contains sorted characters
	for i in range(0, len(arr)):
		arr[i] = output_arr[i]

	return arr


str1 = ''

arr2 = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

for canti_data in arr2:
	print(canti_data)
	arr = np.loadtxt(f"./data/archivo{canti_data}.txt", dtype=int)
	inicio = time.time()
	countingSort(arr)
	fin = time.time()
	result = f'{(fin - inicio)*1000}'
	if canti_data != 100000:
		str1+= str(canti_data) + ' ' +  str(result) + '\n'
	else:
	    str1+= str(result)

file = open("./ResCountingSortPython.txt", "w")
file. write(str1)    
file. close()

