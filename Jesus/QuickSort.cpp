/* C implementation QuickSort */
#include <stdio.h>
#include <iostream>
#include <chrono>
#include <fstream>
#include <string>
#include <windows.h>
#include <limits.h>
#include <algorithm>
#include <vector>
using namespace std;
using namespace std::chrono;
float t0, t1;


void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];    // pivot
    int i = (low - 1);  // Index of smaller element

    for (int j = low; j <= high - 1; j++)
    {
        // If current element is smaller than or
        // equal to pivot
        if (arr[j] <= pivot)
        {
            i++;    // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        int pi = partition(arr, low, high);

        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}


int main()
{
	int arr2[] = { 100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000 };
	int n = sizeof(arr2) / sizeof(arr2[0]);
	string str1 = "";

	for (int i = 0; i < n; i++) {
		int num = arr2[i];
		int* arr = nullptr;
		arr = new int[num];
		ifstream file("archivo" + to_string(num) + ".txt");

		if (file.is_open())
		{
			for (int i = 0; i < num; ++i)
			{
				file >> arr[i];
			}
			file.close();
		}
		cout << num << endl;
		auto t0 = high_resolution_clock::now();
		quickSort(arr, 0, num - 1);
		auto t1 = high_resolution_clock::now();
		auto ms_int = duration_cast<milliseconds>(t1 - t0);
		duration<double, std::milli> ms_double = t1 - t0;
		str1 = str1 + to_string(num) + " " + to_string(ms_double.count()) + "\n";
	}

	ofstream MyFile("ResQuickSortCPlusPlus.txt");
	MyFile << str1 << endl;
	MyFile.close();

	return 0;
}
