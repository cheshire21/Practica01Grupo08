#include <stdio.h>
#include <iostream>
#include <chrono>
#include <fstream>
#include <string>
using namespace std;

using namespace std::chrono;
float t0, t1;

void insercion(int array[], int n) {
	int i, aux, k;
	for (i = 1; i < n; i++) {
		aux = array[i];
		k = i - 1;
		while (k >= 0 && aux < array[k]) {
			array[k + 1] = array[k];
			k = k - 1;
		}
		array[k + 1] = aux;
	}
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

		insercion(arr, num);

		auto t1 = high_resolution_clock::now();

		auto ms_int = duration_cast<milliseconds>(t1 - t0);

		duration<double, std::milli> ms_double = t1 - t0;

		str1 = str1 + to_string(num) + "," + to_string(ms_double.count()) + "\n";
	}
	ofstream MyFile("..\\..\\insertionSortCplus.txt");
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
	insercion(arr, 100);
	imprimir(arr, 100);
	return 0;*/
}
