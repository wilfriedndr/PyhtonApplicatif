"""
Example of a basic calculation app
"""

import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("my pyQt app")

		self.setLayout(qtw.QHBoxLayout())

		self.setUI()

		self.show()
	
	def setUI(self):

		self.input1 = qtw.QLineEdit()
		self.layout().addWidget(self.input1)
		self.layout().addWidget(qtw.QLabel("+"))
		self.input2 = qtw.QLineEdit()
		self.layout().addWidget(self.input2)

		self.btn = qtw.QPushButton("=", clicked = self.onClick)
		self.layout().addWidget(self.btn)

		self.resLabel = qtw.QLabel()
		self.layout().addWidget(self.resLabel)
	
	def onClick(self):
		num1 = int(self.input1.text())
		num2 = int(self.input2.text())
		self.resLabel.setText(str(num1 + num2))

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
