'''
Created on 23.04.2019

@author: IMMaurC1
'''
import pymysql.cursors  
 
# Die Funktion gibt eine Verbindung zurück.
def getConnection():
    connection = pymysql.connect(host='vswcxxesbit01',user='usercompare',password='compareTo',db='mtbv8',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    return connection