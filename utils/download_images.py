# -*- coding:utf-8 -*-
import urllib
from joblib import Parallel, delayed

def fetch(url, path):
    try:
        urllib.urlretrieve(url, path + url.split("/")[-1])
    except:
        print(url + " fail")


def download_img(file_path, pos_dir, neg_dir):
    '''
    将图片分为正负样本，并自动下载到两个文件夹中（多线程下载）
    file中每一行的格式：id + url + 负样本概率 + 正样本概率 + 真实标签
    '''
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
        def is_pos(line): 
            return line.strip().split('\t')[-1] == '1' # 1是正样本
        def is_neg(line): 
            return line.strip().split('\t')[-1] == '0'
        def is_ignore(line): 
            return line.strip().split('\t')[-1] != '0' and line.strip().split('\t')[-1] != '1' # 1是牛皮癣，0是非牛皮癣
        
        pos_lines = map(lambda line : "https://img14.360buyimg.com/n0/" + line.strip().split('\t')[1], filter(is_pos, lines))
        neg_lines = map(lambda line : "https://img14.360buyimg.com/n0/" + line.strip().split('\t')[1], filter(is_neg, lines))
        ignore_lines = map(lambda line : "https://img14.360buyimg.com/n0/" + line.strip().split('\t')[1], filter(is_ignore, lines))
        
        print('pos_lines:' + str(len(list(pos_lines))))
        print('neg_lines:' + str(len(list(neg_lines))))
        print('ignore_lines:' + str(list(ignore_lines)))
        
        Parallel(n_jobs=3)(delayed(fetch)(url, pos_dir) for url in pos_lines)
        Parallel(n_jobs=3)(delayed(fetch)(url, neg_dir) for url in neg_lines)

download_img("F:/npx0509_3", "F:/pos_test/", "F:/neg_test/")
