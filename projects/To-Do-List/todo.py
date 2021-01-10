import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as qtw


qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
tick = QtGui.QImage('tick.png')


class TodoModel(QtCore.QAbstractListModel):
	def __init__(self, *args, todos=None, **kwargs):
		super(TodoModel, self).__init__(*args, **kwargs)
		self.todos = todos or []
		
	def data(self, index, role):
		if role == Qt.DisplayRole:
			_, text = self.todos[index.row()]
			return text
		
		if role == Qt.DecorationRole:
			status, _ = self.todos[index.row()]
			if status:
				return tick

	def rowCount(self, index):
		return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.setLayout(qtw.QVBoxLayout())
		self.setWindowTitle("To-Do-List !")
		self.model = TodoModel()
		self.load()
		self.todoView.setModel(self.model)
		self.addButton.pressed.connect(self.add)
		self.deleteButton.pressed.connect(self.delete)
		self.completeButton.pressed.connect(self.complete)

		todoContainer = qtw.QWidget()
		todoContainer.setLayout(qtw.QHBoxLayout())

	def add(self):
		text = self.todoEdit.text()
		if text:

			self.model.todos.append((False, text))      
			self.model.layoutChanged.emit()
			self.todoEdit.setText("")
			self.save()
		
	def delete(self):
		indexes = self.todoView.selectedIndexes()
		if indexes:
			index = indexes[0]
			del self.model.todos[index.row()]
			self.model.layoutChanged.emit()
			self.todoView.clearSelection()
			self.save()
			
	def complete(self):
		indexes = self.todoView.selectedIndexes()
		if indexes:
			index = indexes[0]
			row = index.row()
			status, text = self.model.todos[row]
			self.model.todos[row] = (True, text)
			self.model.dataChanged.emit(index, index)
			self.todoView.clearSelection()
			self.save()
	
	def load(self):
		try:
			with open('history.txt', 'r') as f:
				self.model.todos = json.load(f)
		except Exception:
			pass

	def save(self):
		with open('history.txt', 'w') as f:
			data = json.dump(self.model.todos, f)


app = QtWidgets.QApplication(sys.argv)
app.setStyle(qtw.QStyleFactory.create('Fusion'))
window = MainWindow()
window.show()
app.exec_()


