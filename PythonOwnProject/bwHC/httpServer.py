'''
Created on 13.12.2018

@author: IMMaurC1
'''
import http.server
import socketserver
from bwHC import rest_API
rest_API

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    
    
