# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 20:43:25 2021

@author: Luis
"""
import matplotlib
import numpy as np
import time 
def insercion(arr):
    for i in range(1, len(arr), 1):
        aux=arr[i]
        k=i-1
        while(k>=0 and aux<arr[k]):
            arr[k+1]=arr[k]
            k=k-1
        arr[k+1]=aux
def imprimir(array):
    for i in array:
        print(i)
        
str1 = ''
arr2 = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
canti_data=100000
for canti_data in arr2:
	print(canti_data)
	arr = np.loadtxt(f"./data/archivo{canti_data}.txt", dtype=int)
	inicio = time.time()
	insercion(arr)
	fin = time.time()
	result = f'{(fin - inicio)*1000}'
	if canti_data <= 100000:
		str1+= str(canti_data) + ',' +  str(result) + '\n'
file = open("./insertionSortPython.csv", "w")
file. write(str1)    
file. close()

# Activar confines de probar el funcionamiento del algoritmo, con el arreglo de 100 elementos
"""print("Luego de ordenar")
canti_data=100
arr = np.loadtxt(f"./data/archivo{canti_data}.txt", dtype=int)
insercion(arr)
imprimir(arr)
"""
