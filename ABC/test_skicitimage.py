# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 10:41:01 2018

@author: gongyanshang1
"""

# =============================================================================
# from skimage.feature import match_template
# import numpy as np
# import PIL.Image as Image
# 
# def get_array(img_file, convert='L'):   
#     img1 = Image.open(img_file)
#     img1 = img1.convert(convert)
#     img1 = np.array(img1)
#     return img1
# 
# img_file1 = 'data/tian.png'
# img_file2 = 'data/xu.png'
# img1 = get_array(img_file1)
# img2 = get_array(img_file2)
# 
# result = match_template(img2, img1)
# print(result)
# =============================================================================

# =============================================================================
# import cv2
# import numpy as np
#     
# def mathc_img(image,Target,value):
# 
#     img_rgb = cv2.imread(image)
#     img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#     template = cv2.imread(Target,0)
#     w, h = template.shape[::-1]
#     res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#     threshold = value
#     loc = np.where( res >= threshold)
#     for pt in zip(*loc[::-1]):
#         cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)   
#     cv2.imshow('Detected',img_rgb)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# 
# image=('data/tian.png')
# Target=('data/xu.png')
# value=0.9
# mathc_img(image,Target,value)
# =============================================================================

# =============================================================================
# import cv2
# img = cv2.imread('data/tian.png')
# gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# sift = cv2.xfeatures2d.SIFT_create()
# kp = sift.detect(gray,None)
# img=cv2.drawKeypoints(gray,kp,img)
# cv2.imshow(img)
# #cv2.imwrite('sift_keypoints.jpg',img)
# 
# =============================================================================

# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *
from numpy import *
import os

def process_image(imagename, resultname, params="--edge-thresh 10 --peak-thresh 5"):
    """ 处理一幅图像，然后将结果保存在文件中"""

    if imagename[-3:] != 'pgm':
        #创建一个pgm文件
        im = Image.open(imagename).convert('L')
        im.save('tmp.pgm')
        imagename ='tmp.pgm'
    cmmd = str("sift "+imagename+" --output="+resultname+" "+params)
    os.system(cmmd)
    print('processed', imagename, 'to', resultname)

# =============================================================================
# def read_features_from_file(filename):
#     """读取特征属性值，然后将其以矩阵的形式返回"""
#     f = loadtxt(filename)
#     return f[:,:4], f[:,4:] #特征位置，描述子
# =============================================================================

# =============================================================================
# def write_featrues_to_file(filename, locs, desc):
#     """将特征位置和描述子保存到文件中"""
#     savetxt(filename, hstack((locs,desc)))
# =============================================================================

def plot_features(im, locs, circle=False):
    """显示带有特征的图像
       输入：im（数组图像），locs（每个特征的行、列、尺度和朝向）"""

    def draw_circle(c,r):
        t = arange(0,1.01,.01)*2*pi
        x = r*cos(t) + c[0]
        y = r*sin(t) + c[1]
        plot(x, y, 'b', linewidth=2)

    imshow(im)
    if circle:
        for p in locs:
            draw_circle(p[:2], p[2])
    else: 
        plot(locs[:,0], locs[:,1], 'ob')
    axis('off')

imname = 'data/baidu.jpg'
#im1 = array(Image.open(imname).convert('L'))
process_image(imname, 'data/tian.sift')
#l1,d1 = read_features_from_file('empire.sift')

# =============================================================================
# figure()
# gray()
# plot_features(im1, l1, circle=True)
# show()
# =============================================================================
