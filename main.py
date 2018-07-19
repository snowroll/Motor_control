# -*- coding:utf-8 -*- 
'''
author: chaihj15
date: 2018/07/17
'''

from Const import *
from key import Key
from Motor import Motor
# from madgwickahrs import MadgwickAHRS

myKey = Key()

if __name__ == '__main__':
    vrep.simxFinish(-1)  #停止之前的仿真
    client_id = vrep.simxStart("127.0.0.1", 19997, True, True, 5000, 5)  #建立与服务器的连接  19997自动建立连接

    if client_id == -1:  #连接失败
        print('Fail to connect')

    else:
        print('connect to v-rep') 
        myKey.start()  #键盘控制       

        try:
            vrep.simxStartSimulation(client_id, oneshot_wait)
            mymotor = Motor(client_id, 'Quadricopter')
            mymotor.set_data(5.335, 0.14, 0.045, 0.004, 0, 0, 0)
            err, gyro_signal = vrep.simxReadStringStream(client_id, 'gyro_signal', streaming)
            err, acce_signal = vrep.simxReadStringStream(client_id, 'acce_signal', streaming)

            iter_num = 0
            while vrep.simxGetConnectionId(client_id) != -1:
                mymotor.update('gyro_signal', 'acce_signal')
                # if iter_num > 300:
                #     break
                # else:
                #     iter_num += 1

                
                             
        except:
            vrep.simxFinish(client_id)
            print('simulation end')