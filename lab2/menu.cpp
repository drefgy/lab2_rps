#include <stdio.h>
#include <iostream>
#include <locale>
#include <vector>
#include "inputValidation.hpp"
#include "functions.hpp"

using namespace std;

enum mainMenu { keyboardInput = 1, randomInput, savingArray, quit };
vector<int> arrayValues;

void greeting() {
    cout << "\t Лабораторная работа №2, вариант №7" << endl;
    cout << "\t Выполнили Инякина Мария, Кондрашина Мария" << endl;
    cout << "\t группа 434" << endl;
    cout << endl << "Сортировка Шелла" << endl;
}

void showMenu() {
    int choice = 0;

    do {
        cout << endl << "\t Меню:" << endl;
        cout << "1 - Ввод данных с клавиатуры" << endl;
        cout << "2 - Заполнение случайными значениями" << endl;
        cout << "3 - Сохранить данные в файл" << endl;
        cout << "4 - Завершение программы" << endl;
        
        cout << endl << "Выберите пункт меню: ";
        
        choice = inputInt();

        switch (choice) {

        case keyboardInput:
            inputArray(arrayValues);
            shellSort(arrayValues);
            printArray(arrayValues);
            break;

        case randomInput:
            randomArray(arrayValues);
            shellSort(arrayValues);
            printArray(arrayValues);
            break;
                
        case savingArray:
            if (!arrayValues.empty()) {
                string filePath;
                cout << "Введите путь к файлу для сохранения массива: ";
                getline(cin, filePath);
                saveArrayToFile(arrayValues, filePath);
            }
            else {
                cout << "Массив пуст. Сначала создайте массив." << endl;
                }
                break;
        case quit:
            cout << "Завешение работы программы" << endl;
            break;

        default:
            cout << "Пункт меню не найден, пожалуйста, введите корректное значение:" << endl;
        }

    } while (choice != quit);
    
}

