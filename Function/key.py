#!/usr/bin/env python

import pyxhook
from Gesture.hand import Hand
import cv2

hand_control = Hand()
Key_dict  = {"Left":'L', "Right":'R', "Up":'F', "Down":'B', "Home":'U', "End":'D', "Space":'S'}

class Key(object):
    def __init__(self):
        self.hm = pyxhook.HookManager()
        self.dire = ""

    def OnKeyPress(self, event):  #实现键盘控制飞行器移动
        if event.Key in Key_dict:
            self.dire = Key_dict[event.Key]
            
        elif event.Key == "Escape":
            exit(0)
        else:
            pass

    def start(self):
        self.hm.KeyDown = self.OnKeyPress
        self.hm.HookKeyboard()
        self.hm.start()

    # def stop(self):
    #     self.dire = ""

    def product(self):
        pos, ori = [0, 0, 0], [0, 0, 0]
        if self.dire == 'L':
            pos[0] = pos[0] - 0.01
        elif self.dire == 'R':
            pos[0] = pos[0] + 0.01
        elif self.dire == 'F':
            pos[1] = pos[1] + 0.01
        elif self.dire == 'B':
            # pos[1] = pos[1] - 0.01
            ori[2] = ori[2] + 1.57
        elif self.dire == 'U':
            pos[2] = pos[2] + 0.01
        elif self.dire == 'D':
            pos[2] = pos[2] - 0.01
        else:
            nothing = ""  #print('no such self.dire')
        self.dire = ''
        return pos, ori

class gesture(object):
    def __init__(self):
        self.dire = ''
        self.camera = cv2.VideoCapture(0)
        self.hand = hand_control
    
    def product(self):
        ret, img = self.camera.read(0)
        cv2.imshow('gesture control', img)
        self.dire = self.hand.predict(img)
        print('move to ', self.dire)

        pos, ori = [0, 0, 0], [0, 0, 0]
        if self.dire == 'L':
            pos[0] = pos[0] - 0.01
        elif self.dire == 'R':
            pos[0] = pos[0] + 0.01
        elif self.dire == 'F':
            pos[1] = pos[1] + 0.01
        elif self.dire == 'B':
            pos[1] = pos[1] - 0.01
        elif self.dire == 'U':
            pos[2] = pos[2] + 0.01
        elif self.dire == 'D':
            pos[2] = pos[2] - 0.01
        else:
            nothing = ""  #print('no such self.dire')
        self.dire = ''

        cv2.waitKey(30)
        return pos, ori
        

    


