import sqlite3  # Импортируем библиотеку для работы с SQLite
import json  # Импортируем библиотеку для работы с JSON

class Array:
    def __init__(self, id, arrayData):
        # Инициализация
        self.id = id  # Уникальный идентификатор массива
        self.arrayData = arrayData  # Данные массива


class Database:
    # Инициализация объекта и установка имени базы данны
    def __init__(self, dbТame='storingArrays.db'):
        self.database = dbТame
        self.init_db()

    # Метод для получения соединения с базой данных
    def get_connection(self):
        conn = sqlite3.connect(self.database)  # Устанавливаем соединение с базой данных
        conn.row_factory = sqlite3.Row  # Устанавливаем фабрику строк для получения данных в виде словаря, чтобы обращаться по именам столбцов

        return conn  # Возвращаем соединение

    # Метод, который выполняет конкретную задачу по созданию таблицы в базе данных.
    def init_db(self):
        conn = self.get_connection()  # Получаем соединение

        # Создаем таблицу, если она не существует
        conn.execute('''
            CREATE TABLE IF NOT EXISTS arrays (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                arrayData TEXT NOT NULL  
            )
        ''')
        conn.commit()
        conn.close()

    # Метод для добавления нового массива в базу данных
    def addArray(self, arrayData):
        json_data = json.dumps(arrayData)  # Сохраняем массив как JSON
        conn = self.get_connection()  # Получаем соединение

        # Вставляем данные в таблицу
        conn.execute('INSERT INTO arrays (arrayData) VALUES (?)', (json_data,))

        conn.commit()
        conn.close()

    # Метод для получения всех массивов из базы данных
    def getAllArrays(self):
        conn = self.get_connection()

        arrays = conn.execute('SELECT * FROM arrays').fetchall()  # Получаем все массивы
        conn.close()

        # Создаем объекты Array из полученных данных и возвращаем их
        return [Array(array['id'], json.loads(array['arrayData'])) for array in arrays]

    # Метод для получения массива по его идентификатору
    def getArrayById(self, array_id):
        conn = self.get_connection()
        array = conn.execute('SELECT * FROM arrays WHERE id = ?', (array_id,)).fetchone()  # Получаем массив по ID
        conn.close()

        # Возвращаем объект Array, если массив найден, иначе возвращаем None
        return Array(array['id'], json.loads(array['arrayData'])) if array else None

    # Метод для обновления массива по его идентификатору
    def updateArray(self, array_id, arrayData):
        json_data = json.dumps(arrayData)  # Сохраняем массив как JSON
        conn = self.get_connection()

        # Обновляем данные в таблице по ID
        conn.execute('UPDATE arrays SET arrayData = ? WHERE id = ?', (json_data, array_id))
        conn.commit()
        conn.close()

    # Метод для удаления массива по его идентификатору
    def deleteArray(self, array_id):
        conn = self.get_connection()

        # Удаляем массив из таблицы по ID
        conn.execute('DELETE FROM arrays WHERE id = ?', (array_id,))
        conn.commit()
        conn.close()

