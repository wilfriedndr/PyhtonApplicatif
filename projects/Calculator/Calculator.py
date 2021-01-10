import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator !")
		self.setLayout(qtw.QVBoxLayout())
		self.setUI()

		self.show()

	def setUI(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		# Creating the buttons
		self.label = qtw.QLineEdit()

		push_equal = qtw.QPushButton('Enter')
		push_equal.clicked.connect(self.action_equal)

		push_clear = qtw.QPushButton('Clear')
		push_clear.clicked.connect(self.action_clear)
		
		push1 = qtw.QPushButton('1')
		push1.clicked.connect(self.action1)

		push2 = qtw.QPushButton('2')
		push2.clicked.connect(self.action2)

		push3 = qtw.QPushButton('3')
		push3.clicked.connect(self.action3)

		push4 = qtw.QPushButton('4')
		push4.clicked.connect(self.action4)

		push5 = qtw.QPushButton('5')
		push5.clicked.connect(self.action5)

		push6 = qtw.QPushButton('6')
		push6.clicked.connect(self.action6)

		push7 = qtw.QPushButton('7')
		push7.clicked.connect(self.action7)

		push8 = qtw.QPushButton('8')
		push8.clicked.connect(self.action8)

		push9 = qtw.QPushButton('9')
		push9.clicked.connect(self.action9)

		push0 = qtw.QPushButton('0')
		push0.clicked.connect(self.action0)
		

		push_plus = qtw.QPushButton('+')
		push_plus.clicked.connect(self.action_plus)

		push_minus = qtw.QPushButton('-')
		push_minus.clicked.connect(self.action_minus)

		push_mul = qtw.QPushButton('*')
		push_mul.clicked.connect(self.action_mul)

		push_div = qtw.QPushButton('/')
		push_div.clicked.connect(self.action_div)


		# Add buttons to layout
		container.layout().addWidget(self.label, 0, 0, 1, 4)

		container.layout().addWidget(push_equal, 1, 0, 1, 2)
		container.layout().addWidget(push_clear, 1, 2, 1, 2)

		container.layout().addWidget(push7,2, 0 )
		container.layout().addWidget(push8,2, 1 )
		container.layout().addWidget(push9,2, 2 )
		container.layout().addWidget(push_plus,2, 3 )

		container.layout().addWidget(push4,3, 0 )
		container.layout().addWidget(push5,3, 1 )
		container.layout().addWidget(push6,3, 2 )
		container.layout().addWidget(push_minus,3, 3 )

		container.layout().addWidget(push1,4, 0 )
		container.layout().addWidget(push2,4, 1 )
		container.layout().addWidget(push3,4, 2 )
		container.layout().addWidget(push_mul,4, 3 )

		container.layout().addWidget(push0,5,0, 1, 3 )
		container.layout().addWidget(push_div,5, 3 )

		self.layout().addWidget(container)
	
	
	def action_equal(self):
		equation = self.label.text()
  
		try:
			ans = eval(equation)
			self.label.setText(str(ans))
  
		except:
			self.label.setText("Wrong Input")
  
	def action_plus(self):
		text = self.label.text() 
		self.label.setText(text + " + ") 
  
	def action_minus(self):
		text = self.label.text() 
		self.label.setText(text + " - ") 
  
	def action_div(self):
		text = self.label.text() 
		self.label.setText(text + " / ") 
  
	def action_mul(self):
		text = self.label.text() 
		self.label.setText(text + " * ") 
  
	def action_point(self):
		text = self.label.text() 
		self.label.setText(text + ".") 
  
	def action0(self):
		text = self.label.text() 
		self.label.setText(text + "0") 
  
	def action1(self):
		text = self.label.text() 
		self.label.setText(text + "1") 
  
	def action2(self):
		text = self.label.text() 
		self.label.setText(text + "2") 
  
	def action3(self):
		text = self.label.text() 
		self.label.setText(text + "3") 
  
	def action4(self):
		text = self.label.text() 
		self.label.setText(text + "4") 
  
	def action5(self):
		text = self.label.text() 
		self.label.setText(text + "5") 
  
	def action6(self): 
		text = self.label.text() 
		self.label.setText(text + "6") 
  
	def action7(self):
		text = self.label.text() 
		self.label.setText(text + "7") 
  
	def action8(self):
		text = self.label.text() 
		self.label.setText(text + "8") 
  
	def action9(self): 
		text = self.label.text() 
		self.label.setText(text + "9") 
  
	def action_clear(self): 
		self.label.setText("") 

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()