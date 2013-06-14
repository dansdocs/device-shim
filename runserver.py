#!/usr/bin/env python
# coding: utf-8
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import website

def the_site(environ, start_response):  
    path = environ["PATH_INFO"]   
    if path == "/websocket":  
        return website.websocket.handle_websocket(environ["wsgi.websocket"])   
    else:
        return website.flask_pages(environ, start_response) 


if __name__ == '__main__':
    http_server = WSGIServer(('',8000), the_site, handler_class=WebSocketHandler)
    http_server.serve_forever()
