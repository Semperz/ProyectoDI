# Form implementation generated from reading ui file '.\templates\dlgGestionprop.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgTipoProp(object):
    def setupUi(self, dlgTipoProp):
        dlgTipoProp.setObjectName("dlgTipoProp")
        dlgTipoProp.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        dlgTipoProp.resize(400, 300)
        dlgTipoProp.setMinimumSize(QtCore.QSize(400, 300))
        dlgTipoProp.setMaximumSize(QtCore.QSize(400, 300))
        dlgTipoProp.setModal(True)
        self.frame = QtWidgets.QFrame(parent=dlgTipoProp)
        self.frame.setGeometry(QtCore.QRect(9, 9, 382, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.txtGestionprop = QtWidgets.QLineEdit(parent=self.frame)
        self.txtGestionprop.setGeometry(QtCore.QRect(120, 170, 150, 20))
        self.txtGestionprop.setMinimumSize(QtCore.QSize(150, 20))
        self.txtGestionprop.setMaximumSize(QtCore.QSize(150, 20))
        self.txtGestionprop.setObjectName("txtGestionprop")
        self.lblGestionprop = QtWidgets.QLabel(parent=self.frame)
        self.lblGestionprop.setGeometry(QtCore.QRect(120, 150, 141, 20))
        self.lblGestionprop.setObjectName("lblGestionprop")
        self.iconGestionprop = QtWidgets.QLabel(parent=self.frame)
        self.iconGestionprop.setGeometry(QtCore.QRect(120, 10, 141, 131))
        self.iconGestionprop.setText("")
        self.iconGestionprop.setPixmap(QtGui.QPixmap(".\\templates\\../img/icono.svg"))
        self.iconGestionprop.setObjectName("iconGestionprop")
        self.widget = QtWidgets.QWidget(parent=dlgTipoProp)
        self.widget.setGeometry(QtCore.QRect(70, 240, 250, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnAltatipoprop = QtWidgets.QPushButton(parent=self.widget)
        self.btnAltatipoprop.setObjectName("btnAltatipoprop")
        self.horizontalLayout.addWidget(self.btnAltatipoprop)
        self.btnDeltipoprop = QtWidgets.QPushButton(parent=self.widget)
        self.btnDeltipoprop.setObjectName("btnDeltipoprop")
        self.horizontalLayout.addWidget(self.btnDeltipoprop)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(dlgTipoProp)
        QtCore.QMetaObject.connectSlotsByName(dlgTipoProp)

    def retranslateUi(self, dlgTipoProp):
        _translate = QtCore.QCoreApplication.translate
        dlgTipoProp.setWindowTitle(_translate("dlgTipoProp", "Dialog"))
        self.lblGestionprop.setText(_translate("dlgTipoProp", "Gestión tipo de propiedad"))
        self.btnAltatipoprop.setText(_translate("dlgTipoProp", "Alta"))
        self.btnDeltipoprop.setText(_translate("dlgTipoProp", "Eliminar"))
