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

// Merges two subarrays of array[].
// First subarray is arr[begin..mid]
// Second subarray is arr[mid+1..end]
void merge(int array[], int const left, int const mid, int const right)
{
    auto const subArrayOne = mid - left + 1;
    auto const subArrayTwo = right - mid;

    // Create temp arrays
    auto* leftArray = new int[subArrayOne],
        * rightArray = new int[subArrayTwo];

    // Copy data to temp arrays leftArray[] and rightArray[]
    for (auto i = 0; i < subArrayOne; i++)
        leftArray[i] = array[left + i];
    for (auto j = 0; j < subArrayTwo; j++)
        rightArray[j] = array[mid + 1 + j];

    auto indexOfSubArrayOne = 0, // Initial index of first sub-array
        indexOfSubArrayTwo = 0; // Initial index of second sub-array
    int indexOfMergedArray = left; // Initial index of merged array

    // Merge the temp arrays back into array[left..right]
    while (indexOfSubArrayOne < subArrayOne && indexOfSubArrayTwo < subArrayTwo) {
        if (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]) {
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
        }
        else {
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
        }
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // left[], if there are any
    while (indexOfSubArrayOne < subArrayOne) {
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
        indexOfSubArrayOne++;
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // left[], if there are any
    while (indexOfSubArrayTwo < subArrayTwo) {
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
        indexOfSubArrayTwo++;
        indexOfMergedArray++;
    }
}

// begin is for left index and end is
// right index of the sub-array
// of arr to be sorted */
void mergeSort(int array[], int const begin, int const end)
{
    if (begin >= end)
        return; // Returns recursivly

    auto mid = begin + (end - begin) / 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}

int main()
{
    int arr2[] = { 100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000 };
    int n = sizeof(arr2) / sizeof(arr2[0]);
    string str1 = "";

    for (int i = 0; i < n; i++) {
        int num = arr2[i];
        int* ar = nullptr;
        ar = new int[num];
        ifstream file("archivo" + to_string(num) + ".txt");

        if (file.is_open())
        {
            for (int i = 0; i < num; ++i)
            {
                file >> ar[i];
            }
            file.close();
        }
        cout << num << endl;
        auto t0 = high_resolution_clock::now();
        mergeSort(ar, 0, num - 1);
        auto t1 = high_resolution_clock::now();
        auto ms_int = duration_cast<milliseconds>(t1 - t0);
        duration<double, std::milli> ms_double = t1 - t0;
        str1 = str1 + to_string(num) + " " + to_string(ms_double.count()) + "\n";
    }

    ofstream MyFile("ResMergeSortCPlusPlus.txt");
    MyFile << str1 << endl;
    MyFile.close();

    return 0;
}