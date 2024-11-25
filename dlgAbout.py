# Form implementation generated from reading ui file '.\templates\dlgAbout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_windowAbout(object):
    def setupUi(self, windowAbout):
        windowAbout.setObjectName("windowAbout")
        windowAbout.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        windowAbout.resize(400, 300)
        windowAbout.setMinimumSize(QtCore.QSize(400, 300))
        windowAbout.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../img/icono.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        windowAbout.setWindowIcon(icon)
        windowAbout.setModal(True)
        self.lblImagenLogo = QtWidgets.QLabel(parent=windowAbout)
        self.lblImagenLogo.setGeometry(QtCore.QRect(0, 0, 131, 141))
        self.lblImagenLogo.setText("")
        self.lblImagenLogo.setPixmap(QtGui.QPixmap(".\\templates\\../img/icono.svg"))
        self.lblImagenLogo.setObjectName("lblImagenLogo")
        self.btnCerrar = QtWidgets.QPushButton(parent=windowAbout)
        self.btnCerrar.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.btnCerrar.setObjectName("btnCerrar")
        self.layoutWidget = QtWidgets.QWidget(parent=windowAbout)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 30, 191, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lblLink = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblLink.setOpenExternalLinks(True)
        self.lblLink.setObjectName("lblLink")
        self.verticalLayout.addWidget(self.lblLink)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.retranslateUi(windowAbout)
        QtCore.QMetaObject.connectSlotsByName(windowAbout)

    def retranslateUi(self, windowAbout):
        _translate = QtCore.QCoreApplication.translate
        windowAbout.setWindowTitle(_translate("windowAbout", "About InmoTeis"))
        self.btnCerrar.setText(_translate("windowAbout", "Cerrar"))
        self.label.setText(_translate("windowAbout", "InmoTeis"))
        self.label_2.setText(_translate("windowAbout", "Autor: Sergio Prieto García"))
        self.label_3.setText(_translate("windowAbout", "Versión: 0.0.1"))
        self.lblLink.setText(_translate("windowAbout", "<a href=\"https://www.youtube.com/watch?v=QOhmcbfwxnA\">IES de Teis</a>"))
        self.label_4.setText(_translate("windowAbout", " Copyright © 2024-2025"))