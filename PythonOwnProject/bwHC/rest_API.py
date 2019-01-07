'''
Created on 07.01.2019

@author: IMMaurC1

'''


from flask import Flask

app = Flask(__name__)

@app.route('/rest')
def hello():
    return "Rest API is here"
    

if __name__ == '__main__':
   app.run(host='localhost', port=80)