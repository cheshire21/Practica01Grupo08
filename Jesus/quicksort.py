import numpy as np
import time 

def quicksort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return quicksort(izquierda)+centro+quicksort(derecha)
    else:
        return lista

str1 = ''
list_pruebas = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

for canti_data in list_pruebas:
	print(canti_data)
	arr = np.loadtxt(f"archivo{canti_data}.txt", dtype=int)
	inicio = time.time()
	quicksort(arr)
	fin = time.time()
	result = f'{(fin - inicio)*1000}'
	if canti_data != 100000:
		str1+= str(canti_data) + ' ' +  str(result) + '\n'
	else:
	    str1+= str(result)
    

file = open("ResQuickSortPython.txt", "w")
file. write(str1)    
file. close()
