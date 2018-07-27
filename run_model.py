# -*- coding:utf-8 -*-

import time
import os
import sys
import cv2
import imageio
from io import StringIO
import signal
import pandas
import pickle
import numpy as np
from controller import PD, PID
from Function.Obstacle import Obstacle
from Function.key import Key
from Gesture.hand import Hand

count1 = 0
def bug():
    global count1
    print("debug", count1)
    count1 += 1

#----------------- Constant --------------#
dt = 0.001  #program run time 1ms  vrep 10ms
dire = ''
frame_count = 0



#-------------------- Instance -----------#
key_cont = Key()
gesture_cont = Hand()
camera = cv2.VideoCapture(0)


#-------------------- control ------------#
def move_control(target_obj, direct, control):  
    if direct != "":
        target_obj.move_to(direct)
        print('move to ', direct)
        control.control_step()


def gesture(Capture, Myhand, target_obj, control):  #move by hand recoginze
    global frame_count
    dire = ''
    if frame_count == 50:
        ret, img = Capture.read(0)
        cv2.imshow("gesture control", img)
        dire = Myhand.predict(img)
        key = cv2.waitKey(20) & 0xff
        frame_count = 0
    else:
        frame_count += 1
    return dire


def Move_step(method, target_obj, control):
    global key_cont, gesture_cont, camera
    if method == 'key':  #control by keyborad
        move_control(target_obj, key_cont.dire, control)
        key_cont.stop()
    elif method == 'hand':
        dire = gesture(camera, gesture_cont, target_obj, control)
        move_control(target_obj, dire, control)
        


if __name__ == '__main__':
    step_num = 17000
    model_name = 'pid'
    control_name = 'key'
    target_func = None   

    print('argv', sys.argv)
    
    if len(sys.argv) == 2:
        model_name = sys.argv[1]  #diff model

    if len(sys.argv) == 3:
        model_name = sys.argv[1]  #diff model
        control_name = sys.argv[2]  #
        print('control', control_name, 'model', model_name)
        
    if model_name in ['pd', 'pid', 'pidt']:
        if model_name == 'pd':
            control = PD(target_func = target_func)
        elif model_name == 'pid':
            control = PID(target_func = target_func)
        else:
            control = PID(target_func = target_func)

        state = []
        count = 0

        if control_name == 'key':
            key_cont.start()
        target_obj = Obstacle('Quadricopter_target', control.cid, control.target)

        while True:
            Move_step(control_name, target_obj, control)
            control.control_step()
                
        
            