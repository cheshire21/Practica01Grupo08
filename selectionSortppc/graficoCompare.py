import matplotlib.pyplot as plt
import numpy as np 

from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter

def main():
    #Generate Bubble Sort 
    resBubbleSortC = np.loadtxt("selectionSortCplusplus.txt", dtype='f',delimiter=',')
    resBubbleSortPy = np.loadtxt("selectionSortPython.csv", dtype='f',delimiter=',')

    
    ax = plt.subplot(1,2,1)
    # plt.subplot(1, 2, 1)
    # ax.title('Bubble Sort')

    

    ax.plot(resBubbleSortC[:,0],resBubbleSortC[:,1], color='green', linewidth=2.0, linestyle='-', label='C++')
    ax.plot(resBubbleSortPy[:,0],resBubbleSortPy[:,1], color='orange', linewidth=2.0, linestyle='-', label='Python')
    
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,}'))

    plt.title('Selection Sort')
    plt.xlabel('Data')
    plt.ylabel('Miliseconds')
    plt.legend(loc='upper left')
    
    #Generate Counting Sort 
    
    
    plt.show()

main()