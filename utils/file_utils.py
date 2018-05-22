#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:31:32 2018

@author: gongyanshang1
"""
import os
import shutil

def copy_by_filelist(filepath, targetpath, sourcepaths):
    """
    从sourcepaths中拷贝文件至targetpath，待拷贝文件名从filepath读取
    """
    
    # 读取所有源文件夹下的文件
    source_dict = dict()
    for sourcepath in sourcepaths:
        for file in os.listdir(sourcepath):
            file_path = os.path.join(sourcepath, file)  
            source_dict[file] = file_path
    
    # 遍历filepath中的文件并拷贝
    with open(filepath, 'r') as f:
        image_name_list = f.readlines()
    for image_name in image_name_list:
        if image_name[-1] == '\n':
            image_name = image_name[:-1]
        if image_name in source_dict:
            file_path = source_dict[image_name] # 待拷贝文件的原位置
            target = os.path.join(targetpath, image_name)
            shutil.copyfile(file_path, target)
        else:
            print('文件不存在，path=' + file_path)
    
    print('%s中的图片已拷贝至%s' % (filepath, targetpath))
    
def output_filelist(dirpaths, outputfile):
    """
    将dirpaths文件夹下的所有文件名输出到文件中
    """
    with open(outputfile, 'w') as f:
        for dirpath in dirpaths:
            for file in os.listdir(dirpath):
                f.write(file)
        print('%s下的文件名已输出至%s' % (dirpaths, outputfile))
    
    
if __name__ == '__main__':
    filepath = "C:/Users/gongyanshang1/Desktop/jd_val_bad_img_4_18.txt"
    targetpath = 'C:/Users/gongyanshang1/Desktop/jd_val_bad_img_4_18_select'
    sourcepaths = ['C:/Users/gongyanshang1/Desktop/jd_val_good_img_4_18', 'C:/Users/gongyanshang1/Desktop/jd_val_bad_img_4_18']
    copy_by_filelist(filepath, targetpath, sourcepaths)

