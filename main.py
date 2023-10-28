import random
from PyQt5.QtWitgets import QApplication
from PyQt5.QtWitgets import QMainWindow
from ui import Ui_MainWindow

class Witget(QMainWindow):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.example)
def example(self):
    signs = ''
    if self.ui.checkBox.isChecked():
        signs = 'qwertyuiopasdfghjklzxcvbnm'
    if self.ui.checkBox_2.isChecked():
        signs += '0123456789'
    result = ''
    number = random.randint(5, 10)
    for i in range(number):
        result += random.choise(signs)
    self.ui.Label_2.setText(result)
app = QApplication([])
ex = Witget()
ex.show()
app.exec_()