from PyQt6 import QtWidgets, QtGui, QtCore
import eventos
import conexion
import propiedades
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
                propiedades.Propiedades.clearCamposPropiedades()
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
                var.ui.tablaPropiedades.setItem(index, 8, QtWidgets.QTableWidgetItem(registro[2]))
                var.ui.tablaPropiedades.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaPropiedades.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaPropiedades.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaPropiedades.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaPropiedades.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaPropiedades.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaPropiedades.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaPropiedades.item(index, 7).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaPropiedades.item(index, 8).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                index += 1
        except Exception as e:
            print("Error carga tabla propiedades ", e)

    def cargaOnePropiedad(self):
        try:
            fila = var.ui.tablaPropiedades.selectedItems()
            datos =  [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOnePropiedad(str(datos[0]))
            listado = [var.ui.txtFechaprop, var.ui.txtFechabajaprop, var.ui.txtDirprop, var.ui.cmbProvprop,
             var.ui.cmbMuniprop, var.ui.cmbTipoprop,
             var.ui.spnHabprop, var.ui.spnBanosprop, var.ui.txtSuperprop,
             var.ui.txtPrecioalquilerprop, var.ui.txtPrecioventaprop, var.ui.txtCPprop,
             var.ui.areatxtDescriprop, var.ui.chkAlquilerprop, var.ui.chkInterprop, var.ui.chkVentaprop,
             var.ui.rbtDisponibleprop, var.ui.rbtVendidoprop, var.ui.rbtAlquiladoprop]
            var.ui.lblIDprop.setText(registro[0])
            for i in range(len(listado)):
                if i == 3 or i == 4 or i == 5:
                    listado[i].setCurrentText(registro[i + 1])
                elif i == 6 or i == 7:
                    listado[i].setValue(int(registro[i + 1]))
                elif i == 13 or i == 14 or i == 15 :
                    if 'Alquiler' in (registro[14]):
                        listado[13].setChecked(True)
                    else:
                        listado[13].setChecked(False)
                    if 'Intercambio' in (registro[14]):
                        listado[14].setChecked(True)
                    else:
                        listado[14].setChecked(False)
                    if 'Venta' in (registro[14]):
                        listado[15].setChecked(True)
                    else:
                        listado[15].setChecked(False)
                elif i == 16 or i == 17 or i == 18:
                    if 'Disponible' in (registro[15]):
                        listado[16].setChecked(True)
                    if 'Vendido' in (registro[15]):
                        listado[17].setChecked(True)
                    if 'Alquilado' in (registro[15]):
                        listado[18].setChecked(True)
                else:
                    listado[i].setText(str(registro[i + 1]))
                var.ui.txtNomeprop.setText(registro[16])
                var.ui.txtMovilprop.setText(registro[17])
        except Exception as error:
            print("error carga propiedad",error)

    def bajaPropiedad(self):
        try:
            datos = [var.ui.txtFechabajaprop.text(), var.ui.lblIDprop.text()]
            if conexion.Conexion.bajaPropiedad(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/logo.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad dada de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Propiedades.cargaTablaPropiedades(self)
                propiedades.Propiedades.clearCamposPropiedades()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/logo.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error baja propiedad: Propiedad no existe o ya está dada de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Propiedades.cargaTablaPropiedades(self)
        except Exception as error:
            print("error baja propiedad", error)

    @staticmethod
    def clearCamposPropiedades():
        var.ui.lblIDprop.setText(None)
        var.ui.txtFechaprop.setText(None)
        var.ui.txtFechabajaprop.setText(None)
        var.ui.txtDirprop.setText(None)
        var.ui.cmbProvprop.setCurrentIndex(0)
        var.ui.cmbTipoprop.setCurrentIndex(0)
        var.ui.spnHabprop.setValue(0)
        var.ui.spnBanosprop.setValue(0)
        var.ui.txtSuperprop.setText(None)
        var.ui.txtPrecioalquilerprop.setText(None)
        var.ui.txtPrecioventaprop.setText(None)
        var.ui.txtCPprop.setText(None)
        var.ui.areatxtDescriprop.setText(None)
        var.ui.chkVentaprop.setChecked(False)
        var.ui.chkInterprop.setChecked(False)
        var.ui.chkAlquilerprop.setChecked(False)
        var.ui.rbtDisponibleprop.setChecked(True)
        var.ui.rbtAlquiladoprop.setChecked(False)
        var.ui.rbtVendidoprop.setChecked(False)
        var.ui.txtNomeprop.setText(None)
        var.ui.txtMovilprop.setText(None)