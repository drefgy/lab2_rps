#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <sstream>
#include "inputValidation.hpp"

using namespace std;
using namespace filesystem;

void shellSort(vector<int>& array) {
    unsigned long length = array.size();
    // Начинаем с большого шага и уменьшаем его
    for (unsigned long gap = length / 2; gap > 0; gap /= 2) {
        // Выполняем сортировку вставками для данного шага
        for (unsigned long i = gap; i < length; i++) {
            int temp = array[i];
            unsigned long j;
            // Сдвигаем элементы arr[0..i-gap], которые больше temp,
            // на одну позицию вперед от их текущей позиции
            for (j = i; j >= gap && array[j - gap] > temp; j -= gap) {
                array[j] = array[j - gap];
            }
            array[j] = temp;
        }
    }
}

void inputArray(vector<int>& array) {
    int size;
    cout << "Введите количество элементов массива: ";
    size = inputInt();
    if (size <= 0) {
        cout << "Размер массива должен быть положительным числом. Пожалуйста, повторите ввод: ";
        size = inputInt();
    }
    if (size > maxSize) {
        cout << "Размер массива не должен превышать " << maxSize <<". Пожалуйста, повторите ввод: ";
        size = inputInt();
    }
    array.resize(size);
    cout << "Введите элементы массива:" << endl;
    for (int i = 0; i < size; ++i) {
        array[i] = inputInt();
    }
}

void printArray(vector<int>& array) {
    cout << "Отсортированный массив: ";
    unsigned long size = array.size();
    for (int i = 0; i < size; ++i) {
        cout << array[i] << " ";
    }
    cout << endl;
}

void randomArray(vector<int>& array) {
    srand(static_cast<unsigned int>(time(0))); // Инициализация генератора случайных чисел
    unsigned long size;
    cout << "Введите количество элементов массива: ";
    size = inputUnsignedLong();
    if (size <= 0) {
        cout << "Размер массива должен быть положительным числом. Пожалуйста, повторите ввод: ";
        size = inputUnsignedLong();
    }
    if (size > maxSize) {
        cout << "Размер массива не должен превышать " << maxSize <<". Пожалуйста, повторите ввод: ";
        size = inputInt();
    }
    array.resize(size);
    for (int i = 0; i < size; ++i) {
        array[i] = lowerBound + rand() % (upperBound - lowerBound + 1);
    }
    cout << "Вектор, заполненный случайными значениями: ";
    for (int i = 0; i < size; ++i) {
        cout << array[i] << " ";
    }
    cout << endl;
}

void saveArrayToFile(const vector<int>& array, const string& filePath) {
    ofstream outputFile(filePath);
    if (outputFile.is_open()) {
        for (const int& value : array) {
            outputFile << value << " ";
        }
        outputFile.close();
        cout << "Массив успешно сохранен в файл: " << filePath << endl;
    } else {
        cout << "Ошибка при открытии файла: " << filePath << endl;
    }
}
