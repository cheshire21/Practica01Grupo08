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
#include <math.h> 
using namespace std;
using namespace std::chrono;

float t0, t1;
void inserta_en_monticulo(int arr[], int n)
{
	int k, aux;
	bool band;
	for (int i = 1; i <= n; i++) {
		k = i;
		band = true;
		while ((k > 0) && (band == true)) {
			band = false;
			if (arr[k] > arr[(k - 1) / 2]) {
				aux = arr[(k - 1) / 2];
				arr[(k - 1) / 2] = arr[k];
				arr[k] = aux;
				k = (k - 1) / 2;
				band = true;
			}			
		}
	}
}

void elimina_monticulo(int arr[], int n)
{
	int aux, izq, der, k, ap;
	bool band;
	for (int i = n-1; i >= 1; i--) {
		aux = arr[i];
		arr[i] = arr[0];
		izq = 1;
		der = 2;
		k = 0;
		band = true;
		int mayor;
		while ((izq < i) && (band == true)) {
			mayor = arr[izq];
			ap = izq;
			if ((mayor < arr[der]) && (der != i)) {
				mayor = arr[der];
				ap = der;
			}
			if (aux < mayor) {
				arr[k] = arr[ap];
				k = ap;
			}
			else {
				band = false;
			}
			izq = k * 2+1;
			der = k * 2 + 2;
		}
		arr[k] = aux;
	}
}
//Funcion heap sort
void heapSort(int arr[], int n) {
	inserta_en_monticulo(arr, n);
	elimina_monticulo(arr, n);
}
void imprimir(int arr[], int n) {
	for (int i = 0; i < n; i++) {
		cout << arr[i] << endl;
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
		//ifstream file("E:\\2021\\UNSA\\Semestre I\\Algoritmos\\Practica\\Trabajo en equipo\\C++\\data\archivo" + to_string(num) + ".txt");
		ifstream file("..\\..\\data\\archivo" + to_string(num) + ".txt");
		if (file.is_open())
		{
			for (int i = 1; i <= num; ++i)
			{
				file >> arr[i];
			}
			file.close();
		}
		cout << num << endl;

		auto t0 = high_resolution_clock::now();

		heapSort(arr, num);

		auto t1 = high_resolution_clock::now();

		auto ms_int = duration_cast<milliseconds>(t1 - t0);

		duration<double, std::milli> ms_double = t1 - t0;

		str1 = str1 + to_string(num) + "," + to_string(ms_double.count()) + "\n";
	}
	ofstream MyFile("..\\..\\HeapSortCplus.txt");
	MyFile << str1 << endl;
	MyFile.close();
	return 0;
	/*Activar solo con fines de probar el funcionamiento del métod Heapsort*/
	/*int* arr = nullptr;
	arr = new int[100];
	ifstream file("..\\..\\data\\archivo" + to_string(100) + ".txt");
	if (file.is_open())
	{
		for (int i = 0; i < 100; i++)
		{
			file >> arr[i];
		}
		file.close();
	}
	heapSort(arr, 100);
	imprimir(arr, 100);
	return 0;*/
}

