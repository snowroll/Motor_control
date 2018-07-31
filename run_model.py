# -*- coding:utf-8 -*-

import time, os, sys
import imageio
from io import StringIO
import signal
import numpy as np
# from Function.key import gesture
# from Gesture.hand import Hand
from controller import PD, PID
# from Function.Server import server
from Server import server
import vrep

#----------------- Constant --------------#
dt = 0.001  #program run time 1ms  vrep 10ms
obj = None

#-------------------- Instance -----------#
# key_cont = Key()
# gesture_cont = gesture()
gesture_cont = None
server_cont = server()
print('server begin')


if __name__ == '__main__':
    step_num = 17000
    model_name = 'pid'
    control_name = 'key'
    target_func = None  
    
    if len(sys.argv) == 2:
        model_name = sys.argv[1]  #diff model

    if len(sys.argv) == 3:
        model_name = sys.argv[1]  
        control_name = sys.argv[2]  #diff control method  1 key  2 gesture 3 ??
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
            obj = key_cont
            print("key board control")
        elif control_name == 'hand':
            obj = gesture_cont
        elif control_name == 'control':
            obj = server_cont

        while True:
            control.control_step(obj, control_name)
            
                
        
            