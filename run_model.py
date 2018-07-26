# -*- coding:utf-8 -*-

import time
import os
import sys
import signal
import pandas
import pickle
import numpy as np
from controller import PD, PID
from Function.Obstacle import Obstacle
from Function.key import Key

dt = 0.001  #program run time 1ms  vrep 10ms
key_cont = Key()

if __name__ == '__main__':
    step_num = 17000
    model_name = 'pid'
    

    target_func = None   
    
    if len(sys.argv) == 2:
        model_name = sys.argv[1]  #diff control
        
    if model_name in ['pd', 'pid', 'pidt']:
        if model_name == 'pd':
            control = PD(target_func = target_func)
        elif model_name == 'pid':
            control = PID(target_func = target_func)
        else:
            control = PID(target_func = target_func)

        state = []
        count = 0

        key_cont.start()
        target_obj = Obstacle('Quadricopter_target', control.cid, control.target)

        while True:
            if key_cont.dire != '':
                print('key is null')
                target_obj.move_to(key_cont.dire)
                control.control_step()
                key_cont.stop()
            control.control_step()
                
        
            