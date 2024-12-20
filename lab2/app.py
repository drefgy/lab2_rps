from flask import Flask, request, redirect, url_for, render_template, flash, jsonify
from db import Database
from sorting import shellSort
import json

app = Flask(__name__)  
app.secret_key = 'secretKey321'  


db = Database()

dbTest = Database('testDatabase.db')



@app.route('/')
def mainPage():
    arrays = db.getAllArrays()
    return render_template('mainPage.html', arrays=arrays)



@app.route('/add', methods=['GET', 'POST'])
def addArray():


    if request.method == 'POST':
        arrayData = request.form['array']  


        try:
            numberArray = list(map(int, arrayData.split()))  
            db.addArray(numberArray)
            flash('Массив успешно добавлен!', 'success')

        except ValueError:
            flash('Ошибка, пожалуйста, введите целые числа, разделенные пробелами', 'error')

        return redirect(url_for('mainPage'))

    
    return render_template('addArray.html')



@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def editArray(index):
    currentArray = db.getArrayById(index)  

    
    if not currentArray:
        flash('Массив не найден!', 'error')
        return redirect(url_for('mainPage'))

    
    if request.method == 'POST':

        
        if 'delete' in request.form:
            db.deleteArray(index)
            flash('Массив успешно удален!', 'success')
            return redirect(url_for('mainPage'))

        
        if 'sort' in request.form:
            arrayData = request.form['array']  

            try:
                
                numberArray = list(map(int, arrayData.split()))
                sortedArray = shellSort(numberArray)  
                db.updateArray(index, sortedArray)  
                flash('Массив успешно отсортирован!', 'success')
                return redirect(url_for('editArray', index=index))

            except ValueError:
                flash('Ошибка: убедитесь, что вы ввели только числа, разделенные пробелами.', 'error')
                
                return render_template('editArray.html', index=index, currentArray=arrayData)

        
        new_data = request.form['array']

       
        try:
            numberArray = list(map(int, new_data.split()))  
            db.updateArray(index, numberArray)
            flash('Массив успешно обновлен!', 'success')
        except ValueError:
            flash('Ошибка: убедитесь, что вы ввели только числа, разделенные пробелами.', 'error')

        return redirect(url_for('mainPage'))

    
    arrayString = ' '.join(map(str, currentArray.arrayData))

    
    return render_template('editArray.html', currentArray=arrayString)



@app.route('/test-add', methods=['POST'])
def testAddArray():

    arrayData = request.json  
    
    try:
        dbTest.addArray(arrayData)
        return jsonify({"status": "success"}), 201

    except ValueError:
        return jsonify({"status": "error"}), 400



@app.route('/test-delete-all', methods=['POST'])
def testDeleteAll():
    arrays = dbTest.getAllArrays()

    for array in arrays:
        dbTest.deleteArray(array.id)

    return jsonify({"status": "success"}), 201



@app.route('/test-sort-all', methods=['POST'])
def testSortAll():
    arrays = dbTest.getAllArrays()

    for array in arrays:
        sortedArray = shellSort(array.arrayData) 
        dbTest.updateArray(array.id, sortedArray)  

    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(debug=True)
