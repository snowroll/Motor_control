# -*- coding:utf-8 -*- 
'''
author: chaihj15
date: 2018/07/15
'''

import matplotlib.pyplot as plt
import cv2
import numpy as np
import math
import PIL
import vrep
from Function.Slam import Slam

slam = Slam()

class Detect:
    def __init__(self):
        self.img_num = 0

    def draw_plt(self, x, y):
        figure = plt.figure()
        figure.patch.set_facecolor('black')
        plt.xlim(xmax = 6, xmin = -6)
        plt.ylim(ymax = 6, ymin = -6)
        plt.axis('off')
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
        plt.margins(0,0)
        plt.plot(x, y, 'ro')
        # plt.savefig("detect_img0.jpg")
        # im = cv2.imread("detect_img0.jpg")
        im = self.fig2img( figure )
        w, h = im.size
        im = np.array(im)
        res = cv2.resize(im, dsize=(math.ceil(w / 2), math.ceil(h / 2)), interpolation=cv2.INTER_CUBIC)
        print(res.shape)
        # im.show()
        # plt.show()
        return res
    
    def fig2data (self, fig):
        """
        @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
        @param fig a matplotlib figure
        @return a numpy 3D array of RGBA values
        """
        # draw the renderer
        fig.canvas.draw ( )
    
        # Get the RGBA buffer from the figure
        w,h = fig.canvas.get_width_height()
        buf = np.fromstring ( fig.canvas.tostring_argb(), dtype=np.uint8 )
        buf.shape = ( w, h,4 )
    
        # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
        buf = np.roll ( buf, 3, axis = 2 )
        return buf

    def fig2img (self, fig):
        """
        @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
        @param fig a matplotlib figure
        @return a Python Imaging Library ( PIL ) image
        """
        # put the figure pixmap into a numpy array
        buf = self.fig2data ( fig )
        w, h, d = buf.shape
        return PIL.Image.frombytes( "RGBA", ( w ,h ), buf.tostring( ) )

    def map_point(self, client_id, singal_name):  #获取每一次雷达扫描的点集,并作图
        x = []
        y = []
        np_img = []
        err, signal = vrep.simxReadStringStream(client_id, singal_name, vrep.simx_opmode_buffer) 
        if err == vrep.simx_return_ok:
            data = vrep.simxUnpackFloats(signal)
            for i in range(0, len(data), 3):
                if data[i + 2] > 0:
                    x.append(data[i])
                    y.append(data[i + 1])
                else:
                    pass
            np_img = mydetect.draw_plt(x, y)
            
            if len(np_img) != 0:
                cv2.imwrite('data/' + str(self.img_num) + '.jpg', np_img)
                result = slam.no_T_Slam(np_img)
                cv2.imshow('map point', result)
                cv2.waitKey(1500)
                cv2.destroyAllWindows()
        return np_img


