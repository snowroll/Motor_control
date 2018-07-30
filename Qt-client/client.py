#author chaihj
#date 2018/07/28

# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PIL import Image
from PIL.ImageQt import ImageQt
import numpy as np
import SRC
from UAV import Ui_UAV
import cv2, pickle
import socket
import threading, time

import sys  #for import upper level module
sys.path.insert(0, '..')
from Function.Slam import Slam

slam = Slam()


HOST = '127.0.0.1'

class Controller(QMainWindow, Ui_UAV):
    def __init__(self, *args, **kwargs):
        super(Controller, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Controller')
        self.setWindowIcon(QIcon('src/logo.jpeg'))
        self.client = socket.socket()
        self.step = 0.4  

        #direct control
        self.front.mousePressEvent = self.Front_change
        self.front.mouseReleaseEvent = self.Front
        self.back.mousePressEvent = self.Back_change
        self.back.mouseReleaseEvent = self.Back
        self.left.mousePressEvent = self.Left_change
        self.left.mouseReleaseEvent = self.Left
        self.right.mousePressEvent = self.Right_change
        self.right.mouseReleaseEvent = self.Right
        self.up.mousePressEvent = self.Up_change
        self.up.mouseReleaseEvent = self.Up
        self.down.mousePressEvent = self.Down_change
        self.down.mouseReleaseEvent = self.Down
        
        self.send.clicked.connect(self.Get_info_Send)

        #client part
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip = "127.0.0.1"
        self.connect()
        self.s.settimeout(0.001)  #for no blocking commuticate
        self.timer = QTimer()
        self.timer.timeout.connect(self.receive)
        self.timer.start(5)

        #some unimport function
        self.slam_img.setScaledContents(True)

        self.show()

    def Front_change(self, event):
        self.front.setStyleSheet("border-image: url(:/src/front_click.png);")

    def Back_change(self, event):
        self.back.setStyleSheet("border-image: url(:/src/back_click.png);")

    def Left_change(self, event):
        self.left.setStyleSheet("border-image: url(:/src/left_click.png);")

    def Right_change(self, event):
        self.right.setStyleSheet("border-image: url(:/src/right_click.png);")

    def Up_change(self, event):
        self.up.setStyleSheet("border-image: url(:/src/up_click.png);")

    def Down_change(self, event):
        self.down.setStyleSheet("border-image: url(:/src/down_click.png);")

    def Front(self, event):
        pos, ori = [self.step, 0, 0], [0, 0, 0]
        self.Send(pos, ori)
        self.front.setStyleSheet("border-image: url(:/src/front.png);")
    
    def Back(self, event):
        pos, ori = [-self.step, 0, 0], [0, 0, 0]
        self.Send(pos, ori)
        self.back.setStyleSheet("border-image: url(:/src/back.png);")
    
    def Up(self, event):
        pos, ori = [0, 0, self.step], [0, 0, 0]
        self.Send(pos, ori)
        self.up.setStyleSheet("border-image: url(:/src/up.png);")

    def Down(self, event):
        pos, ori = [0, 0, -self.step], [0, 0, 0]
        self.Send(pos, ori)
        self.down.setStyleSheet("border-image: url(:/src/down.png);")

    def Left(self, event):
        pos, ori = [0, -self.step, 0], [0, 0, 0]
        self.Send(pos, ori)
        self.left.setStyleSheet("border-image: url(:/src/left.png);")

    def Right(self, event):
        pos, ori = [0, self.step, 0], [0, 0, 0]
        self.Send(pos, ori)
        self.right.setStyleSheet("border-image: url(:/src/right.png);")

    def Send(self, pos, ori):
        str_pos = ' '.join(map(str, pos))
        str_ori = ' '.join(map(str, ori))
        data = str_pos + ' ' + str_ori
        self.s.sendall(data.encode('utf-8'))
        print('data is ', data)
        

    def Quit(self):
        info = 'exit'
        self.s.sendall(info.encode('utf-8'))
        QCoreApplication.instance().quit

    def Get_info_Send(self):
        _pos, _ori = [0, 0, 0], [0, 0, 0]
        pos = self.pos_input.text()
        ori = self.ori_input.text()
        if pos == '' and ori == '':
            QMessageBox.about(self, 'warnning', 'pos and ori are set to 0')
        elif pos == '':
            QMessageBox.about(self, 'warnning', 'pos is set to 0')
            tmp_ori = ori.split(' ')
            for i in range(3):
                _ori[i] = float(tmp_ori[i])
        elif ori == '':
            QMessageBox.about(self, 'warnning', 'ori is set to 0')
            tmp_pos = pos.split(' ')
            for i in range(3):
                _pos[i] = float(tmp_pos[i])
        else:
            tmp_pos = pos.split(' ')
            tmp_ori = ori.split(' ')
            for i in range(3):
                _pos[i], _ori[i] = float(tmp_pos[i]), float(tmp_ori[i])
        self.pos_input.clear()
        self.ori_input.clear()
        self.Send(_pos, _ori)

    #tcp function
    def connect(self):
        try:
            self.s.connect((self.ip,8888))
            print("connect success")
            print('connect time: '+ time.ctime())
        except ConnectionError:
            print('connect error')
            sys.exit(-1)
        except:
            print('unexpect error')
            sys.exit(-1)
 
    def receive(self):
        try:
            data = self.s.recv(40960000)
            if len(data) != 0:
                print('receve data')
                img = pickle.loads(data, encoding='bytes')
                im = Image.fromarray(img)
                im = np.array(im)
                # print('receve im type', type(im))
                slam_res = slam.product(im)  #slam compute
                slam_res = Image.fromarray(slam_res.astype('uint8')).convert('RGB')
                qt_im = ImageQt(slam_res)  #convert np array to QPixmap to show
                pix = QPixmap.fromImage(qt_im)
                self.slam_img.setPixmap(pix)
        except socket.timeout:
            pass

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("UAV Controller")

    window = Controller()
    app.exec_()


#TODO  time机制实时显示图片