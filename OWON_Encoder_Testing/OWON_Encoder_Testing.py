import sys
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QHBoxLayout, QGroupBox, QComboBox, QLabel, QTextEdit
from PyQt5.QtGui import QIcon
 
from Plots import PlotCanvas
from usb import usbManager
 
class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.left = 50
		self.top = 50
		self.title = 'Virtual Scope'
		self.width = 800
		self.height = 400
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		#self.init_menuBar()

		# init widgets
		deviceSelectorLabel = QLabel("Device:")
		deviceSelector = QComboBox()
		scopeValue = QTextEdit("0")
		scopeValue.setReadOnly(True)
		scopeValueLabel = QLabel("Value")
		#graphGroup = QGroupBox("Scope")
		#ControlsGroup = QGroupBox("Controls")

		 #matplotlib in action
		m = PlotCanvas(self, width=6, height=1)
		m.move(50,50)

		# init layouts
		hBox = QHBoxLayout()
		hBox.setContentsMargins(20,10,10,10)
		controlsVBox = QVBoxLayout()
		controlsVBox.setContentsMargins(10,0,10,0)
		controlsVBox.addWidget(deviceSelectorLabel)
		controlsVBox.addWidget(deviceSelector)
		controlsVBox.addStretch(1)
		controlsVBox.addWidget(scopeValueLabel)
		controlsVBox.addWidget(scopeValue)
		controlsVBox.addStretch(10)
		hBox.addWidget(m)
		hBox.addLayout(controlsVBox)

		#button = QPushButton('PyQt5 button', self)
		#button.setToolTip('This s an example button')
		#button.move(500,0)
		#button.resize(140,100)

		myUsbManager = usbManager()

		self.setLayout(hBox)
		self.show()

	def init_menuBar(self):
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('File')
		viewMenu = menubar.addMenu('View')
		toolsMennu = menubar.addMenu('Tools')
		helpMenu = menubar.addMenu('Help')
		
		impMenu = QMenu('Import', self)
		impAct = QAction('Import mail', self) 
		impMenu.addAction(impAct)
		
		newAct = QAction('New', self)        
		
		fileMenu.addAction(newAct)
		fileMenu.addMenu(impMenu)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())