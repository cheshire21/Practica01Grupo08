// heapSort.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
//

#include <stdio.h>
#include <iostream>
#include <chrono>
#include <fstream>
#include <string>
using namespace std;

using namespace std::chrono;
float t0, t1;
void heapify(int arr[], int n, int i)
{
	int largest = i; // Initialize largest as root
	int l = 2 * i + 1; // left = 2*i + 1
	int r = 2 * i + 2; // right = 2*i + 2

	// If left child is larger than root
	if (l < n && arr[l] > arr[largest])
		largest = l;

	// If right child is larger than largest so far
	if (r < n && arr[r] > arr[largest])
		largest = r;

	// If largest is not root
	if (largest != i) {
		swap(arr[i], arr[largest]);

		// Recursively heapify the affected sub-tree
		heapify(arr, n, largest);
	}
}

//Funcion heap sort
void heapSort(int arr[], int n)
{
	// Build heap (rearrange array)
	for (int i = n / 2 - 1; i >= 0; i--)
		heapify(arr, n, i);

	// One by one extract an element from heap
	for (int i = n - 1; i > 0; i--) {
		// Move current root to end
		swap(arr[0], arr[i]);
		// call max heapify on the reduced heap
		heapify(arr, i, 0);
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
		arr=new int[num];
		ifstream file("E:\\2021\\UNSA\\Semestre I\\Algoritmos\\Practica\\Trabajo en equipo\\C++\\data\\archivo" + to_string(num) + ".txt");

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

		heapSort(arr, num);

		auto t1 = high_resolution_clock::now();

		/* Getting number of milliseconds as an integer. */
		auto ms_int = duration_cast<milliseconds>(t1 - t0);

		/* Getting number of milliseconds as a double. */
		duration<double, std::milli> ms_double = t1 - t0;

		str1 = str1 + to_string(num) + "," + to_string(ms_double.count()) + "\n";
	}
	ofstream MyFile("E:\\2021\\UNSA\\Semestre I\\Algoritmos\\Practica\\Trabajo en equipo\\C++\\data\\heapSortCplus.txt");
	MyFile << str1 << endl;
	MyFile.close();
	return 0;
}
