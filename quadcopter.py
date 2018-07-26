#-*- coding:utf-8 -*- 

import numpy as np
import vrep
import ctypes
import math
import sys
import time

sim_dt = 0.01 
dt = 0.001

SYNC = True
vrep_mode = vrep.simx_opmode_oneshot

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

count = 0
def bug():
    global count
    print("debug", count)
    count += 1

class Quadcopter( object ):
    """
    This callable class will return the state of the quadcopter relative to its
    target whenever it is called. It will also accept motor commands which will be
    sent to the quadcopter in V-REP.
    """
    def __init__( self, max_target_distance=4, noise=False,
                  noise_std=None, dodging=True,
                  target_func=None, cid=None
                ):

        # If a cid is specified, assume the connection has already been
        # established and should remain open
        if cid is None:
            vrep.simxFinish(-1) # just in case, close all opened connections
            self.cid = vrep.simxStart('127.0.0.1',19997,True,True,5000,5)
        else:
            self.cid = cid

        if self.cid != -1:
            print ('Connected to V-REP remote API server, client id: %s' % self.cid)
            vrep.simxStartSimulation( self.cid, vrep.simx_opmode_oneshot )
            if SYNC:
                vrep.simxSynchronous( self.cid, True )
        else:
            print ('Failed connecting to V-REP remote API server')
            self.exit()

        err, self.copter = vrep.simxGetObjectHandle(self.cid, "Quadricopter_base",
                                                vrep.simx_opmode_oneshot_wait )
        err, self.target = vrep.simxGetObjectHandle(self.cid, "Quadricopter_target",
                                                vrep.simx_opmode_oneshot_wait )
        
        # Reset the motor commands to zero
        packedData=vrep.simxPackFloats([0,0,0,0])
        raw_bytes = (ctypes.c_ubyte * len(packedData)).from_buffer_copy(packedData) 
        
        err = vrep.simxSetStringSignal(self.cid, "rotorTargetVelocities",
                                        raw_bytes,
                                        vrep_mode)
    
        self.pos = [0,0,0]
        self.pos_err = [0,0,0]
        self.t_pos = [0,0,0]
        self.lin = [0,0,0]
        self.ori = [0,0,0]
        self.ori_err = [0,0,0]
        self.t_ori = [0,0,0]
        self.ang = [0,0,0]
        self.count = 0

        # Maximum target distance error that can be returned
        self.max_target_distance = max_target_distance
        # If noise is being modelled
        if noise_std is not None:
            self.noise = True
        else:
            self.noise = False

        # Standard Deviation of the noise for the 4 state variables
        self.noise_std = noise_std
        # Overwrite the get_target method if the target is to be controlled by a
        # function instead of by V-REP
        if target_func is not None:
          
            self.step = 0
            self.target_func = target_func

            def get_target():
                err, t_ori = vrep.simxGetObjectOrientation(self.cid, self.target, -1,
                                                    vrep_mode )
                err, t_pos = vrep.simxGetObjectPosition(self.cid, self.target, -1,
                                                vrep_mode )
        
                # Convert orientations to z-y-x convention
                t_ori = convert_angles(t_ori)
                self.t_pos, self.t_ori = self.target_func( self.step )
                self.step += 1

            self.get_target = get_target
  
    def stop( self ):
        """
        Stops the simulation
        """
        err = vrep.simxStopSimulation( self.cid, vrep.simx_opmode_oneshot_wait )
        time.sleep(0.01) # Maybe this will prevent V-REP from crashing as often
        return hasattr(self, 'failed') # Returns true if this is a failed run


    def reset( self ):
        err = vrep.simxStopSimulation(self.cid, vrep.simx_opmode_oneshot_wait)
        time.sleep(1)
        self.pos_err = [0,0,0]
        self.ori_err = [0,0,0]
        self.lin = [0,0,0]
        self.ang = [0,0,0]
        err = vrep.simxStartSimulation(self.cid, vrep.simx_opmode_oneshot_wait)
        if SYNC:
            vrep.simxSynchronous( self.cid, True )
    
    def exit( self ):
        self.failed = True
        exit(1)

    def get_target( self ):
        err, self.t_ori = vrep.simxGetObjectOrientation(self.cid, self.target, -1,
                                                    vrep_mode )
        err, self.t_pos = vrep.simxGetObjectPosition(self.cid, self.target, -1,
                                                vrep_mode )
        
        # Convert orientations to z-y-x convention
        self.t_ori = convert_angles(self.t_ori)

    def calculate_error( self ):
        # Return the state variables
        err, self.ori = vrep.simxGetObjectOrientation(self.cid, self.copter, -1,
                                                vrep_mode )
        err, self.pos = vrep.simxGetObjectPosition(self.cid, self.copter, -1,
                                            vrep_mode )
        err, self.lin, self.ang = vrep.simxGetObjectVelocity(self.cid, self.copter,
                                                            vrep_mode )
        
        self.ori = convert_angles(self.ori)
        
        # Apply noise to each measurement if required
        #FIXME this is a dumb way to do this, clean it up later
        if self.noise:
            n_pos = np.random.normal(0,self.noise_std[0],3)
            n_lin = np.random.normal(0,self.noise_std[1],3)
            n_ori = np.random.normal(0,self.noise_std[2],3)
            n_ang = np.random.normal(0,self.noise_std[3],3)
            for i in range(3):
                self.pos[i] += n_pos[i]
                self.lin[i] += n_lin[i]
                self.ori[i] += n_ori[i]
                self.ang[i] += n_ang[i]
            #TODO: might have to wrap angles here
        
        # Find the error
        self.ori_err = [self.t_ori[0] - self.ori[0], 
                        self.t_ori[1] - self.ori[1],
                        self.t_ori[2] - self.ori[2]]
        cz = math.cos(self.ori[2])
        sz = math.sin(self.ori[2])
        x_err = self.t_pos[0] - self.pos[0]
        y_err = self.t_pos[1] - self.pos[1]
        self.pos_err = [ x_err * cz + y_err * sz, 
                        -x_err * sz + y_err * cz, 
                         self.t_pos[2] - self.pos[2]]
        
        self.lin = [self.lin[0]*cz+self.lin[1]*sz, -self.lin[0]*sz+self.lin[1]*cz, self.lin[2]]
        self.ang = [self.ang[0]*cz+self.ang[1]*sz, -self.ang[0]*sz+self.ang[1]*cz, self.ang[2]]

        for i in range(3):
            if self.ori_err[i] > math.pi:
                self.ori_err[i] -= 2 * math.pi
            elif self.ori_err[i] < -math.pi:
                self.ori_err[i] += 2 * math.pi

    def send_motor_commands( self, values ):

        # Limit motors by max and min values
        motor_values = np.zeros(4)
        for i in range(4):
            """
            if values[i] > 30:
                motor_values[i] = 30
            elif values[i] < 0:
                motor_values[i] = 0
            else:
                motor_values[i] = values[i]
            """
            motor_values[i] = values[i]
        packedData=vrep.simxPackFloats(motor_values.flatten())
        raw_bytes = (ctypes.c_ubyte * len(packedData)).from_buffer_copy(packedData) 
        err = vrep.simxSetStringSignal(self.cid, "rotorTargetVelocities",
                                        raw_bytes,
                                        vrep_mode)
    
    def handle_input( self, values ):
        
        # Send motor commands to V-REP
        self.send_motor_commands( values )

        # Retrieve target location
        self.get_target()

        # Calculate state error
        self.calculate_error()

    def bound( self, value ):
        if abs( value ) > self.max_target_distance:
            return math.copysign( self.max_target_distance, value )
        else:
            return value

    def get_state( self ):
        """
        Returns the current state. Used for recording benchmarks of performance
        """
        return [self.pos, self.ori, 
                self.lin, self.ang, 
                self.t_pos, self.t_ori]

    def handle_output( self ):
        l = math.sqrt(self.pos_err[0]**2 + self.pos_err[1]**2)
        bl = self.bound(l)
        r = (bl+.1)/(l+.1)

        return [r*self.pos_err[0], r*self.pos_err[1], self.bound(self.pos_err[2]), 
                self.lin[0], self.lin[1], self.lin[2], 
                self.ori_err[0], self.ori_err[1], self.ori_err[2], 
                self.ang[0], self.ang[1], self.ang[2]]

    def __call__( self, t, values ):
        """ This class will be callable within a nengo node. It will accept as input
        the control signals for each rotor, and will output the relevant state
        variables (position, velocity, orientation, angular velocity).
        """
        self.count += 1
        if self.count == int(round(sim_dt/dt)):
            self.count = 0
            self.handle_input( values )

            if SYNC:
                vrep.simxSynchronousTrigger( self.cid )
        return self.handle_output()