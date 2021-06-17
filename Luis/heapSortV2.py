# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:42:08 2021
@author: Luis
"""
import matplotlib
import numpy as np
import time 
# Versión 1
#def heapify(arr,n,i):
#    parent=i
#    lChild=2*i+1
#    rChild=2*i+2
#    if(lChild<n and arr[lChild]>arr[parent]):
#        parent=lChild
#    if(rChild<n and arr[rChild]>arr[parent]):
#        parent=rChild
#    if(parent!=i):
#        arr[i],arr[parent] = arr[parent],arr[i] 
#        heapify(arr, n, parent)
#def heapsort(arr):
#    for i in range(len(arr) // 2 - 1, -1, -1):
#        heapify(arr, len(arr), i)
#    for i in range(len(arr)-1, 0, -1):
#        arr[i], arr[0] = arr[0], arr[i] 
#        heapify(arr, i, 0)
# Fin version 1
def inserta_en_monticulo(arr,n):
    for i in range(2,n):
        k=i
        band=True
        while((k>1)and(band==True)):
            band=False
            aux=arr[(k//2)]
            arr[(k//2)]=arr[k]
            arr[k]=aux
            k=k//2
            band=True
def elimina_monticulo(arr,n):
    for i in range(n-1,2,-1):
        aux=arr[i]
        arr[i]=arr[1]
        izq=2
        der=3
        k=1
        band=True
        while((izq<i) and (band==True)):
            mayor=arr[izq]
            ap=izq
            if((mayor<arr[der]) and (der!=i)):
                mayor=arr[der]
                ap=der
            if(aux<mayor):
                arr[k]=arr[ap]
                k=ap
            else:
                band=False
            izq=k*2
            der=k*2+1
        arr[k]=aux
def heapSort(arr):
    inserta_en_monticulo(arr, len(arr))
    elimina_monticulo(arr, len(arr))
          
        

str1 = ''
arr2 = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
canti_data=100000
for canti_data in arr2:
	print(canti_data)
	arr = np.loadtxt(f"./data/archivo{canti_data}.txt", dtype=int)
	inicio = time.time()
	heapSort(arr)
	fin = time.time()
	result = f'{(fin - inicio)*1000}'
	if canti_data <= 100000:
		str1+= str(canti_data) + ',' +  str(result) + '\n'
file = open("./heapSortPython.csv", "w")
file. write(str1)    
file. close()





