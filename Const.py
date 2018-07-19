# -*- coding:utf-8 -*- 
'''
author: chaihj15
date: 2018/07/14
'''

import matplotlib.pyplot as plt
import numpy as np
import imageio
import skimage.io
from io import StringIO
import pyxhook  #控制键盘,linux下的库
import pylab
import vrep
import math
import cv2
import PIL 
import sys



# 常量
oneshot      = vrep.simx_opmode_oneshot
oneshot_wait = vrep.simx_opmode_oneshot_wait
blocking     = vrep.simx_opmode_blocking
streaming    = vrep.simx_opmode_streaming
buffer       = vrep.simx_opmode_buffer

dire = ""  #飞行器方向
Dire_dict = {1:'U', 2:'D', 3:'L', 4:'R', 5:'F', 6:'B', 7:'S'}  #根据手势判别结果给出运动方向