'''
Created on 11.12.2018

@author: IMMaurC1
'''

import mysql.connector
from sqlite3.test.factory import MyCursor

class db_connections(object):
    '''
    classdocs
    '''
    mydb = mysql.connector.connect(host="vswcxxesbit01",user="usercompare",passwd="compareTo", database = "mtbv8")
    
    def HW(self):
        ret = print("Hello world")
        return ret
    
    def open_db():
        mydb = mysql.connector.connect(host="vswcxxesbit01",user="usercompare",passwd="compareTo", database = "mtbv8")
        db_conn = mydb
           
        mycursor = db_conn.cursor()

        mycursor.execute("SELECT * FROM patient ")
   
        for x in mycursor:
            print(x)
            
    def getPatient(mpi):
        
        open = db_connections.mydb
        mycursor = open.cursor()
        mycursor.execute("SELECT * FROM patient where patient_mpi = "+ mpi+"")
        
        for x in mycursor:
            output = x
                       
        return str(output)
        
        
    def top10Pat(self):
        open = self.open_db()
        
        mycursor = open.cursor()
        mycursor.execute("SELECT TOP 10 * FROM patient")  
     
     
        for y in mycursor:
            print(y)  
# 
#     def user(self):
#         open = self.open_db()
#         open.mydb
#         mycursor = open.cursor()
#         mycursor.execute("select * from user where username = ")
    
    def __init__(self, params):
        '''
        Constructor
        '''
        