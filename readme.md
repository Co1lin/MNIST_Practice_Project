# Demo
https://www.bilibili.com/video/av88086690/  
Blog：https://blog.valderfield.com/archives/17/  

# Summary

A handwriting number recognizer based on TensorFlow.  

MNIST is the "`Hello, World`" in machine learning. I add an drawingboard, although it doesn't work fluently.  

# Usage

Run `demo1.py` in the directory within python3, TensorFlow 2 environment. Then you can write number on the drawingboard. Every time the left button of your mouse up, the program will recognize the image on the board as a number, and print the result in the terminal. Press ESC to quit the program, and press C to clear the drawingboard.  

# More Detail

`demo1.py` imports `drawingboard.py`(the drawingboard UI) and `ml.py`(which includes the machine learning model using the trained model file "`my_model_eproch_5.h5`" or "`my_model.h5`").  

If you want to train the model by yourself, you can run `train.py` on your own computer or on the CoLab by Google. You may learn how to copy the trained model to your Google Drive if you choose the last one.  

`img2arr.py` is a program that converts an image into an array which is the input of the neural network. It is intergreted into `ml.py` as a method.  
