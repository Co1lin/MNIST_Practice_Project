import cv2
import tensorflow as tf

def img2arr(img_path):
    img = cv2.imread(img_path)
    # convert BGR img to GRAY img: Using cv2.cvtColor(src, code)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # erode (an optimization)
    img = cv2.erode(img, None, iterations=4)
    # resize the img to 28*28 which MNIST required
    img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_CUBIC)  # interpolation 插值方法
    # binaryzation: color <= 160 --> 0, white
    ret, img = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)  # return threshold value 160 to ret
    img = 255 - img # invert the color (black background and white text to fit the data of MNIST!!!)
    # add batch dimension before dim0 and reshape to [1, 28 * 28]
    img_arr = tf.reshape(img, [-1, 28 * 28])
    img_arr = tf.cast(img_arr, dtype=tf.float32)  # convert the data type from integer to float
    img_arr /= 255  # normalization
    return img_arr

#print(img2arr('num2.jpg'))

if __name__ == '__main__':
    img2arr('1.png')