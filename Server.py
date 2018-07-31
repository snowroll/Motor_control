# -*- coding: utf-8 -*-
# author chaihj
# date 2018/07/30

import socket, sys, threading
from PIL.ImageQt import ImageQt
from PIL import Image
import numpy as np
import pickle

HOST = '127.0.0.1'
port = 8888

class server(object):
    def __init__(self):  #build connect with client
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind((HOST, port))
        self.s.listen(5)
        self.conn, addr = self.s.accept()  #In fact, only one client
        # self.conn.setblocking(0)  #not blocking
        self.conn.settimeout(0.001)

    def rece_data(self):
        pos, ori = [0, 0, 0], [0, 0, 0]
        try:
            data = self.conn.recv(1024)  #pos and ori  
            if len(data) != 0:
                data_str = data.decode('utf-8')
                data_list = data_str.split(' ')
                for i in range(3):
                    pos[i] = eval(data_list[i])
                    ori[i] = eval(data_list[3+i])
                print('pos', pos, 'ori', ori)
                del data, data_str, data_list
        except socket.timeout:
            pass
        return pos, ori
    
    def send_data(self, img):  #img is np array
        tran_data = pickle.dumps(img)  #laser detect map
        print('length data', len(tran_data))
        self.conn.sendall(tran_data)
        del tran_data

    def product(self):
        pos, ori = self.rece_data()
        return pos, ori





        