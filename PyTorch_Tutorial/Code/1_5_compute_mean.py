# -*- coding: utf-8 -*-

import numpy as np
import cv2
import random
import os

train_txt_path = os.path.join('..', 'Data/train.txt')

CNum = 2000

img_h, img_w = 32, 32
imgs = np.zeros([img_w, img_h, 3, 1])
means, stdevs = [], []

with open(train_txt_path, 'r') as f:
    lines = f.readlines()
    random.shuffle(lines)

    for i in range(CNum):
        img_path = lines[i].rstrip().split()[0]

        img = cv2.imread(img_path)
        img = cv2.resize(img, (img_h, img_w))

        img = img[:, :, :, np.newaxis]

        imgs = np.concatenate((imgs, img), axis=3)
        print(i)

imgs = imgs.astype(np.float) / 255

for i in range(3):
    pixels = imgs[:, :, i, :].ravel()
    means.append(np.mean(pixels))
    stdevs.append(np.std(pixels))

means.reverse()
stdevs.reverse()

print('normMean = {}'.format(means))
print('normStd = {}'.format(stdevs))


