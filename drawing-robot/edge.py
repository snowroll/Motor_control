import cv2
import numpy as np
from util import *


def canny(imgname):
    img = cv2.imread(imgname)
    hi, lo, r, sigma = 150, 20, 3, 0
    imgblur = cv2.GaussianBlur(img, (r, r), sigma)
    edgeimg = cv2.Canny(imgblur, hi, lo)
    return edgeimg


if __name__ == '__main__':
    imgname = 'bikesgray.jpg'
    img = cv2.imread(imgname)
    while 1:
        hi, lo, r = [int(i) for i in input('para: ').split(' ')]
        sigma = 0
        imgblur = cv2.GaussianBlur(img, (r, r), sigma)
        edgeimg = cv2.Canny(imgblur, hi, lo)
        imshow_cv(edgeimg, winname='edge img')