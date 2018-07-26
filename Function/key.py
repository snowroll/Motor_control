#!/usr/bin/env python

import pyxhook

Key_dict  = {"Left":'L', "Right":'R', "Up":'F', "Down":'B', "Home":'U', "End":'D', "Space":'S'}

class Key(object):
    def __init__(self):
        self.hm = pyxhook.HookManager()
        self.dire = ""

    def OnKeyPress(self, event):  #实现键盘控制飞行器移动
        if event.Key in Key_dict:
            self.dire = Key_dict[event.Key]
            
        elif event.Key == "Escape":
            exit(0)
        else:
            pass

    def start(self):
        self.hm.KeyDown = self.OnKeyPress
        self.hm.HookKeyboard()
        self.hm.start()

    def stop(self):
        self.dire = ""

    


