# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/KettleForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 516)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.h = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.h.setDecimals(4)
        self.h.setMaximum(1.0)
        self.h.setSingleStep(0.01)
        self.h.setProperty("value", 0.1)
        self.h.setObjectName("h")
        self.verticalLayout.addWidget(self.h)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.eps = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.eps.setDecimals(4)
        self.eps.setMinimum(0.001)
        self.eps.setMaximum(1.0)
        self.eps.setSingleStep(0.001)
        self.eps.setProperty("value", 0.01)
        self.eps.setObjectName("eps")
        self.verticalLayout.addWidget(self.eps)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.m = QtWidgets.QSpinBox(self.groupBox_2)
        self.m.setMinimum(1)
        self.m.setMaximum(99999)
        self.m.setProperty("value", 10)
        self.m.setObjectName("m")
        self.verticalLayout.addWidget(self.m)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.k = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.k.setDecimals(3)
        self.k.setMinimum(0.001)
        self.k.setMaximum(1.0)
        self.k.setSingleStep(0.001)
        self.k.setProperty("value", 0.01)
        self.k.setObjectName("k")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.k)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.t0 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.t0.setDecimals(1)
        self.t0.setObjectName("t0")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.t0)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.T0 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.T0.setDecimals(1)
        self.T0.setMinimum(-275.0)
        self.T0.setMaximum(200.0)
        self.T0.setProperty("value", 100.0)
        self.T0.setObjectName("T0")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.T0)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Tenv = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Tenv.setDecimals(1)
        self.Tenv.setMaximum(200.0)
        self.Tenv.setProperty("value", 24.0)
        self.Tenv.setObjectName("Tenv")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Tenv)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.label_5.setBuddy(self.h)
        self.label_6.setBuddy(self.eps)
        self.label_2.setBuddy(self.t0)
        self.label.setBuddy(self.k)
        self.label_3.setBuddy(self.T0)
        self.label_4.setBuddy(self.Tenv)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.T0, self.Tenv)
        Dialog.setTabOrder(self.Tenv, self.k)
        Dialog.setTabOrder(self.k, self.t0)
        Dialog.setTabOrder(self.t0, self.h)
        Dialog.setTabOrder(self.h, self.eps)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "Параметры численного метода"))
        self.label_5.setText(_translate("Dialog", "Шаг интегрирования"))
        self.label_6.setText(_translate("Dialog", "Точность"))
        self.label_7.setText(_translate("Dialog", "Шаг записи"))
        self.groupBox_4.setTitle(_translate("Dialog", "GroupBox"))
        self.groupBox_3.setTitle(_translate("Dialog", "GroupBox"))
        self.label_2.setText(_translate("Dialog", "Начальный момент времени"))
        self.label.setText(_translate("Dialog", "Скорость остывания"))
        self.groupBox.setTitle(_translate("Dialog", "Температура"))
        self.label_3.setText(_translate("Dialog", "Начальная"))
        self.label_4.setText(_translate("Dialog", "Среды"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

