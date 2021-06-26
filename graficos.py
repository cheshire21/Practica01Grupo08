import matplotlib.pyplot as plt
import numpy as np 

from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter

def main():
    str1 = "./result/" 
    #Generate Bubble Sort 
    resBubbleSortC = np.loadtxt(str1+"ResBubbleSortCPlusPlus.txt", dtype='f')
    resBubbleSortPy = np.loadtxt(str1+"ResBubbleSortPython.txt", dtype='f')

    
    ax = plt.subplot(1,2,1)
    # plt.subplot(1, 2, 1)
    # ax.title('Bubble Sort')
    ax.plot(resBubbleSortC[:,0],resBubbleSortC[:,1], color='green', linewidth=2.0, linestyle='-', label='C++')
    ax.plot(resBubbleSortPy[:,0],resBubbleSortPy[:,1], color='orange', linewidth=2.0, linestyle='-', label='Python')
    
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

    plt.title('Algoritmo Bubble Sort')
    plt.xlabel('Cantidad de Datos')
    plt.ylabel('Tiempo en Milisegundos')
    plt.legend(loc='upper left')
    
    #Generate Counting Sort 
    resCountSortC = np.loadtxt(str1+"ResCountingSortCPlusPlus.txt", dtype='f')
    resCountSortPy = np.loadtxt(str1+"ResCountingSortPython.txt", dtype='f')
    
    ax2 = plt.subplot(1, 2, 2)
    plt.title('Algoritmo Counting Sort')
    ax2.plot(resCountSortC[:,0],resCountSortC[:,1], color='green', linewidth=2.0, linestyle='-', label='C++ ')
    ax2.plot(resCountSortPy[:,0],resCountSortPy[:,1], color='orange', linewidth=2.0, linestyle='-', label='Python')
    
    ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    ax2.xaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

    plt.xlabel('Cantidad de Datos')
    plt.ylabel('Tiempo en Milisegundos')
    plt.legend(loc='upper left')
    plt.show()

    #Generate Sort 
    
    resHeapSortC = np.loadtxt(str1+"HeapSortCPlus.txt", dtype='f')
    resHeapSortPy = np.loadtxt(str1+"heapSortPython.txt", dtype='f')

    resInsertionSortC = np.loadtxt(str1+"insertionSortCPlus.txt", dtype='f')
    resInsertionSortPy = np.loadtxt(str1+"insertionSortPython.txt", dtype='f')

    resMergeSortC = np.loadtxt(str1+"ResMergeSortCPlusPlus.txt", dtype='f')
    resMergeSortPy = np.loadtxt(str1+"ResMergeSortPython.txt", dtype='f')

    resQuickSortC = np.loadtxt(str1+"ResQuickSortCPlusPlus.txt", dtype='f')
    resQuickSortPy = np.loadtxt(str1+"ResQuickSortPython.txt", dtype='f')

    resSelectionSortC = np.loadtxt(str1+"SelectionSortC.txt", dtype='f')
    resSelectionSortPy = np.loadtxt(str1+"SelectionSortPy.txt", dtype='f')

    ax3 = plt.subplot(1, 2, 1)
    
    # ax3.plot(resBubbleSortC[:,0],resBubbleSortC[:,1], linestyle='-', label='Bubble Sort') #omitir
    ax3.plot(resCountSortC[:,0],resCountSortC[:,1],  linestyle='-', label='Counting Sort')
    ax3.plot(resHeapSortC[:,0],resHeapSortC[:,1],  linestyle='-', label='Heap Sort')
    # ax3.plot(resInsertionSortC[:,0],resInsertionSortC[:,1],  linestyle='-', label='Insertion Sort')#omitir
    ax3.plot(resMergeSortC[:,0],resMergeSortC[:,1],  linestyle='-', label='Merge Sort')
    ax3.plot(resQuickSortC[:,0],resQuickSortC[:,1],  linestyle='-', label='Quick Sort')
    # ax3.plot(resSelectionSortC[:,0],resSelectionSortC[:,1],  linestyle='-', label='Selection Sort')#omitir
    
    ax3.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    ax3.xaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    
    plt.title('Comparacion en C++')
    plt.xlabel('Cantidad de Datos')
    plt.ylabel('Tiempo en Milisegundos')
    plt.legend(loc='upper left')
    

    ax4 = plt.subplot(1, 2, 2)
    
    # ax4.plot(resBubbleSortPy[:,0],resBubbleSortPy[:,1], linestyle='-', label='Bubble Sort')#omitir
    ax4.plot(resCountSortPy[:,0],resCountSortPy[:,1],  linestyle='-', label='Counting Sort')
    ax4.plot(resHeapSortPy[:,0],resHeapSortPy[:,1], linestyle='-', label='Heap Sort')
    # ax4.plot(resInsertionSortPy[:,0],resInsertionSortPy[:,1], linestyle='-', label='Insertion Sort')#omitir
    ax4.plot(resMergeSortPy[:,0],resMergeSortPy[:,1], linestyle='-', label='Merge Sort')
    ax4.plot(resQuickSortPy[:,0],resQuickSortPy[:,1], linestyle='-', label='Quick Sort')
    # ax4.plot(resSelectionSortPy[:,0],resSelectionSortPy[:,1], linestyle='-', label='Selection Sort')#omitir
    
    ax4.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    ax4.xaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    
    plt.title('Comparacion en Python')
    plt.xlabel('Cantidad de Datos')
    plt.ylabel('Tiempo en Milisegundos')
    plt.legend(loc='upper left')
    
    plt.show()



main()