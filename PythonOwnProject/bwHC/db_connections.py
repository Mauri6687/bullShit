'''
Created on 11.12.2018

@author: IMMaurC1
'''

import mysql.connector

class db_connections(object):
    '''
    classdocs
    '''
    print("Hello world")


    mydb = mysql.connector.connect(
        host="VSWCENTRAXX02",
        user="sa_zpm_read_all",
        passwd="pI1UL6x&"
        )

    print(mydb)
    
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
      print(x)
      
    mycursor.execute("SELECT TOP 10 * FROM current_patient_data")  
    
    '''print(mycursor[65])'''
    
    
    for y in mycursor:
      print(y)  

    
    
    def __init__(self, params):
        '''
        Constructor
        '''
        