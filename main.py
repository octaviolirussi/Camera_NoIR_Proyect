import sys
from PySide6 import QtWidgets
from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        print("Clicked!")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()