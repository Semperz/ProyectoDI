from PyQt6 import QtWidgets, QtGui

import conexion
import var
from conexion import Conexion


class Propiedades():
    def altaTipoPropiedad(self):
        try:
            tipo =  var.dlggestion.ui.txtGestionprop.text().title()
            registro = conexion.Conexion.altaTipoprop(tipo)
            if registro:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/logo.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad añadida a la base de datos')
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
                var.ui.cmbTipoprop.clear()
                var.ui.cmbTipoprop.addItems(registro)
                var.dlggestion.ui.txtGestionprop.setText("")
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/logo.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad Existe')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
        except Exception as e:
            print(e)


    def bajaTipoPropiedad(self):
        try:
            tipo =  var.dlggestion.ui.txtGestionprop.text().title()
            registro = conexion.Conexion.bajaTipoprop(tipo)
            if registro:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/logo.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad eliminada de la base de datos')
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
                var.ui.cmbTipoprop.clear()
                var.ui.cmbTipoprop.addItems(registro)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/logo.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad no existente')
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
            var.dlggestion.ui.txtGestionprop.setText("")
        except Exception as e:
            print(e)



    def altaPropiedad(self):
        try:
            propiedad = [var.ui.txtFechaprop.text(),var.ui.txtFechabajaprop.text(), var.ui.txtDirprop.text(),
                         var.ui.cmbProvprop.currentText(), var.ui.cmbMuniprop.currentText(), var.ui.cmbTipoprop.currentText(),
                         var.ui.spnHabprop.text(), var.ui.spnBanosprop.currentText(), var.ui.txtSuperprop.text(),
                         var.ui.txt.txtPrecioalquilerprop.text(), var.ui.txtPrecioventaprop.text(), var.ui.txtCPprop.text(),
                         var.ui.areatxtDescriprop.toPlainText(), var.ui.txtMovilprop.text()
                         ]
        except Exception as error:
            print(error)