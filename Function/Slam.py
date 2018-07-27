# -*- coding: utf-8 -*-    
import cv2    
import numpy as np    
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 4
MAX_IMG_COUNT = 5
MAP_RANGE = 500
SEARCH_RANGE = 5
MAX_MISS = 1.2

class Slam(object):
    """docstring for Slam"""
    def __init__(self):
        super(Slam).__init__()

        self.Big_Map = np.zeros((MAP_RANGE*2,MAP_RANGE*2))
        self.V = np.array([0,0])
        self.result = None
        self.flag = 0;
        self.best = []
        self.pre = None
        self.resent_result = None

    def Low_B_Slam(self,v,img):

        img_V = self.V + v
        L_x = -img.shape[0] + img_V[0]
        L_y = -img.shape[1] + img_V[1]
        for x in range(1,img.shape[0]):
                for y in range(1,img.shape[1]):
                    if ((sum (img[x][y]) != 255*3) and  (sum(img[x][y]) != 0 )):
                        self.Big_Map[x+L_x][y+L_y] = img1[x][y]

    def get_Big_Map(self):
        return self.Big_Map

    def rgb2gray(self,rgb):
        return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

    def clear_img(self,img):
        
        # print(np.size(np.shape(img)))
        if np.size(np.shape(img)) == 3:
            # pass
            img = self.rgb2gray(img)

        ret,thresh1 = cv2.threshold(img,25,100,cv2.THRESH_BINARY)
        return thresh1

    def no_T_Slam(self,img):
        img = self.clear_img(img)
        if img is None:
            return 
        if self.flag == 0:
            result = img
            self.result = result
            self.flag = 1
            self.pre = result.sum()
            return result

        img2 = img
        temp_sum = img2.sum()

        if temp_sum/(self.pre+50) > MAX_MISS:
            print("error: bad match")
            self.result = self.resent_result
            # return self.result

        self.pre = temp_sum
        best_vector = np.array([0,0])
        best_px = 0
        best_py = 0
        match_value = 0
        len_vector = SEARCH_RANGE*SEARCH_RANGE*2
        for rx in range(-SEARCH_RANGE,SEARCH_RANGE+1):
            for ry in range(-SEARCH_RANGE,SEARCH_RANGE+1):
                v1 = np.array([rx,ry]) + self.V
              
                max_x =  min(img2.shape[0],self.result.shape[0]-v1[0],self.result.shape[0]) 
                max_y =  min(img2.shape[1],self.result.shape[1]-v1[1],self.result.shape[1]) 
                min_x = max(0,v1[0])
                min_y = max(0,v1[1])
                p_min_x = min(0,v1[0])
                p_min_y = min(0,v1[1])

                part_result =  np.zeros(img2.shape - np.array([p_min_x,p_min_y]))                
                part_result[0-p_min_x:max_x-min_x-p_min_x,0-p_min_y:max_y-min_y-p_min_y] = self.result[min_x:max_x,min_y:max_y]
             
                C = (np.fabs(img2 - part_result[0:img2.shape[0],0:img2.shape[1]]))
                count = part_result.sum() + img2.sum()
                temp_match_value = (count - C.sum())
               
                if temp_match_value > match_value:
                    match_value = temp_match_value
                    best_vector = v1
                    len_vector = rx*rx+ry*ry
                    best_px = p_min_x
                    best_py = p_min_y
                else:
                    if temp_match_value == match_value:
                        temp_len_vector = rx*rx+ry*ry
                        if temp_len_vector < len_vector:
                            len_vector = temp_len_vector
                            best_vector = v1
                            best_px = p_min_x
                            best_py = p_min_y

        print("best_vector",best_vector)
        max_x = max(self.result.shape[0],best_vector[0]+img2.shape[0])
        max_y = max(self.result.shape[1],best_vector[1]+img2.shape[1]) 
        temp_new_img = np.zeros([max_x,max_y]-np.array([best_px,best_py]))
                 
        temp_new_img[0-best_px:self.result.shape[0]-best_px,0-best_py:self.result.shape[1]-best_py] = self.result
        for x in range(1,img2.shape[0]):
                for y in range(1,img2.shape[1]):
                    if ( (img2[x][y]) != 0):
                        temp_new_img[x+best_vector[0]-best_px][y+best_vector[1]-best_py] = 255
                   
        # cv2.imshow( "result", temp_new_img)       
        # cv2.waitKey(0)

        self.best.append(best_vector)
        self.resent_result = temp_new_img      
        self.V = best_vector

        return temp_new_img

    def GetGoodMatch(self,img1,img2 ):

        sift = cv2.xfeatures2d.SIFT_create()
        self.kp1, des1 = sift.detectAndCompute(img2,None)
        self.kp2, des2 = sift.detectAndCompute(img1,None)
     
        FLANN_INDEX_KDTREE = 0    
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)    
        search_params = dict(checks = 50)   # or pass empty dictionary 

        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(des1,des2,k=2)
       
        good = []    
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)

        imgMatches = None    
        imgMatches = cv2.drawMatches( img1, self.kp1, img2, self.kp2, good, imgMatches )    
        cv2.imshow( "good_matches", imgMatches )    
        cv2.imwrite( "./data/good_matches.png", imgMatches )    
        cv2.waitKey(0)
        return good

    def Slam3D():
        pass


# # demo --------

# mySlam = Slam()

# for x in range(1,53):
#     if x!=6:
#         a = cv2.imread('data/'+str(x)+'.jpg')
#         print(x)
#         result = mySlam.no_T_Slam(a)


