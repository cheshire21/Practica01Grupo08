import matplotlib.pyplot as plt
import numpy as np 

from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter

def main():
    #Generate Bubble Sort 
    resMergeSortC = np.loadtxt("ResMergeSortCPlusPlus.txt", dtype='f')
    resMergeSortPy = np.loadtxt("ResMergeSortPython.txt", dtype='f')

    
    ax = plt.subplot(1,2,1)
    # plt.subplot(1, 2, 1)
    # ax.title('Bubble Sort')
    ax.plot(resMergeSortC[:,0],resMergeSortC[:,1], color='green', linewidth=2.0, linestyle='-', label='C++')
    ax.plot(resMergeSortPy[:,0],resMergeSortPy[:,1], color='orange', linewidth=2.0, linestyle='-', label='Python')
    
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

    plt.title('Merge Sort')
    plt.xlabel('Data')
    plt.ylabel('Miliseconds')
    plt.legend(loc='upper left')
    
    #Generate Counting Sort 
    resQuickSortC = np.loadtxt("ResQuickSortCPlusPlus.txt", dtype='f')
    resQuickSortPy = np.loadtxt("ResQuickSortPython.txt", dtype='f')
    
    ax2 = plt.subplot(1, 2, 2)
    plt.title('Quick Sort')
    ax2.plot(resQuickSortC[:,0],resQuickSortC[:,1], color='green', linewidth=2.0, linestyle='-', label='C++ ')
    ax2.plot(resQuickSortPy[:,0],resQuickSortPy[:,1], color='orange', linewidth=2.0, linestyle='-', label='Python')
    
    ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    ax2.xaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

    plt.xlabel('Data')
    plt.ylabel('Miliseconds')
    plt.legend(loc='upper left')
    
    plt.show()

main()