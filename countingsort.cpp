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


void countingSort(vector<int>& arr)
{
    int max = *max_element(arr.begin(), arr.end());
    int min = *min_element(arr.begin(), arr.end());
    int range = max - min + 1;
 
    vector<int> count(range), output(arr.size());
    for (int i = 0; i < arr.size(); i++)
        count[arr[i] - min]++;
 
    for (int i = 1; i < count.size(); i++)
        count[i] += count[i - 1];
 
    for (int i = arr.size() - 1; i >= 0; i--) {
        output[count[arr[i] - min] - 1] = arr[i];
        count[arr[i] - min]--;
    }
	
    for (int i = 0; i < arr.size(); i++)
        arr[i] = output[i];

	
}

string getCurrentDir() {
    char buff[MAX_PATH];
    GetModuleFileName( NULL, buff, MAX_PATH );
    string::size_type position = string( buff ).find_last_of( "\\/" );
    return string( buff ).substr( 0, position);
}
int main()
{
	int arr2[] = {100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000};
	int n = sizeof(arr2)/sizeof(arr2[0]);
	
	string str1 = "";

	for(int i = 0; i < n; i++){
		int num = arr2[i];
		// int num = arr2[0];
		vector<int> arr;
		ifstream file(getCurrentDir() + "\\data\\archivo"+to_string(num)+".txt");
		
		if(file.is_open())
		{
			for(int i = 0; i < num; ++i)
			{
				int valor = 0;

				file >> valor;

				arr.push_back(valor);
			}
			file.close();
		}
		cout << num << endl;

		auto t0= high_resolution_clock::now();

		countingSort(arr);
		
		auto t1= high_resolution_clock::now();
		
		auto ms_int = duration_cast<milliseconds>(t1 - t0);

		duration<double, std::milli> ms_double = t1 - t0;

		str1 = str1 +to_string(num) + " " + to_string(ms_double.count()) + "\n";
	}
	
	ofstream MyFile(getCurrentDir() + "\\ResCountingSortCPlusPlus.txt");
	MyFile << str1<< endl;
	MyFile.close();

	return 0;
}
