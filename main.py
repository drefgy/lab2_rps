import requests
import random
import time
import unittest

BASE_URL = "http://127.0.0.1:5000"

def generateRandomArray():
    size = random.randint(1, 100)  # Генерируем случайный размер массива
    return [random.randint(1, 1000) for _ in range(size)]  # Генерируем случайные числа

def addArrays(self, numArrays):
    startTime = time.time()
    successCounter = 0
    failureCounter = 0

    for _ in range(numArrays):
        arrayData = generateRandomArray()
        response = requests.post(BASE_URL + '/test-add', json=arrayData)
        if response.status_code == 201:
            successCounter += 1
        else:
            failureCounter += 1

    endTime = time.time()
    AllTime = endTime - startTime

    print(f"Успешно добавлено массивов: {successCounter}")
    print(f"Неудачных попыток: {failureCounter}")
    print(f"Время выполнения: {AllTime:.2f} секунд")

    # Проверка успешного выполнения
    self.assertEqual(failureCounter, 0, "Не все массивы были успешно добавлены.")

def sortArrays(numArrays):
    startTime = time.time()
    response = requests.post(BASE_URL + '/test-sort-all')
    endTime = time.time()
    AllTime = endTime - startTime
    if response.status_code == 201:
        print(f"Добавленные массивы успешно отсортированы за {AllTime:.2f} секунд")
        print(f"Среднее время: {AllTime/numArrays:.2f} секунд")
    else:
        print(f"Добавленные массивы не удалось отсортирвоать за {AllTime:.2f} секунд")

def deleteArrays():
    startTime = time.time()
    response = requests.post(BASE_URL + '/test-delete-all')
    endTime = time.time()
    AllTime = endTime - startTime
    if response.status_code == 201:
        print(f"Тестовая БД успешно очищена от тестовых данных за {AllTime:.2f} секунд")
    else:
        print(f"Не удалось очистить тестовую БД за {AllTime:.2f} секунд")

class Test100(unittest.TestCase):
    def test1Add(self):
        addArrays(self, 100)

    def test2Sort(self):
        sortArrays(100)

    def test3Delete(self):
        deleteArrays()


class Test1000(unittest.TestCase):
    def test1Add(self):
        addArrays(self, 1000)

    def test2Sort(self):
        sortArrays(1000)

    def test3Delete(self):
        deleteArrays()


class Test10000(unittest.TestCase):
    def test1Add(self):
        addArrays(self, 10000)

    def test2Sort(self):
        sortArrays(10000)

    def test3Delete(self):
        deleteArrays()

if __name__ == "__main__":
    unittest.main()