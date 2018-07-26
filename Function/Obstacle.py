# -*- coding:utf-8 -*- 
'''
author: chaihj15
date: 2018/07/08
'''

import vrep
import math
oneshot = vrep.simx_opmode_oneshot
buffer  = vrep.simx_opmode_buffer
blocking = vrep.simx_opmode_blocking

class Obstacle:
    def __init__(self, name, client_id, target_handle):
        self.name = name
        self.client_id = client_id
        self.target_handle = target_handle
        err_code, self.position = vrep.simxGetObjectPosition(self.client_id, self.target_handle, -1, oneshot)
        err_code, self.ori = vrep.simxGetObjectOrientation(self.client_id, self.target_handle, -1, oneshot)
        # self.ori = convert_angles(self.ori)

        

    def move_to(self, direct):
        print("move to direct " + direct)
        
        if direct == 'L':
            self.position[0] = self.position[0] - 0.01
        elif direct == 'R':
            self.position[0] = self.position[0] + 0.01
        elif direct == 'F':
            self.position[1] = self.position[1] + 0.01
        elif direct == 'B':
            # self.position[1] = self.position[1] - 0.01
            self.ori[2] = self.ori[2] + 1.57
        elif direct == 'U':
            self.position[2] = self.position[2] + 0.01
        elif direct == 'D':
            self.position[2] = self.position[2] - 0.01
        else:
            nothing = ""  #print('no such direct')

        vrep.simxSetObjectPosition(self.client_id, self.target_handle, vrep.sim_handle_parent, self.position, oneshot)
        vrep.simxSetObjectOrientation(self.client_id, self.target_handle, vrep.sim_handle_parent, self.ori, oneshot)

def b( num ):
    """ forces magnitude to be 1 or less """
    if abs( num ) > 1.0:
        return math.copysign( 1.0, num )
    else:
        return num

def convert_angles( ang ):
    """ Converts Euler angles from x-y-z to z-x-y convention """
    s1 = math.sin(ang[0])
    s2 = math.sin(ang[1])
    s3 = math.sin(ang[2])
    c1 = math.cos(ang[0])
    c2 = math.cos(ang[1])
    c3 = math.cos(ang[2])

    pitch = math.asin( b(c1*c3*s2-s1*s3) )
    cp = math.cos(pitch)
    # just in case
    if cp == 0:
        cp = 0.000001

    yaw = math.asin( b((c1*s3+c3*s1*s2)/cp) ) #flipped
    # Fix for getting the quadrants right
    if c3 < 0 and yaw > 0:
        yaw = math.pi - yaw
    elif c3 < 0 and yaw < 0:
        yaw = -math.pi - yaw
    
    roll = math.asin( b((c3*s1+c1*s2*s3)/cp) ) #flipped
    return [roll, pitch, yaw]
