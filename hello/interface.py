from PyQt5 import QtCore, QtGui, QtWidgets
from kettle_form import Ui_Dialog

class KettleForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(KettleForm, self).__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.model = None
        
    def accept(self, model):
        self.model=model
        self.update()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kf = KettleForm()
    kf.show()
    sys.exit(app.exec_())

main()
