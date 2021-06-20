# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 06:20:00 2021

@author: Luis
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Lectura de resultados algoritmo heapSort
df_python_heapSort = pd.read_csv('./heapSortPython.csv',header=None)
df_c_heapSort = np.loadtxt('./heapSortCplus.txt', delimiter=",",skiprows=0,usecols=[0,1])
df_c_heapSort=pd.DataFrame(df_c_heapSort)

x_1 = df_python_heapSort.iloc[:,0]
y_1=df_python_heapSort.iloc[:,1]
y_2=df_c_heapSort.iloc[:,1]

# Gráfica algoritmo HeapSort
plt.title("Algoritmo Heapsort", position=(0.5, 0.9),
          fontdict={'family': 'helvetica', 
                    'color' : 'black',
                    #'weight': 'none',
                    'size': 14})

#plt.plot(x_1, y_1, marker="+",label="Python",linestyle = ":",mec = "orange",mew = 1.8,ms = 10)
#plt.plot(x_1, y_2, marker="+",label="C++",linestyle = ":",mec = "g",mew = 1.8,ms = 10)
plt.plot(x_1,y_2, color='green', linewidth=2.0, linestyle='-', label='C++')
plt.plot(x_1,y_1, color='orange', linewidth=2.0, linestyle='-', label='Python')

plt.xlabel('Cantidad de datos')
plt.ylabel('Tiempo en milisegundos')
#plt.plot(x_1, y_2, marker="*",label="C++",linestyle = ":")
leg = plt.legend(loc='best', ncol=1, mode="", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)
plt.show()

# Lectura de resultados algoritmo heapSort
df_python_insertionSort = pd.read_csv('./insertionSortPython.csv',header=None)
df_c_insertionSort = np.loadtxt('./insertionSortCplus.txt', delimiter=",",skiprows=0,usecols=[0,1])
df_c_insertionSort=pd.DataFrame(df_c_insertionSort)

x_11 = df_python_insertionSort.iloc[:,0]
y_11=df_python_insertionSort.iloc[:,1]
y_22=df_c_insertionSort.iloc[:,1]


# Gráfica algoritmo HeapSort
plt.title("Algoritmo Inserción directa", position=(0.5, 0.9),
          fontdict={'family': 'helvetica', 
                    'color' : 'black',
                    #'weight': 'none',
                    'size': 14})

plt.plot(x_11,y_22, color='green', linewidth=2.0, linestyle='-', label='C++')
plt.plot(x_11,y_11, color='orange', linewidth=2.0, linestyle='-', label='Python')
plt.xlabel('Cantidad de datos')
plt.ylabel('Tiempo en milisegundos')
#plt.plot(x_1, y_2, marker="*",label="C++",linestyle = ":")
leg = plt.legend(loc='best', ncol=1, mode="", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)
plt.show()



