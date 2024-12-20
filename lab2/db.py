import sqlite3 
import json  

class Array:
    def __init__(self, id, arrayData):
       
        self.id = id  
        self.arrayData = arrayData  


class Database:
    
    def __init__(self, dbТame='storingArrays.db'):
        self.database = dbТame
        self.init_db()

    
    def get_connection(self):
        conn = sqlite3.connect(self.database)  
        conn.row_factory = sqlite3.Row  

        return conn  

    
    def init_db(self):
        conn = self.get_connection()  

        
        conn.execute('''
            CREATE TABLE IF NOT EXISTS arrays (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                arrayData TEXT NOT NULL  
            )
        ''')
        conn.commit()
        conn.close()

    
    def addArray(self, arrayData):
        json_data = json.dumps(arrayData)  
        conn = self.get_connection()  


        conn.execute('INSERT INTO arrays (arrayData) VALUES (?)', (json_data,))

        conn.commit()
        conn.close()


    def getAllArrays(self):
        conn = self.get_connection()

        arrays = conn.execute('SELECT * FROM arrays').fetchall()  
        conn.close()

   
        return [Array(array['id'], json.loads(array['arrayData'])) for array in arrays]


    def getArrayById(self, array_id):
        conn = self.get_connection()
        array = conn.execute('SELECT * FROM arrays WHERE id = ?', (array_id,)).fetchone()  
        conn.close()


        return Array(array['id'], json.loads(array['arrayData'])) if array else None


    def updateArray(self, array_id, arrayData):
        json_data = json.dumps(arrayData)  
        conn = self.get_connection()

        
        conn.execute('UPDATE arrays SET arrayData = ? WHERE id = ?', (json_data, array_id))
        conn.commit()
        conn.close()

    
    def deleteArray(self, array_id):
        conn = self.get_connection()

        
        conn.execute('DELETE FROM arrays WHERE id = ?', (array_id,))
        conn.commit()
        conn.close()
