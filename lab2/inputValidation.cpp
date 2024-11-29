#include <iostream>
#include <sstream>
#include <limits>
#include <cctype>
using namespace std;

template<typename T>
T getInput() {
    string input;
    T value;
    while (true) {
        getline(cin, input); // Считываем ввод как строку
        stringstream ss(input);
        if (ss >> value) { // Пытаемся преобразовать строку в нужный тип
            if (ss.eof()) { // Проверяем, что больше нет данных в строке
                break; // Корректный ввод, выходим из цикла
            }
        }
        // Если ввод некорректный, вывод сообщения об ошибке
        cout << "Ошибка, пожалуйста, введите корректное значение: ";
    }
    return value;
}

int inputInt() {
   return getInput<int>();
}

unsigned long inputUnsignedLong() {
   return getInput<unsigned long>();
}

double inputDouble() {
   return getInput<double>();
}

bool inputBool() {
   return getInput<bool>();
}

