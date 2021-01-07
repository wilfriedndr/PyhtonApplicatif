"""
Initialize a window with PyQt
"""

import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("my pyQt app")
		self.show()

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
