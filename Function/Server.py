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

    def rece_data(self):
        data = self.conn.recv(1024)  #pos and ori  eg: 1 1 1 1 1 1
        data_str = data.decode('utf-8')
        data_list = data_str.split(' ')
        data_array = np.array(data_list, dtype='float')
        return data_array
    
    def send_data(self, img):  #img is np array
        tran_data = pickle.dumps(img)  #laser detect map
        self.conn.sendall(tran_data)





        