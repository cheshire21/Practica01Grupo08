import matplotlib.pyplot as plt
import numpy as np 

from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter

def main():
    #Generate Bubble Sort 
    resBubbleSortC = np.loadtxt("./ResBubbleSortCPlusPlus.txt", dtype='f')
    resBubbleSortPy = np.loadtxt("./ResBubbleSortPython.txt", dtype='f')

    
    ax = plt.subplot(1,2,1)
    # plt.subplot(1, 2, 1)
    # ax.title('Bubble Sort')
    ax.plot(resBubbleSortC[:,0],resBubbleSortC[:,1], color='green', linewidth=2.0, linestyle='-', label='C++')
    ax.plot(resBubbleSortPy[:,0],resBubbleSortPy[:,1], color='orange', linewidth=2.0, linestyle='-', label='Python')
    
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

    plt.title('Bubble Sort')
    plt.xlabel('Data')
    plt.ylabel('Miliseconds')
    plt.legend(loc='upper left')
    
    #Generate Counting Sort 
    resCountSortC = np.loadtxt("./ResCountingSortCPlusPlus.txt", dtype='f')
    resCountSortPy = np.loadtxt("./ResCountingSortPython.txt", dtype='f')
    
    ax2 = plt.subplot(1, 2, 2)
    plt.title('Counting Sort')
    ax2.plot(resCountSortC[:,0],resCountSortC[:,1], color='green', linewidth=2.0, linestyle='-', label='C++ ')
    ax2.plot(resCountSortPy[:,0],resCountSortPy[:,1], color='orange', linewidth=2.0, linestyle='-', label='Python')
    
    ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    ax2.xaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

    plt.xlabel('Data')
    plt.ylabel('Miliseconds')
    plt.legend(loc='upper left')
    
    plt.show()

main()