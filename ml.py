from __future__ import absolute_import, division, print_function, unicode_literals
import cv2
import tensorflow as tf
from tensorflow import keras

class MachineLearning(object):

    def __init__(self, model_path = 'my_model.h5'):
        print("Load saved model...")
        self.img_to_test = 'img_to_test'
        self.img_type = 'img_type'
        self.img_inverse = False
        print('TensorFlow version: ', tf.version.VERSION)
        (self.train_images, self.train_labels), (self.test_images, self.test_labels) = tf.keras.datasets.mnist.load_data()
        self.train_images = self.train_images.reshape(-1, 28 * 28) / 255.0
        self.test_images = self.test_images.reshape(-1, 28 * 28) / 255.0
        # 重新创建完全相同的模型，包括其权重和优化程序
        self.model = keras.models.load_model(model_path)
        # 显示网络结构
        self.model.summary()

    def test_accuracy(self):
        print("Test accuracy...")
        loss, acc = self.model.evaluate(self.test_images, self.test_labels, verbose=2)
        print("Restored model, accuracy: {:5.2f}%".format(100 * acc))

    def set_img(self, img_to_test, img_type, img_inverse = True):
        print("Set image...")
        self.img_to_test = img_to_test
        self.img_type = img_type
        self.img_inverse = img_inverse

    def __img_pre_process(self, preview):
        print("Pre-process the image...")
        if self.img_type is 'image':
            img = cv2.imread(self.img_to_test)
        elif self.img_type is 'array':
            img = self.img_to_test
        # convert BGR img to GRAY img: Using cv2.cvtColor(src, code)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # erode (an optimization)
        # img = cv2.erode(img, None, iterations=1)
        # resize the img to 28*28 which MNIST required
        img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_CUBIC)  # interpolation 插值方法
        # binaryzation: color <= 160 --> 0, black
        if self.img_inverse:
            ret, img = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)  # return threshold value 160 to ret
            img = 255 - img  # invert the color (black background and white text to fit the data of MNIST!!!)
        else:
            ret, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
        if preview:
            window_name = 'Processed image. Press any key to continue.'
            cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
            # cv2.startWindowThread()
            cv2.imshow(window_name, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # add batch dimension before dim0 and reshape to [1, 28 * 28]
        img = tf.reshape(img, [-1, 28 * 28])
        img = tf.cast(img, dtype = tf.float32)  # convert the data type from integer to float
        img /= 255  # normalization
        return img

    def predict(self, preview):
        print("Predict...")
        img_arr = self.__img_pre_process(preview)
        pred = self.model.predict_classes(img_arr)
        return pred

if __name__ == '__main__':
    ml = MachineLearning('my_model_eproch_5.h5')
    ml.set_img('6.png', 'image', True)
    ml.test_accuracy()
    res = ml.predict()
    print('Result: ', res)