'''
Created on 23.04.2019

@author: IMMaurC1
'''
import trunk.PythonOwnProject.bwHC.myconnutils as myconnutils
import pymysql.cursors  

# import bwHC.myconnutils
# import pymysql.cursors  
 
# Mit der Datenbank verbinden.

 
 
def getPatient(mpi):
    connection = myconnutils.getConnection()
    try:
        cursor = connection.cursor()        
           
        # SQL 
        sql = "select * from patient where patient_mpi = "+mpi+";"
         
        # Den AbfragenBefehl implementieren (Execute Query).
        cursor.execute(sql)
         
        #print ("cursor.description: ", cursor.description)
 
        #print()
         
        for x in cursor:
            output = x
                 
    finally:
        return str(output)
        # Die Verbindung schliessen (Close connection).      
        connection.close()
        
   
        
def check_authen(hashCode):
    connection = myconnutils.getConnection()
    #print("HashCode?????  --- > "+hashCode)
    try:
        cursor = connection.cursor()
        hashCode = hashCode[6:]
        sql = "select rest_hash from rest_permission where rest_hash = '"+hashCode+"';"
        
        #print(sql)
        
        cursor.execute(sql)
        
        output = cursor.fetchone()
    
    finally:
        #print("output-- >" + output['rest_hash']+"")
        
        if hashCode == output['rest_hash']:
            # Die Verbindung schliessen (Close connection).      
            connection.close()
            return int(1)
        
        else:
            # Die Verbindung schliessen (Close connection).      
            connection.close()
            return int(0)
        
    
def bwHC_data(searchValues):
    connection = myconnutils.getConnection()
    try:
        cursor = connection.cursor()        
           
        # SQL 
        sql = "select * from bwhc_data_set_consent where x = "+searchValues+";"
         
        # Den AbfragenBefehl implementieren (Execute Query).
        cursor.execute(sql)
         
        #print ("cursor.description: ", cursor.description)
 
        #print()
         
        for x in cursor:
            output = x
                 
    finally:
        #XML müsste man an dieser Stelle bauen....
        return str(output)
        # Die Verbindung schliessen (Close connection).      
        connection.close()
