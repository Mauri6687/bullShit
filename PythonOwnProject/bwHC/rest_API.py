'''
Created on 07.01.2019

@author: IMMaurC1

'''

import rest_DB as rest_db

#import trunk.PythonOwnProject.bwHC.rest_DB as rest_db

#import bwHC.rest_DB as rest_db
import base64

from flask import Flask
from flask.globals import request



    
app = Flask(__name__)

# @app.route('/')
# def headerRead():
#     print(request.headers)
#     print(request.headers['User-Agent'])
#     print("##########Authorization#############")
#     print(request.headers['Authorization'])
#     return "well done header could read"


@app.route('/rest')
def rest():
    return "The rest API from the ZPM is alive"

@app.route('/patient/mpi=<string:mpi>', methods=['GET', 'POST'])
def patient(mpi):
    try:
        authorization = request.headers['Authorization']
        
    except Exception as e:
        e = "no valid authentification"
        return e
        
    if len(request.headers['Authorization']) >= 1:
        authorization = str(request.headers['Authorization'])
    else:
        authorization = " "
    
    
    #print(rest_db.check_authen(authorization))
    if rest_db.check_authen(str(authorization)) == 1:
        try:
            output = rest_db.getPatient(mpi)
        except Exception as e:
            e = "no valid mpi"
            return e    
        return  output
    else:        
        return "no valid authentification" 
     
# if __name__ == '__main__':
#     app.run(host='10.231.37.198', port=5455)