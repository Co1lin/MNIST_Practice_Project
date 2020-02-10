import threading
import time
import numpy as np
import cv2

class DrawingBoard(object):

    def __init__(self):
        print("Initializing drawing board...")
        self.window_name = 'Drawing Board'
        cv2.namedWindow(self.window_name, cv2.WINDOW_AUTOSIZE)
        #cv2.startWindowThread()
        # create an image array
        self.img = np.zeros([256, 256, 3], dtype = np.uint8)
        # create trackbar for setting colors
        cv2.createTrackbar('R', self.window_name, 255, 255, self.nothing)
        cv2.createTrackbar('G', self.window_name, 255, 255, self.nothing)
        cv2.createTrackbar('B', self.window_name, 255, 255, self.nothing)
        cv2.createTrackbar('Thickness', self.window_name, 20, 40, self.nothing)
        cv2.rectangle(self.img, (40, 40), (215, 215), (0, 190, 0))
        # set parameters
        self.drawing = False
        self.x_last, self.y_last = -1, -1
        self.report_id = 0
        self.quited = False

        if 0:
            cv2.imshow(self.window_name, self.img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def nothing(self, x):
        pass

    def drawCircle(self, event, x, y, flags, param):
        r = cv2.getTrackbarPos('R', self.window_name)
        g = cv2.getTrackbarPos('G', self.window_name)
        b = cv2.getTrackbarPos('B', self.window_name)
        thickness = cv2.getTrackbarPos('Thickness', self.window_name)
        radius = thickness / 2
        color = (b, g, r)
        # correspond the event
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.x_last, self.y_last = x, y
        elif event == cv2.EVENT_MOUSEMOVE and self.drawing:
            if self.x_last != -1:   # draw line
                cv2.line(self.img, (self.x_last, self.y_last), (x, y), color, thickness)
                self.x_last, self.y_last = x, y
            cv2.circle(self.img, (x, y), int(radius), color, thickness = -1)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.x_last = self.y_last = -1
            self.report_id += 1

    def clear(self):
        self.img = np.zeros([256, 256, 3], dtype=np.uint8)
        cv2.rectangle(self.img, (40, 40), (215, 215), (0, 190, 0))

    def start(self):
        print("Drawing Board start working...")
        cv2.setMouseCallback(self.window_name, self.drawCircle)
        while True:
            #print(self.report_id)
            cv2.imshow(self.window_name, self.img)
            key = cv2.waitKey(1)
            if key is 99:   # C
                self.clear()
            elif key is 27:   # esc
                break
        # end While
        cv2.destroyAllWindows()
        #return self.img
        self.quited = True

class BoardThread(threading.Thread):
    def __init__(self):
        super(BoardThread, self).__init__()
        self.board = DrawingBoard()

    def run(self):
        self.board.start()

if __name__ == '__main__':
    board = DrawingBoard()
    board.start()