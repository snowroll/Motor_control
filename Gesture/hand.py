# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
from skimage import io,transform
from Gesture.alexnet import AlexNet 
# import matplotlib.pyplot as plt
from PIL import Image

Direct = {1:'U', 2:'D', 3:'L', 4:'R', 5:'F', 6:'B', 7:''}

class Hand(object):
    """docstring for Hand"""
    def __init__(self):
        super(Hand, self).__init__()
        # Network params
        learning_rate = 0.03
        num_epochs = 10
        batch_size = 1
        display_step = 4
        dropout = 0.5
        num_classes = 7
        train_layers = ['fc8']

        print(batch_size)

        self.x = tf.placeholder(tf.float32, [ 1,227, 227, 3])
        y = tf.placeholder(tf.float32, [ batch_size,num_classes])
        self.keep_prob = tf.placeholder(tf.float32)

        self.model = AlexNet(self.x, self.keep_prob, num_classes, train_layers)

        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = self.model.fc8, labels = y))
        optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost,var_list = tf.global_variables()[-2:])
        correct_pred = tf.equal(tf.argmax(self.model.fc8,1), tf.argmax(y,1))
        accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

        self.saver = tf.train.Saver(tf.global_variables())
        self.sess = tf.InteractiveSession()
        # self.model.load_initial_weights(self.sess)
        self.saver.restore(self.sess, "Gesture/Model/model.ckpt") 

    def reshape(self,img):
        try:
            img = Image.fromarray(img.astype('uint8')).convert('RGB')
        except Exception as e:
            pass
        
        r,g,b=img.split()
        pic=Image.merge('RGB',(b,g,r))
        dst = pic.resize((227, 227))
        a = np.array(dst) - [103.939, 116.779, 123.68]
        # print (a)
        return a

    def predict(self, img):
        a = self.reshape(img)
        img_array = np.array(a)
       
        x_test = np.zeros((1,227,227,3))
        x_test[0] = img_array

        pre = self.model.fc8.eval(feed_dict={self.x:x_test[0:1],self.keep_prob:1.})
        

        rank = 0
        now = -1
        result = 6

        # print(np.shape(pre))
        # print((pre))

        for x in pre[0]:
            rank += 1
            if now < x:
                now = x
                result = rank 

        return Direct[result]



# demo ---- #
# print(1,2,3,4,5,6,7)

# myHand = Hand()

# for x in range(1,6):
    
    # img = io.imread(str(x)+".jpg")
#     # print(img)
    # img = transform.resize(img,(227,227,3))# img shape must be 227*227*3
    
#     # io.imshow(img)
#     # plt.show()
    
    # print(x, myHand.predict(img*255/2+255/2))# img value must be 0 - 255
    # print(x, myHand.predict(img))# img value must be 0 - 255


#     # print(img*255/2+255/2)








