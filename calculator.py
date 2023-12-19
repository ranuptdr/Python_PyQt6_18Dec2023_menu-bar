import sys

#from toplevelModule.SubModulen  import element1,element2........
from PyQt6.QtWidgets import QApplication, QMainWindow

#2. create  instance/class object of QApplication class
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
#window = QWidget()
#window = QPushButton('Click Me')
window = QMainWindow()
window.show()

# create a menubar
menu_bar = window.menuBar()
file_menu = menu_bar.addMenu('File')

edit_menu = menu_bar.addMenu("Edit")
selection_menu = menu_bar.addMenu('selection')
view_menu = menu_bar.addMenu("View")


# Start the event loop.
app.exec()
