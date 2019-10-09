#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer

    with tf.name_scope(layer_name):
        with tf.name_scope('input'):
            Weight = tf.Variable(tf.random_normal(
                [in_size, out_size]), name='W')
            tf.summary.histogram(layer_name + '/weights', Weight)
        with tf.name_scope('biase'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='biase')
            tf.summary.histogram(layer_name + '/biases', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weight) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs


def main():
    x_data = np.linspace(-2, 2, num=3000)[:, np.newaxis]  # 300行
    noise = np.random.normal(0, 0.05, x_data.shape)
    y_data = np.square(x_data) - 0.5 + noise

    with tf.name_scope('input'):
        xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
        ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

    ly1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)
    predition = add_layer(ly1, 10, 1, n_layer=2, activation_function=None)

    # 比较预测值与实际值的差别 reduction_indices
    with tf.name_scope('loss'):
        loss = tf.reduce_mean(tf.reduce_sum(
            tf.square(ys - predition), reduction_indices=[1]))
        tf.summary.scalar('loss', loss)
    with tf.name_scope('train'):
        train_step = tf.train.GradientDescentOptimizer(
            0.1).minimize(loss)  # 0.1 学习效率
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        merged = tf.summary.merge_all()
        writer = tf.summary.FileWriter('/tmp/b', sess.graph)
        sess.run(init)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(x_data, y_data)
        plt.ion()
        plt.show()
        for i in range(100000):
            sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
            if i % 50 == 0:
                # print(i, sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
                try:
                    ax.lines.remove(lines[0])
                except Exception:
                    pass
                predition_value = sess.run(predition, feed_dict={xs: x_data})
                lines = ax.plot(x_data, predition_value, "r-", lw=5)
                plt.pause(0.1)
                result = sess.run(merged, feed_dict={xs: x_data, ys: y_data})
                writer.add_summary(result, i)

if __name__ == '__main__':
    main()
    print("over...")
