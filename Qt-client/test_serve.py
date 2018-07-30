# -*- coding: utf-8 -*-
import socket, sys
import threading
from PIL.ImageQt import ImageQt
from PIL import Image
import numpy as np
import pickle

first = True
second = True

def send_info(conn):
    global first, second
    while True:
        try:
            if first:
                myfile = Image.open('src/up.png')
                myfile.show()
                img = np.array(myfile)
                tran_data = pickle.dumps(img)
                conn.sendall(tran_data)
                print('first send')
                first = False
            elif second:
                myfile = Image.open('src/left.png')
                myfile.show()
                img = np.array(myfile)
                tran_data = pickle.dumps(img)
                conn.sendall(tran_data)
                print('second send')
                second = False
            else:
                # sock.sendall(tran_data)
                sth = input('say something:\n')
                conn.sendall(sth)
        except ConnectionError:
            print('connect error')
            sys.exit(-1)
        except:
            print('unexpect error')
            sys.exit(-1)

class rece_info(threading.Thread):
    def __init__(self, connect):
        threading.Thread.__init__(self)
        self.connect = connect
        self.daemon = True
        self.start()

    def run(self):
        while True:
            try:
                data = self.connect.recv(1024)
                data2 = data.decode('utf-8')
                print('get message:'+data2)
            except ConnectionError:
                print('connect error')
                sys.exit(-1)
            except:
                print('unexpect error')
                sys.exit(-1)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
port = 8888
s.bind((HOST, port))
print('bind ok', port)
s.listen(5)
conn, addr = s.accept()
c1 = rece_info(conn)
send_info(conn)


