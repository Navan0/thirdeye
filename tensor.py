import time
import tensorflow as tf
hello=tf.constant('hello')
sess=tf.Session()
sess.run(hello)
time.sleep(5)
