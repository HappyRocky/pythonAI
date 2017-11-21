from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import time
import data_helpers

beginTime = time.time();

# parameter definitions
batch_size = 100
learning_rate = 0.005
max_steps = 5000

# prepare data
data_sets = data_helpers.load_data()

# define input placeholders
images_placeholder = tf.placeholder(tf.float32, shape=[None, 3072])
labels_placeholder = tf.placeholder(tf.int64, shape=[None])

# define variables 
weights = tf.Variable(tf.zeros([3072,10]))
biases = tf.Variable(tf.zeros([10]))

# define classifier's result
logits = tf.matmul(images_placeholder, weights) + biases

# define the loss function
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=labels_placeholder))

# define the training operation
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

# operation comparing prediction with true label
correct_prediction = tf.equal(tf.argmax(logits, 1), labels_placeholder)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# run
with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    for i in range(max_steps):
        indices = np.random.choice(data_sets['images_train'].shape[0], batch_size)
        images_batch = data_sets['images_train'][indices]
        labels_batch = data_sets['labels_train'][indices]
        if i % 100 == 0:
            train_accuracy = sess.run(accuracy,feed_dict={images_placeholder:images_batch,labels_placeholder:labels_batch})
            print('Step {:5d}:training accuracy {:g}'.format(i, train_accuracy))
        sess.run(train_step, feed_dict={images_placeholder:images_batch,labels_placeholder:labels_batch})
    
    # after finishing the training, evaluate on the test set
    test_accuracy = sess.run(accuracy, feed_dict={images_placeholder:data_sets['images_test'],labels_placeholder:data_sets['labels_test']})
    print('Test accuracy {:g}'.format(test_accuracy))

endTime = time.time()
print('Total time:{:5.2}s'.format(endTime - beginTime))

