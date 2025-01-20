from datetime import datetime
from operator import index

from PyQt6 import QtWidgets, QtGui, QtCore
import conexion

import eventos
import var

class Vendedores:

    def checkDNIven(dni):
        try:
            dni = str(dni).upper()
            var.ui.txtDniven.setText(str(dni))
            check = eventos.Eventos.validarDNI(dni)
            if check:
                var.ui.txtDniven.setStyleSheet("background-color: rgb(229, 255, 255);")
            else:
                var.ui.txtDniven.setStyleSheet('background-color:#FFC0CB;')
                var.ui.txtDniven.setText(None)
                var.ui.txtDniven.setFocus()
        except Exception as e:
            print("error check vendedor",e)

    def altaVendedores(self):
        try:

            nuevoVen = [var.ui.txtDniven.text(), var.ui.txtAltaven.text(), var.ui.txtNomven.text(),
                     var.ui.txtEmailven.text(), var.ui.txtMovilven.text(),var.ui.cmbDelegacionven.currentText()]
            camposObligatorios = [var.ui.txtDniven.text(), var.ui.txtNomven.text(), var.ui.txtMovilven.text(), var.ui.cmbDelegacionven.currentText()]
            for i in range(len(camposObligatorios)):
                if camposObligatorios[i] == "":
                    QtWidgets.QMessageBox.critical(None, 'Error', "Faltan campos obligatorios por cubrir")
                    return
                else:
                    pass
            if nuevoVen[0] in conexion.Conexion.listarDNIven():
                QtWidgets.QMessageBox.critical(None, 'Error', "El DNI ya existe")
            elif not conexion.Conexion.altaVendedor(nuevoVen):
                QtWidgets.QMessageBox.critical(None, 'Error', "No se ha podido completar la alta")
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("./img/icono.svg"))
                mbox.setWindowTitle('Aviso')
                mbox.setText("Vendedor grabado en la base de datos")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                #Vendedores.cargaTablaVendedores(self)
                Vendedores.clearCamposVendedores()
        except Exception as e:
            print("error alta vendedor",e)

    @staticmethod
    def cargarDelegacionven():
        var.ui.cmbDelegacionven.clear()
        listado = conexion.Conexion.listarProvincias()
        var.ui.cmbDelegacionven.addItems(listado)

    @staticmethod
    def clearCamposVendedores():
        var.ui.txtDniven.setText(None)
        var.ui.txtNomven.setText(None)
        var.ui.txtMovilven.setText(None)
        var.ui.txtEmailven.setText(None)
        var.ui.txtAltaven.setText(None)
        var.ui.cmbDelegacionven.setCurrentIndex(0)


    def historicoVen(self):
        try:
            if var.ui.chkHistoricoven.isChecked():
                var.historico = 0
            else:
                var.historico = 1
            Vendedores.cargarTablaVendedores(self)
        except (Exception) as error:
            print("error al historico vendedor",error)
    
    @staticmethod
    def resizeTablaVendedores():
        try:
            header = var.ui.tablaVendedores.horizontalHeader()
            for i in range(header.count()):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

            header_item = var.ui.tablaVendedores.horizontalHeaderItem(i)
            font = header_item.font()
            font.setBold(True)
            header_item.setFont(font)
        except Exception as e:
            print("error en resize tabla vendedores", e)
    
    def cargarTablaVendedores(self):
        try:
            var.ui.tablaVendedores.setRowCount(0)
            listado = conexion.Conexion.listadoVendedores()
            for index, registro in enumerate(listado):
                var.ui.tablaVendedores.insertRow(index)
                var.ui.tablaVendedores.setItem(index, 0, QtWidgets.QTableWidgetItem(" " + " " +str(registro[0]) + " " + " "))
                var.ui.tablaVendedores.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tablaVendedores.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tablaVendedores.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[7])))
                var.ui.tablaVendedores.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaVendedores.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaVendedores.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaVendedores.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)


        except Exception as e:
            print("Error carga tabla vendedores ", e)

    def checkEmail(nuevo):
        try:
            mail = str(var.ui.txtEmailven.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailven.setStyleSheet('background-color: rgb(229, 255, 255);')
                var.ui.txtEmailven.setText(mail.lower())

            else:
                var.ui.txtEmailven.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtEmailven.setText(None)
                var.ui.txtEmailven.setFocus()

        except Exception as error:
            print("error check vendedor", error)

    def checkNumero(nuevo):
        try:
            telefono = str(var.ui.txtMovilven.text())
            if eventos.Eventos.validarTelefono(telefono):
                var.ui.txtMovilven.setStyleSheet('background-color: rgb(229, 255, 255);')
                var.ui.txtMovilven.setText(telefono.lower())

            else:
                var.ui.txtMovilven.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtMovilven.setText(None)
                var.ui.txtMovilven.setFocus()
        except Exception as e:
            print("error check vendedor", e)


    def modifVendedor(self):
        try:
            modifVen = [var.ui.txtDniven.text(), var.ui.txtAltaven.text(), var.ui.txtNomven.text(),
                        var.ui.txtEmailven.text(), var.ui.txtMovilven.text(), var.ui.cmbDelegacionven.currentText(), var.ui.txtBajaven.text()]

            validarFechaBaja = Vendedores.checkFechaValidaven()
            if (validarFechaBaja == False):
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "La fecha de baja no puede ser anterior a la fecha de alta.")
            elif conexion.Conexion.modifVendedor(modifVen):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Vendedor modificado')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Vendedores.cargarTablaVendedores(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error vendedor modificado')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Vendedores.cargarTablaVendedores(self)
            Vendedores.cargarTablaVendedores(self)
        except Exception as error:
            print("error al modificar clientes",error)

    def cargaOneVendedor(self):
        try:
            fila = var.ui.tablaVendedores.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneVendedor(str(datos[0]))

            listado = [var.ui.txtIDven, var.ui.txtDniven, var.ui.txtNomven, var.ui.txtAltaven, var.ui.txtBajaven,
             var.ui.txtMovilven, var.ui.txtEmailven, var.ui.cmbDelegacionven]


            '''
            conexión con ventas
            '''
            var.ui.txtIDven.setText(str(registro[0]))

            for index in range(len(listado)):
                if index == 7:
                    listado[index].setCurrentText(registro[index])
                else:
                    listado[index].setText(registro[index])
        except Exception as error:
            print("error carga vendedor", error)
    @staticmethod
    def checkFechaValidaven():
        try:
            if var.ui.txtBajaven.text() == "" or var.ui.txtBajaven.text() is None:
                return True
            else:
                fechaBaja = datetime.strptime(var.ui.txtBajaven.text(), "%d/%m/%Y")
                fechaAlta = datetime.strptime(var.ui.txtAltaven.text(), "%d/%m/%Y")
                if fechaBaja < fechaAlta:
                    return False
                else:
                    return True

        except Exception as e:
            print("error check fecha baja", e)


    def bajaVendedor(self):
        try:
            datos = [var.ui.txtBajaven.text(), var.ui.txtDniven.text()]
            if conexion.Conexion.bajaVendedor(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Vendedor dado de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Vendedores.cargarTablaVendedores(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error baja vendedor: vendedor no existe o ya está dado de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Vendedores.cargarTablaVendedores(self)
        except Exception as error:
            print("error baja vendedor", error)



    def filtroBusquedaVendedor(self):
        try:
            Vendedores.cargarTablaVendedores(self)
            Vendedores.cargaOneVendedorBusqueda(self)
        except Exception as e:
            print(e)

    def cargaOneVendedorBusqueda(self):
        try:
            movil = var.ui.txtMovilven.text()
            registro = conexion.Conexion.datosOneVendedorMovil(str(movil))
            if registro == []:
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "No existe esa persona.")
                var.ui.btnBuscarven.setChecked(False)
                Vendedores.cargarTablaVendedores(self)

            else:
                listado = [var.ui.txtDniven, var.ui.txtNomven, var.ui.txtAltaven, var.ui.txtBajaven,
                           var.ui.txtMovilven, var.ui.txtEmailven, var.ui.cmbDelegacionven]
                for index in range(len(listado)):
                    if index == 6:
                        listado[index].setCurrentText(registro[index])
                    else:
                        listado[index].setText(registro[index])
        except Exception as error:
            print("error carga cliente", error)