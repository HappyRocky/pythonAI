# -*- coding: utf-8 -*-

# 引入 word2vec
from gensim.models import word2vec

# 引入日志配置
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 引入数据集
raw_sentences = ["the quick brown fox jumps over the lazy dogs","yoyoyo you go home now to sleep"]

# 切分词汇
sentences= [s.split() for s in raw_sentences]


# 构建模型
#model = word2vec.Word2Vec(sentences, min_count=1)
model = word2vec.Word2Vec(sentences, size=100, window=2, min_count=1)


model.save('outp1')
model.wv.save_word2vec_format('outp2', binary=False)



# 进行相关性比较
print(model.wv.similarity('home','go'))
print(model.wv.__getitem__('jumps'))