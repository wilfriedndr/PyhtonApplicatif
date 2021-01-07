"""
Basic layout with PyQt
"""

import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("my pyQt app")

		self.setLayout(qtw.QHBoxLayout())

		self.btn = qtw.QPushButton("btn Push Button")
		self.layout().addWidget(self.btn)

		self.layout().addWidget(qtw.QPushButton("Press me"))
		self.layout().addWidget(qtw.QPushButton("Press me"))
		self.layout().addWidget(qtw.QPushButton("Press me"))

		self.show()

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
