# -*- coding:utf-8 -*- 
'''
author: chaihj15
date: 2018/07/18
'''

from Const import *
from madgwickahrs import MadgwickAHRS
from quaternion import Quaternion
from array import array

class Motor(object):
    myAhrs = MadgwickAHRS()
    def __init__(self, client_id,  Handle_name, Ahrs = myAhrs):
        self.client_id = client_id 
        self.handle = vrep.simxGetObjectHandle(client_id, Handle_name, blocking)
        self.accelerometer = np.array([0.0, 0.0, 0.0])  #3轴加速度
        self.gyroscope     = np.array([0.0, 0.0, 0.0])  #3轴角速度
        self.coef          = np.array([0.0, 0.0, 0.0])  #Kp Ki Kd  比例,积分,微分系数
        self.seted_euler   = np.array([0.0, 0.0, 0.0])  #欧拉角 roll pitch yaw
        self.real_euler    = np.array([0.0, 0.0, 0.0])
        self.error_old     = np.array([0.0, 0.0, 0.0])
        self.error_inter   = np.array([0.0, 0.0, 0.0])
        self.Thr           = 5.335  #初始油门设为悬浮所需值
        self.Ahrs = Ahrs
        vel = vrep.simxGetFloatSignal(self.client_id, 'vel', streaming)
        
    def set_data(self, thr, Kp, Ki, Kd, roll = 0.0, pitch = 0.0, yaw = 0.0):  #设定期望欧拉角
        self.seted_euler = np.array([roll, pitch, yaw])
        self.Thr = thr
        self.coef = np.array([Kp, Ki, Kd])
        self.error_old   = np.array([0.0, 0.0, 0.0])
        self.error_inter = np.array([0.0, 0.0, 0.0])

    def PID(self, error_euler):  #根据误差数据来调整四轴转速
        error_diff = error_euler - self.error_old
        self.error_old = error_euler  #近似表示误差微分
        self.error_inter += self.error_old  #近似表示误差积分

        print("1", self.error_old, self.error_inter)
        #Ail 横滚  Ele 俯仰  Rud 偏航  coef Kp Ki Kd  比例,积分,微分系数
        Ail = self.coef[0] * self.error_old[0] + self.coef[1] * self.error_inter[0] + self.coef[2] * error_diff[0]          
        Ele = self.coef[0] * self.error_old[1] + self.coef[1] * self.error_inter[1] + self.coef[2] * error_diff[1]
        Rud = self.coef[0] * self.error_old[2] + self.coef[1] * self.error_inter[2] + self.coef[2] * error_diff[2]

        print("2", Ail, Ele, Rud)
        Motor_v = [5.335, 5.335, 5.335, 5.335]
        Motor_v[0] = self.Thr + Ail - Ele + Rud
        Motor_v[1] = self.Thr - Ail - Ele - Rud
        Motor_v[2] = self.Thr - Ail + Ele + Rud
        Motor_v[3] = self.Thr + Ail + Ele - Rud


        print("3", Motor_v)
        # data = vrep.simxGetStringSignal(self.client_id, 'Motor_v', streaming)
        # if not data:
        #     data = ''
        data =  vrep.simxPackFloats(Motor_v)
        err  = vrep.simxWriteStringStream(self.client_id, 'Motor_v', data, oneshot)
        if err == vrep.simx_return_ok:
            print("send successfull")
        print("4")


    def update(self, signal_gyro, signal_acce):  
        err_gyro, gyro_signal = vrep.simxReadStringStream(self.client_id, signal_gyro, buffer)
        err_acce, acce_signal = vrep.simxReadStringStream(self.client_id, signal_acce, buffer)

        if err_gyro == vrep.simx_return_ok:
            self.gyroscope = vrep.simxUnpackFloats(gyro_signal)

        if err_acce == vrep.simx_return_ok:
            self.accelerometer = vrep.simxUnpackFloats(acce_signal)

        if err_acce == vrep.simx_return_ok and err_gyro == vrep.simx_return_ok:
            self.Ahrs.update_imu(self.gyroscope, self.accelerometer)
            self.real_euler[0], self.real_euler[1], self.real_euler[2] = self.Ahrs.quaternion.to_euler_angles()
            print("real " )
            print(self.real_euler)
            print("seted ")
            print(self.seted_euler)
            euler_error = self.seted_euler - self.real_euler
            print("euler error", euler_error)
            self.PID(euler_error)    
    
# 初始化为numpy array