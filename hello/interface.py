from PyQt5 import QtCore, QtGui, QtWidgets
from kettle_form import Ui_Dialog
from models import Euler

class KettleForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(KettleForm, self).__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.model = None

    def accept_model(self, model):
        self.model=model
        print("Model")
        self.update_model()

    def update_model(self):
        self.ui.h.setProperty("value",self.model.h)

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kf = KettleForm()
    kf.show()
    kf.accept_model(Euler(
            0.01,
            24.0,
            0.0,
            100.0,
            0.2415,
            0.01,
            10))
    sys.exit(app.exec_())

main()

