import tkinter as tk
import matplotlib.pyplot as plt
import time


class GUI:
    def __init__(self, size, paths):
        plt.plot()
        self.paths = paths
        win = tk.Tk()
        win.title('demo')
        h, w = size

        self.canvas = tk.Canvas(win, width=w, height=h, bg='black')
        self.canvas.pack()
        frame = tk.Frame(win)
        frame.pack()

        self.img = tk.PhotoImage(width=w, height=h)
        self.canvas.create_image((w / 2, h / 2), image=self.img, state='normal')
        self.canvas.image = self.img
        bt = tk.Button(frame, text='draw', command=self.draw)
        bt.grid(row=1, column=1)
        win.mainloop()

    def draw(self):
        self.img.blank()
        for idx in self.paths.solution:
            p = self.paths.pathlist[idx[0] >> 1]
            if idx[0] & 1 == 1:
                p = reversed(p)
            for xy in p:
                self.img.put('#ffffff', (xy[1], xy[0]))
                self.canvas.update()
            time.sleep(0.1)