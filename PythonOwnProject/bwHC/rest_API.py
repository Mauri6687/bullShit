'''
Created on 07.01.2019

@author: IMMaurC1

'''
import bwHC.db_connections as db

from flask import Flask
from flask.globals import request


app = Flask(__name__)

@app.route('/rest')
def rest():
    return "Rest API is here"


@app.route('/zpm')
def zpm():
    return "ZPM is here"

@app.route('/user/<string:username>', methods=['GET'])
def user(username):
    return "ZPM is here and you are "+username

@app.route('/patient/mpi=<string:mpi>', methods=['GET'])
def patient(mpi):
    output = db.db_connections.getPatient((str(mpi)))        
    return str(output)


if __name__ == '__main__':
    app.run(host='10.231.37.198', port=80)