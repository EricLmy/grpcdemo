# -*- coding:utf-8 -*- 
# 

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import QTimer
if __name__ == '__main__':
    from usb1_ui import Ui_Form
else:
    from windows.usb1_ui import Ui_Form

import cv2

class usb1Windows(QWidget):
    def __del__(self):
        self.camera.release()# 释放资源

    def init_fun(self):
        self.window = Ui_Form()
        self.window.setupUi(self)

        self.timer = QTimer()# 定义一个定时器对象
        self.timer.timeout.connect(self.timer_fun) #计时结束调用方法

        # 1. open usb and show
        self.window.pushButton_2.clicked.connect(self.timer_start)
        # 2. catch one picture
        self.window.pushButton.clicked.connect(self.catch_picture)

    def catch_picture(self):
        ret, frame = self.camera.read()
        if ret:
            b, g, r = cv2.split(frame)
            imgret = cv2.merge([r,g,b])
            self.window.pic_figaxes.clear()
            self.window.pic_figaxes.imshow(imgret)
            self.window.pic_figure.canvas.draw()
        else:
            pass # get faild

    def timer_fun(self):
        ret, frame = self.camera.read()
        if ret:
            self.showimg2figaxes(frame)
        else:
            self.timer.stop()

    def timer_start(self):
        self.camera = cv2.VideoCapture(0)
        # get 
        print(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(self.camera.get(cv2.CAP_PROP_FPS))
        print(self.camera.get(cv2.CAP_PROP_BRIGHTNESS))
        print(self.camera.get(cv2.CAP_PROP_CONTRAST))
        print(self.camera.get(cv2.CAP_PROP_HUE))
        print(self.camera.get(cv2.CAP_PROP_EXPOSURE))
        
        self.timer.start(41) #设置计时间隔并启动

    def showimg2figaxes(self,img):
        b, g, r = cv2.split(img)
        imgret = cv2.merge([r,g,b])# 这个就是前面说书的，OpenCV和matplotlib显示不一样，需要转换
        self.window.video_figaxes.clear()
        self.window.video_figaxes.imshow(imgret)
        # self.window.video_figaxes.autoscale_view()
        self.window.video_figure.canvas.draw()


if __name__ == '__main__':
    
    import sys
    app = QApplication(sys.argv)
    mainW = QMainWindow()
    ui = usb1Windows(mainW)
    ui.init_fun()
    mainW.show()
    sys.exit(app.exec_())