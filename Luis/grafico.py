# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 06:20:00 2021

@author: Luis
"""



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Lectura de resultados algoritmo heapSort
df_python_heapSort = pd.read_csv('E:/2021/UNSA/Semestre I/Algoritmos/Practica/Trabajo en equipo/python/data/heapSortPython.csv',header=None)
df_c_heapSort = np.loadtxt('E:/2021/UNSA/Semestre I/Algoritmos/Practica/Trabajo en equipo/c++/data/heapSortV2Cplus.txt', delimiter=",",skiprows=0,usecols=[0,1])
df_c_heapSort=pd.DataFrame(df_c_heapSort)

x_1 = df_python_heapSort.iloc[:,0]
y_1=df_python_heapSort.iloc[:,1]
y_2=df_c_heapSort.iloc[:,1]

# Gráfica algoritmo HeapSort
plt.title("Algoritmo HeapSort", position=(0.5, 0.9),
          fontdict={'family': 'helvetica', 
                    'color' : 'black',
                    #'weight': 'none',
                    'size': 14})

plt.plot(x_1, y_1, marker="+",label="Python",linestyle = ":",mec = "g",mew = 1.8,ms = 10)
plt.plot(x_1, y_2, marker="+",label="C++",linestyle = ":",mec = "orange",mew = 1.8,ms = 10)
plt.xlabel('Cantidad de datos')
plt.ylabel('Tiempo en milisegundos')
#plt.plot(x_1, y_2, marker="*",label="C++",linestyle = ":")
leg = plt.legend(loc='best', ncol=1, mode="", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)
plt.show()

# Lectura de resultados algoritmo heapSort
df_python_insertionSort = pd.read_csv('E:/2021/UNSA/Semestre I/Algoritmos/Practica/Trabajo en equipo/python/data/insertionSortPython.csv',header=None)
df_c_insertionSort = np.loadtxt('E:/2021/UNSA/Semestre I/Algoritmos/Practica/Trabajo en equipo/c++/data/insertionSortCplus.txt', delimiter=",",skiprows=0,usecols=[0,1])
df_c_insertionSort=pd.DataFrame(df_c_insertionSort)

x_11 = df_python_insertionSort.iloc[:,0]
y_11=df_python_insertionSort.iloc[:,1]
y_22=df_c_insertionSort.iloc[:,1]


# Gráfica algoritmo HeapSort
plt.title("Algoritmo Insertion Sort", position=(0.5, 0.9),
          fontdict={'family': 'helvetica', 
                    'color' : 'black',
                    #'weight': 'none',
                    'size': 14})

plt.plot(x_11, y_11, marker="+",label="Python",linestyle = ":",mec = "g",mew = 1.8,ms = 10)
plt.plot(x_11, y_22, marker="+",label="C++",linestyle = ":",mec = "orange",mew = 1.8,ms = 10)
plt.xlabel('Cantidad de datos')
plt.ylabel('Tiempo en milisegundos')
#plt.plot(x_1, y_2, marker="*",label="C++",linestyle = ":")
leg = plt.legend(loc='best', ncol=1, mode="", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)
plt.show()



