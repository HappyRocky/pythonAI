from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) # 读取数据集
sess = tf.InteractiveSession() # 创建session

# 正态分布
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)
#创建一个结构为shape的矩阵
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)
# 卷积遍历个方向步数为1，SAME：外边缘自动补0，遍历相乘
def conv2d(x,W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')
# 池化卷积结果，池华层采用kernel的大小2x2，步数也为2，周围补0，取最大值
def max_poll_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

xs = tf.placeholder(tf.float32,[None, 28*28])
ys = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)
x_image = tf.reshape(xs, [-1,28,28,1])