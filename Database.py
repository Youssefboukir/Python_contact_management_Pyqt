import sqlite3

def createTable():
    connection = sqlite3.connect('login.db')

    connection.execute("CREATE TABLE Message( iduser TEXT,Name TEXT,emailcontact TEXT ,message TEXT)")
    connection.commit()
    
 
    connection.close()

createTable()
        
    
