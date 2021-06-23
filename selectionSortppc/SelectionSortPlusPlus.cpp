// heapSortV2.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
//

// heapSort.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
//

#include <stdio.h>
#include <iostream>
#include <chrono>
#include <fstream>
#include <string>
#include <windows.h>
#include <limits.h>
#include <tchar.h>
using namespace std;
using namespace std::chrono;

float t0, t1;

void swap(long int* a, long int* b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void selectionSort( int arr[],  int n)
{
	long int i, j, midx;

	for (i = 0; i < n - 1; i++) {

		// Find the minimum element in unsorted array
		midx = i;

		for (j = i + 1; j < n; j++)
			if (arr[j] < arr[midx])
				midx = j;

		// Swap the found minimum element
		// with the first element
		swap(arr[midx], arr[i]);
	}
	
}

string getCurrentDir() {
    char buff[MAX_PATH];
    GetModuleFileName( NULL, buff, MAX_PATH );
    string::size_type position = string( buff ).find_last_of( "\\/" );
    return string( buff ).substr( 0, position);
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
		//ifstream file("E:\\2021\\UNSA\\Semestre I\\Algoritmos\\Practica\\Trabajo en equipo\\Practica01Grupo08\\Luis\\data\\archivo" + to_string(num) + ".txt");
		ifstream file(getCurrentDir() +"\\data\\archivo" + to_string(num) + ".txt");
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

		selectionSort(arr, num);

		auto t1 = high_resolution_clock::now();

		/* Getting number of milliseconds as an integer. */
		auto ms_int = duration_cast<milliseconds>(t1 - t0);

		/* Getting number of milliseconds as a double. */
		duration<double, std::milli> ms_double = t1 - t0;

		str1 = str1 + to_string(num) + "," + to_string(ms_double.count()) + "\n";
	}
	ofstream MyFile(getCurrentDir() +"\\SelectionSortC.txt");
	MyFile << str1 << endl;
	MyFile.close();
	return 0;
}

