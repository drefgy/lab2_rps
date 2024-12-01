#pragma once
#include <vector>

using namespace std;

void shellSort(vector<int>& array); // Сортировка Шелла
void inputArray(vector<int>& array); // Заполнение массива с клавиатуры
void printArray(vector<int>& array); // Вывод массива
void randomArray(vector<int>& array); // Заполнение массива случайными значениями
void saveArrayToFile(const vector<int>& array, const string& filePath); // Сохранение массива в файл
