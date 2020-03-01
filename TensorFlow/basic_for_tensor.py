#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf

# 创建一个常量运算，将作为一个节点加入到默认计算图中
hello = tf.constant("Hello World!")

# 创建一个tf对话
sess = tf.compat.v1.Session()

# 运行并获得最后结果
print(sess.run(hello))


# In[3]:


# a simple one
node1 = tf.constant(3.0, tf.float32, name = "node1")
node2 = tf.constant(4.0, tf.float32, name = "node2")
node3 = tf.add(node1, node2)


# In[4]:


print(node3)


# In[5]:


print(node1)


# In[6]:


# 建立对话并显示运算结果
sess = tf.Session()
print("运行sess.run(node1)的结果：", sess.run(node1))


# In[8]:


# 建立对话并显示运算结果
print("运行sess.run(node3)的结果：", sess.run(node3))

# 关闭session
sess.close()


# In[10]:


import tensorflow as tf
tens1 = tf.constant([1,2,3])

# 创建会话
sess = tf.Session()
try:
    print(sess.run(tens1))
except:
    print("Exception!")
finally:
    # 关闭会话
    sess.close()


# In[11]:


node1 = tf.constant(3.0, tf.float32, name = "node1")
node2 = tf.constant(4.0, tf.float32, name = "node2")
node3 = tf.add(node1, node2)

# 创建会话通过Python的上下文管理器来管理会话
with tf.Session() as sess:
    # 使用这个会话来计算关心的结果
    print(sess.run(node3))


# In[13]:


node1 = tf.constant(3.0, tf.float32, name = "node1")
node2 = tf.constant(4.0, tf.float32, name = "node2")
node3 = tf.add(node1, node2)

sess = tf.Session()
with sess.as_default():
    # 使用这个会话来计算关心的结果
    print(node3.eval())


# In[21]:


node1 = tf.Variable(3.0, tf.float32, name = "node1")
node2 = tf.Variable(4.0, tf.float32, name = "node2")
node3 = tf.add(node1, node2, name = "add")
sess = tf.Session()

# 变量初始化
init = tf.global_variables_initializer()

sess.run(init)
print(sess.run(node3))
sess.close()

