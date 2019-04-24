'''
Created on 15.04.2019

@author: IMMaurC1
'''


import bwHC.rest_API as rest_api
import bwHC.rest_DB as rest_db


from basicauth import encode
from basicauth import decode



def basicAuth(username, password, hash):
    #GET USER, PASSWORD
    print("################ Uebergabe von Benutzername und Passwort ###############")
    #username, password = "MTB_Admin", "MTB_Admin"
    encode_str = encode(username, password)
    print(encode_str)
    print("################ Uebergabe von Benutzername und Passwort ###############")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("################ Uebergabe von Hash ###############")
    #GET HASH
    username, password = decode(encode_str)
    print(username, password)
    print("################ Uebergabe von Hash ###############")
    #den jeweiligen wert pruefen!!!!
    
    


def main():
    rest_api.app.run(host='10.231.37.198', port=5455)
    
    #rest_db.getPatient('5860837')
    #rest_db.check_authen('TVRCX0FkbWluOk1UQl9BZG1pbg==')
    
   


if __name__ == '__main__':
    main()