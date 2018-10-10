# -*- coding:utf-8 -*- 
# 

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer
if __name__ == '__main__':
    from usb1_ui import Ui_Form
else:
    from windows.usb1_ui import Ui_Form

import cv2
import copy

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

        self.window.comboBox.currentIndexChanged.connect(self.set_width_and_height)

        self.window.pushButton_5.clicked.connect(self.preview_picture)
        self.window.pushButton_4.clicked.connect(self.save_picture)

    def save_picture(self):
        if hasattr(self, 'preview_res'):
            tmp_save_picture = self.preview_res
        else:
            if hasattr(self, 'raw_frame'):
                tmp_save_picture = self.raw_frame
            else:
                return # no pic
        cv2.imwrite("./image/save.jpg", tmp_save_picture)
        # filename, filetype = QFileDialog.getSaveFileName(self, "save", "jpg Files(*.jpg)::All Files(*)")
        # if filename:
        #     cv2.imwrite(filename, tmp_save_picture)

    def preview_picture(self):
        if hasattr(self, 'raw_frame'):
            width = self.window.spinBox.value()
            height = self.window.spinBox_2.value()
            # self.raw_frame.reszie((width, height))
            self.preview_res = cv2.resize(self.raw_frame, (width, height), interpolation=cv2.INTER_CUBIC)
            self.showimg2figaxes2(self.preview_res)


    def set_width_and_height(self):
        # print(self.window.comboBox.currentText())
        width, height = self.window.comboBox.currentText().split('*')
        if hasattr(self, "camera"):
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, int(width))
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, int(height))

    def catch_picture(self):
        if hasattr(self, "camera") and self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                self.raw_frame = copy.deepcopy(frame)
                self.showimg2figaxes2(frame)
            else:
                pass # get faild

    def timer_fun(self):
        ret, frame = self.camera.read()
        if ret:
            self.showimg2figaxes(frame)
        else:
            self.timer.stop()

    def timer_start(self):
        if hasattr(self, "camera"):
            if not self.camera.isOpened():
                self.camera.open(0)
                # self.camera = cv2.VideoCapture(0)
        else:
            self.camera = cv2.VideoCapture(0)
        if self.camera.isOpened():
            pass
        else:
            self.camera.open(0)
        # get 
        width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        print(width)
        height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(int(height))
        self.window.comboBox.setCurrentText("%d*%d" % (int(width), int(height)))

        fps = self.camera.get(cv2.CAP_PROP_FPS)
        if fps == float('inf'):
            pass
        else:
            print(fps)

        brightness = self.camera.get(cv2.CAP_PROP_BRIGHTNESS)
        if brightness == float('inf'):
            self.window.doubleSpinBox_2.setValue(0.0)
        else:
            self.window.doubleSpinBox_2.setValue(brightness)

        contrast = self.camera.get(cv2.CAP_PROP_CONTRAST)
        if contrast == float('inf'):
            self.window.doubleSpinBox.setValue(0.0)
        else:
            self.window.doubleSpinBox.setValue(contrast)

        hue = self.camera.get(cv2.CAP_PROP_HUE)
        if hue == float('inf'):
            self.window.doubleSpinBox_3.setValue(0.0)
        else:
            self.window.doubleSpinBox_3.setValue(hue)

        exposure =self.camera.get(cv2.CAP_PROP_EXPOSURE) 
        if exposure == float('inf'):
            self.window.doubleSpinBox_4.setValue(0.0)
        else:
            self.window.doubleSpinBox_4.setValue(exposure) # inf

        saturation =self.camera.get(cv2.CAP_PROP_SATURATION) 
        if saturation == float('inf'):
            self.window.doubleSpinBox_5.setValue(0.0)
        else:
            self.window.doubleSpinBox_5.setValue(saturation) # inf
    
        self.timer.start(41) #设置计时间隔并启动

    def showimg2figaxes2(self, frame):
        b, g, r = cv2.split(frame)
        imgret = cv2.merge([r,g,b])
        self.window.pic_figaxes.clear()
        self.window.pic_figaxes.imshow(imgret)
        self.window.pic_figure.canvas.draw()

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