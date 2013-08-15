# coding: utf-8
import json
import gevent

def websocket_send(ws):
    count = 0;
    while True:
        try:
            ws.send(json.dumps({'output': str(count)}))
        except:
            print "websocket must be closed..."
            break
        gevent.sleep(3)
        count = count + 1

        
#def websocket_receive(ws):
#    while True:

def thread_alive(thread2, ws):
    while True:
        print thread2, ws    
        gevent.sleep(5)


def handle_websocket(ws):
    thread2 = gevent.spawn(websocket_send, ws)
    thread3 = gevent.spawn(thread_alive, thread2, ws)
    while True:
        print "here i am"
        print "here i am2"
        message = ws.receive()
        if message is None:
            break

        message = json.loads(message)

        ws.send(json.dumps({'output': message['output']}))
