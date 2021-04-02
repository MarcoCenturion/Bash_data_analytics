import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic 

class Dialogo(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("membresias.ui",self)
		self.boton.clicked.connect(self.getItem)

	def getItem(self):
		yr = self.years2.currentText()
		week = self.weeks.currentText()
		self.seleccionado.setText("Años elegidos"+yr+week)


app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()