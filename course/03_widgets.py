"""
Widgets examples with PyQt
"""

import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("my pyQt app")

		self.setLayout(qtw.QVBoxLayout())
		
		self.layout().addWidget(qtw.QLineEdit())
		self.layout().addWidget(qtw.QPushButton("Button"))
		self.layout().addWidget(qtw.QTextEdit("hello"))
		self.layout().addWidget(qtw.QLabel("This is a label"))
		
		self.checkbox = qtw.QCheckBox()
		self.checkbox.stateChanged.connect(self.checkboxStateChanged)

		self.layout().addWidget(self.checkbox)
		
		combobox = qtw.QComboBox(self)

		combobox.addItem("Choice 1")
		combobox.addItem("Choice 2")
		combobox.addItem("Choice 3")
		combobox.addItem("Choice 5")

		self.layout().addWidget(combobox)


		self.show()
	
	def checkboxStateChanged(self, state):
		print(self.checkbox.isChecked())


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
