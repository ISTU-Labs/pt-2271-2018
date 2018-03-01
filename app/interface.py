from PyQt5 import QtCore, QtGui, QtWidgets
from kettle_form import Ui_Dialog
from models import Euler


class KettleView(QtWidgets.QDialog):
    def __init__(self, parent=None, model=None):
        super(KettleView, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.accept(model)

    def accept(self, model):
        self.model = model
        if model is not None:
            self.update()

    def get_widget(self, name):
        widget = getattr(self.ui, name)
        return widget

    def get_data(self, name):
        val = getattr(self.model, name)
        return val

    def update(self):
        """Update View with Model Data"""
        assert self.model is not None, "setup model first"
        ui = self.ui
        m = self.model
        fields = "k,Tenv,t0,T0,h,eps,m".split(",")
        for name in fields:
            widget = self.get_widget(name)
            val = self.get_data(name)
            widget.setProperty("value", val)

            # @eugeneai


class KettleController:

    __fields__ = "k,Tenv,t0,T0,h,eps,m".split(",")

    def get_model(self):
        return self.view.model

    model = property(get_model)

    def __init__(self, view):
        self.accept(view)

    def accept(self, view):
        self.view = view
        for name in self.__class__.__fields__:
            widget = self.view.get_widget(name)
            widget.valueChanged[str].connect(self._on_value_changed)

    def _on_value_changed(self, value):
        sender = self.view.sender()
        name = sender.objectName()
        value = value.replace(",", '.')
        try:
            v = int(value)
        except ValueError:
            try:
                v = float(value)
            except ValueError:
                print("Bad value")
                return

        setattr(self.model, name, v)
        print("Set {} to {}".format(name, repr(v)))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)

    e = Euler(
        0.015,
        23.0,
        0.01,
        200.0,
        0.15,
        0.015,
        20)

    # e.calculate()

    kv = KettleView()
    kv.show()
    kc = KettleController(kv)

    kv.accept(e)

    sys.exit(app.exec_())


main()
