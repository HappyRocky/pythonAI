from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
print("开始读取数据")
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) # 读取数据集
sess = tf.InteractiveSession() # 创建session
print("数据读取完毕")

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

# 第一层卷积
W_conv1 = weight_variable([5,5,1,32]) # 前两个参数为卷积核大小，第三个为图像通道数，第四个是卷积核的数目
b_conv1 = bias_variable([32]) # 每一个卷积核都有一个偏置量
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1) # 图片乘以卷积核，再加上偏置量，卷积结果28x28x32
h_pool1 = max_poll_2x2(h_conv1) # 池化结果 14x14x32

# 第二层卷积
w_conv2 = weight_variable([5,5,32,64]) # 上一层的卷积核数目作为这一层的通道数
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2) + b_conv2) # 卷积结果 14x14x64
h_pool2 = max_poll_2x2(h_conv2) # 池化结果 7x7x64

# 第三层全连接
W_fc1 = weight_variable([7*7*64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64]) # [n_samples, 7, 7, 64] ==> [n_samples, 7*7*64]
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1) # 

# dropout操作
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 第四层输出
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# 定义loss
cross_entry = -tf.reduce_sum(ys * tf.log(y_conv))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(cross_entry)

# 训练和预测
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(ys, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
tf.global_variables_initializer().run()
for i in range(2000):
    batch = mnist.train.next_batch(50)
    if i%100 == 0:
        train_accuracy = accuracy.eval(feed_dict={xs:batch[0],ys:batch[1], keep_prob:1.0})
        print("step %d, training accuracy %g"%(i, train_accuracy))
    train_step.run(feed_dict={xs:batch[0], ys:batch[1],keep_prob:0.5})
print("test accuracy %g"%accuracy.eval(feed_dict={xs:mnist.test.images,ys:mnist.test.labels,keep_prob:1.0}))




 