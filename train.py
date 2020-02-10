from __future__ import absolute_import, division, print_function, unicode_literals

import os
# %tensorflow_version 2.x   # use it in CoLab
import tensorflow as tf
from tensorflow import keras
print(tf.version.VERSION)

# 定义一个简单的序列模型
def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
  ])

  model.compile(optimizer='adam',   # 优化器
                loss='sparse_categorical_crossentropy', # 损失采用交叉熵
                metrics=['accuracy'])   # 指标采用准确率
  return model


(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_images = train_images.reshape(-1, 28 * 28) / 255.0
test_images = test_images.reshape(-1, 28 * 28) / 255.0

# 创建一个基本的模型实例
model = create_model()
# 显示模型的结构
model.summary()
# 训练模型
model.fit(train_images, train_labels, epochs=5)
# 将整个模型保存为HDF5文件
model.save('my_model_eproch_5.h5')