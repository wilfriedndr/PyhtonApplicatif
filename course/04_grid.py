"""
Layout grid with PyQt
"""


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

		container.layout().addWidget(qtw.QLabel("top-left"), 0,0)
		container.layout().addWidget(qtw.QLabel("top"), 0,1)
		container.layout().addWidget(qtw.QLabel("right"), 0,2)
		container.layout().addWidget(qtw.QLabel("left"), 1,0)
		container.layout().addWidget(qtw.QLabel("center"), 1,1)
		container.layout().addWidget(qtw.QLabel("right"), 1,2)
		container.layout().addWidget(qtw.QLabel("bottom-left"), 2,0)
		container.layout().addWidget(qtw.QLabel("bottom"), 2,1)
		container.layout().addWidget(qtw.QLabel("bottom-right"), 2,2)
		
		container.layout().addWidget(qtw.QLabel(" ---------- LAST ROW --------- "),4, 0, 1, 3 )

		self.layout().addWidget(container)

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
