import sqlite3
from os.path import isfile

# SELECT name FROM PRAGMA_TABLE_INFO('talbe_name') << Get table colls

class createDB(object):
    def __init__(self, name):
        self.name = name
        self.connectDB()

    def connectDB(self):
        if isfile(self.name):
           self.conn = sqlite3.connect(self.name)
           self.c = self.conn.cursor()
        else:
           self.conn = sqlite3.connect(self.name)
           self.c = self.conn.cursor()
           self.c.executescript(open('buildDB.sql', 'r').read())
           self.c.executescript(open('fillDBTestData.sql', 'r').read())
           self.conn.commit()
    
    def executeQuery(self, query):
        return self.c.execute(query).fetchall()
    
    def getTableRows(self, fromUnit):
        return self.executeQuery(f'select name from pragma_table_info(\'{fromUnit}\')')
    
    def getAllDetails(self, fromUnit):
        return self.executeQuery(f'select * from {fromUnit}')
    
    def findByName(self, fromUnit, name):
        return self.executeQuery(f'select * from {fromUnit} where Name = \'{name}\'')