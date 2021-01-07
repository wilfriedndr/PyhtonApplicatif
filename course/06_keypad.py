
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("my pyQt app")
		self.setLayout(qtw.QVBoxLayout())
		self.setUI()

		self.show()

	def setUI(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		# create the buttons
		btn_1 = qtw.QPushButton('1')
		btn_2 = qtw.QPushButton('2')
		btn_3 = qtw.QPushButton('3')
		btn_4 = qtw.QPushButton('4')
		btn_5 = qtw.QPushButton('5')
		btn_6 = qtw.QPushButton('6')
		btn_7 = qtw.QPushButton('7')
		btn_8 = qtw.QPushButton('8')
		btn_9 = qtw.QPushButton('9')
		btn_0 = qtw.QPushButton('0', clicked = self.onClick)

		


		# add buttons to layout
		container.layout().addWidget(btn_7,0, 0 )
		container.layout().addWidget(btn_8,0, 1 )
		container.layout().addWidget(btn_9,0, 2 )

		container.layout().addWidget(btn_4,1, 0 )
		container.layout().addWidget(btn_5,1, 1 )
		container.layout().addWidget(btn_6,1, 2 )

		container.layout().addWidget(btn_1,2, 0 )
		container.layout().addWidget(btn_2,2, 1 )
		container.layout().addWidget(btn_3,2, 2 )

		container.layout().addWidget(btn_0,4,0, 1, 3 )


		self.layout().addWidget(container)
	
	def onClick(self):
		qtw.QMessageBox.about(self, "HELLO", "test")

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
