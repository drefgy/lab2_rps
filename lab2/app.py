from flask import Flask, request, redirect, url_for, render_template, flash, jsonify
from db import Database
from sorting import shellSort
import json

app = Flask(__name__)  # Создаем экземпляр приложения Flask
app.secret_key = 'secretKey321'  # Устанавливаем секретный ключ для использования сессий и flash-сообщений

# Создаем экземпляр БД для пользовательских данных
db = Database()
# Создаем экземпляр БД для тестовых данных
dbTest = Database('testDatabase.db')


# Главная страница
@app.route('/')
def mainPage():
    arrays = db.getAllArrays()
    return render_template('mainPage.html', arrays=arrays)


# Страница добавления
@app.route('/add', methods=['GET', 'POST'])
def addArray():

    # Обрабатываем запрос POST
    if request.method == 'POST':
        arrayData = request.form['array']  # Получаем данные массива из формы

        # Сохраняем массив, обрабатываем ошибки
        try:
            numberArray = list(map(int, arrayData.split()))  # Преобразуем строку в список целых чисел
            db.addArray(numberArray)
            flash('Массив успешно добавлен!', 'success')

        except ValueError:
            flash('Ошибка, пожалуйста, введите целые числа, разделенные пробелами', 'error')

        return redirect(url_for('mainPage'))

    # Выполянем запрос GET
    return render_template('addArray.html')


# Редактирование
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def editArray(index):
    currentArray = db.getArrayById(index)  # Получаем текущий массив по его индексу

    # Проверяем, существует ли массив
    if not currentArray:
        flash('Массив не найден!', 'error')
        return redirect(url_for('mainPage'))

    # Обрабатываем POST-запрос
    if request.method == 'POST':

        # Удаление массива
        if 'delete' in request.form:
            db.deleteArray(index)
            flash('Массив успешно удален!', 'success')
            return redirect(url_for('mainPage'))

        # Сортировка массива
        if 'sort' in request.form:
            arrayData = request.form['array']  # Получаем введенные данные

            try:
                # Пробуем преобразовать строку в список целых чисел
                numberArray = list(map(int, arrayData.split()))
                sortedArray = shellSort(numberArray)  # Сортируем массив с помощью битонной сортировки
                db.updateArray(index, sortedArray)  # Обновляем данные
                flash('Массив успешно отсортирован!', 'success')
                return redirect(url_for('editArray', index=index))

            except ValueError:
                flash('Ошибка: убедитесь, что вы ввели только числа, разделенные пробелами.', 'error')
                # Возвращаем пользователя на страницу редактирования с введёнными данными
                return render_template('editArray.html', index=index, currentArray=arrayData)

        # Получаем новые данные массива из формы
        new_data = request.form['array']

        # Сохраняем массив, обрабатываем ошибки
        try:
            numberArray = list(map(int, new_data.split()))  # Преобразуем строку в список целых чисел
            db.updateArray(index, numberArray)
            flash('Массив успешно обновлен!', 'success')
        except ValueError:
            flash('Ошибка: убедитесь, что вы ввели только числа, разделенные пробелами.', 'error')

        return redirect(url_for('mainPage'))

    # Преобразуем массив в строку для отображения в форме
    arrayString = ' '.join(map(str, currentArray.arrayData))

    # GET запрос, текущий массив на шаблон редактирования отправляем
    return render_template('editArray.html', currentArray=arrayString)


# Добавление записей в тесте
@app.route('/test-add', methods=['POST'])
def testAddArray():

    arrayData = request.json  # Получаем данные массива из формы
    # Сохраняем массив, обрабатываем ошибки
    try:
        dbTest.addArray(arrayData)
        return jsonify({"status": "success"}), 201

    except ValueError:
        return jsonify({"status": "error"}), 400


# Удаление всех записей из тестовой БД
@app.route('/test-delete-all', methods=['POST'])
def testDeleteAll():
    arrays = dbTest.getAllArrays()

    for array in arrays:
        dbTest.deleteArray(array.id)

    return jsonify({"status": "success"}), 201


# Сортировка всех записей из тестовой БД
@app.route('/test-sort-all', methods=['POST'])
def testSortAll():
    arrays = dbTest.getAllArrays()

    for array in arrays:
        sortedArray = shellSort(array.arrayData)  # Сортируем массив с помощью сортировки Шелла
        dbTest.updateArray(array.id, sortedArray)  # Обновляем данные

    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(debug=True)

