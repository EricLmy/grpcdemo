# -*- coding:utf-8 -*- 
# 

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

if __name__ == '__main__':
	from demo1_ui import Ui_Form
else:
	from windows.demo1_ui import Ui_Form
class demo1Windows(QWidget):
	def init_fun(self):
		self.window = Ui_Form()
		self.window.setupUi(self)

	def closeEvent(self, event):
		print("demo1111")
		event.accept()


if __name__ == '__main__':
	
	import sys
	app = QApplication(sys.argv)
	mainW = QMainWindow()
	ui = demo1Windows(mainW)
	ui.init_fun()
	mainW.show()
	sys.exit(app.exec_())