import PyQt5.QtWidgets as qtw

initial_todos = [
			{
				"title": "Faire les courses",
				"state": False,
			},
			{
				"title": "Réviser les cours",
				"state": False
			},
			{
				"title": "Méditation",
				"state": True
			}
		]

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()

		self.todos = initial_todos  # Load from file

		self.setWindowTitle("my pyQt app")
		self.setLayout(qtw.QVBoxLayout())

		self.setTodos()

		self.show()

	def setTodos(self):
		# for todo in self.todos:
		for i in range(len(self.todos)):
			todo = self.todos[i]
			# container
			todoContainer = qtw.QWidget()
			todoContainer.setLayout(qtw.QHBoxLayout())

			#checkbox
			checkbox = qtw.QCheckBox()
			checkbox.setChecked(todo["state"])
			todoContainer.layout().addWidget(checkbox)
			self.todos[i]["checkbox"] = checkbox
			checkbox.stateChanged.connect(self.checkboxStateChanged)

			# label
			label = qtw.QLabel(todo["title"])
			todoContainer.layout().addWidget(label)

			self.layout().addWidget(todoContainer)

	def checkboxStateChanged(self):
		for i in range(len(self.todos)):
			if (self.todos[i]["checkbox"]):
				self.todos[i]["state"] = self.todos[i]["checkbox"].isChecked()
		
		# Save to file
		print(self.todos)

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()