from PyQt6 import QtWidgets, QtGui, QtCore
import eventos
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
            propiedad = [var.ui.txtFechaprop.text(), var.ui.txtDirprop.text(), var.ui.cmbProvprop.currentText(),
                         var.ui.cmbMuniprop.currentText(), var.ui.cmbTipoprop.currentText(),
                         var.ui.spnHabprop.text(), var.ui.spnBanosprop.text(), var.ui.txtSuperprop.text(),
                         var.ui.txtPrecioalquilerprop.text(), var.ui.txtPrecioventaprop.text(), var.ui.txtCPprop.text(),
                         var.ui.areatxtDescriprop.toPlainText()]
            tipooper = []
            if var.ui.chkAlquilerprop.isChecked():
                tipooper.append(var.ui.chkAlquilerprop.text())
            if var.ui.chkVentaprop.isChecked():
                tipooper.append(var.ui.chkVentaprop.text())
            if var.ui.chkInterprop.isChecked():
                tipooper.append(var.ui.chkInterprop.text())
            propiedad.append(tipooper)
            if var.ui.rbtDisponibleprop.isChecked():
                propiedad.append(var.ui.rbtDisponibleprop.text())
            if var.ui.rbtAlquiladoprop.isChecked():
                propiedad.append(var.ui.rbtAlquiladoprop.text())
            if var.ui.rbtVendidoprop.isChecked():
                propiedad.append(var.ui.rbtVendidoprop.text())

            propiedad.append(var.ui.txtNomeprop.text())
            propiedad.append(var.ui.txtMovilprop.text())
            if conexion.Conexion.altaPropiedad(propiedad):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("./img/icono.svg"))
                mbox.setWindowTitle('Aviso')
                mbox.setText("Propiedad grabada en la base de datos")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Propiedades.cargaTablaPropiedades(self)
            else:
                QtWidgets.QMessageBox.critical(None, 'Error', "Faltan campos por cubrir o hay datos mal puestos.")
        except Exception as error:
            print(error)

    def checkNumeroProp(nuevo):
        try:
            telefono = str(var.ui.txtMovilprop.text())
            if eventos.Eventos.validarTelefono(telefono):
                var.ui.txtMovilprop.setStyleSheet('background-color: rgb(229, 255, 255);')
                var.ui.txtMovilprop.setText(telefono.lower())

            else:
                var.ui.txtMovilprop.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtMovilprop.setText(None)
                var.ui.txtMovilprop.setFocus()
        except Exception as e:
            print("error numero propiedad", e)

    def cargaTablaPropiedades(self):
        try:
            listado = conexion.Conexion.listadoPropiedades()
            index = 0
            for registro in listado:
                var.ui.tablaPropiedades.setRowCount(index + 1)
                var.ui.tablaPropiedades.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaPropiedades.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[5]))
                var.ui.tablaPropiedades.setItem(index, 2, QtWidgets.QTableWidgetItem(registro[6]))
                var.ui.tablaPropiedades.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[7])))
                var.ui.tablaPropiedades.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[8])))
                if registro[10] == '':
                    registro[10] = '-'
                if registro[11] == '':
                    registro[11] = '-'
                var.ui.tablaPropiedades.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[10])+ " €"))
                var.ui.tablaPropiedades.setItem(index, 6, QtWidgets.QTableWidgetItem(str(registro[11])+ " €"))
                var.ui.tablaPropiedades.setItem(index, 7, QtWidgets.QTableWidgetItem(registro[14]))
                var.ui.tablaPropiedades.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaPropiedades.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaPropiedades.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaPropiedades.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaPropiedades.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaPropiedades.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaPropiedades.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaPropiedades.item(index, 7).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                index += 1
        except Exception as e:
            print("Error carga tabla clientes ", e)