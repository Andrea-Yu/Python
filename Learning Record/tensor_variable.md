```python
import tensorflow as tf
a = tf.placeholder(tf.float32, name = "a")
b = tf.placeholder(tf.float32, name = "b")
c = tf.multiply(a, b, name = "c")

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    result = sess.run(c, feed_dict = {a:8.0, b:3.0})
    
    print(result)
```

    24.0
    


```python
import tensorflow as tf
tf.reset_default_graph()
logdir = "C:\TensorFlow\log"
input1 = tf.constant([1.0, 2.0, 3.0], name="input1")
input2 = tf.Variable(tf.random_uniform([3]), name="input2")
output = tf.add_n([input1, input2], name="add")
writer = tf.summary.FileWriter(logdir, tf.get_default_graph())
writer.close()
```
