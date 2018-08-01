import numpy as np
import cv2
import matplotlib.pyplot as plt


def lmap(func, *iterables):
    return list(map(func, *iterables))


def printd(*args, sep=' ', end='\n', file=None):
    # print(*args, sep=sep, end=end, file=file)
    pass


def bgr2gray(img: np.ndarray):
    if len(img.shape) == 2:
        return img
    else:
        lumi = np.array([0.114, 0.587, 0.299])  # bgr combine
        gray = np.sum(img * lumi, axis=2).astype(np.uint8)
        return gray


def imshow_cv(imseq, delay=0, winname='compare'):
    plt.plot()
    if type(imseq) == np.ndarray:
        imseq = [imseq]
    for img in imseq:
        cv2.imshow(winname, img.astype(np.uint8))
        cv2.waitKey(delay)
    cv2.destroyAllWindows()


def imshow(img: np.ndarray):
    if img.max() > 1:
        img = img.clip(0, 255) / 255
    plt.imshow(img[:, :, ::-1])
    plt.show()


def imshow_cv_one(imseq, delay=0):
    plt.plot()
    if type(imseq) == np.ndarray:
        imseq = [imseq]
    maxh = max(map(lambda x: x.shape[0], imseq))
    imseq = lmap(
        lambda arr: np.pad(arr, [(0, maxh - arr.shape[0]), (0, 10), (0, 0)], 'constant'),
        imseq)
    img = np.concatenate(imseq, axis=1)
    cv2.imshow('compare', img.astype(np.uint8))
    cv2.waitKey(delay)
    cv2.destroyAllWindows()