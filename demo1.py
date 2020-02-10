from __future__ import absolute_import, division, print_function, unicode_literals
import threading
import cv2
import tensorflow as tf
from tensorflow import keras
import drawingboard, ml

def test():
    model = ml.MachineLearning('6.png', 'image', True, 'my_model.h5')
    model.test_accuracy()
    res = model.predict()
    print(res)

if __name__ == '__main__':

    model = ml.MachineLearning('my_model_eproch_5.h5')
    board = drawingboard.DrawingBoard()

    def model_thread():
        last_report_id = board.report_id
        while True:
            if (last_report_id != board.report_id):
                #print(last_report_id, board.report_id)
                model.set_img(board.img, 'array', False)
                res = model.predict(preview=False)
                print('*** Result: ', int(res), ' ***')
                last_report_id = board.report_id
            if board.quited is True:
                break

    thread1 = threading.Thread(target=model_thread)
    thread1.start()

    board.start()
