'''
Created on 11.12.2018

@author: IMMaurC1
'''

import mysql.connector

class db_connections(object):
    '''
    classdocs
    '''
    def HW(self):
        ret = print("Hello world")
        return ret
    
    def open_db(self):
        self.mydb = mysql.connector.connect(host="VSWZPM01",user="usercompare",passwd="compareTo")

        print(self.mydb)
    
        mycursor = self.mydb.cursor()

        mycursor.execute("SHOW DATABASES")

        for x in mycursor:
            print(x)

    def top10Pat(self):
        open = self.open_db()
        open.mydb
        mycursor = open.cursor()
        mycursor.execute("SELECT TOP 10 * FROM patient")  
    
    
        for y in mycursor:
            print(y)  

    
    
    def __init__(self, params):
        '''
        Constructor
        '''
        