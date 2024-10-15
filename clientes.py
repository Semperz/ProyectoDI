from PyQt6 import QtWidgets, QtGui, QtCore

import clientes
import conexion
import conexionserver
import eventos
import var

class Clientes:

    def checkDNI(dni):
        try:
            dni = str(dni).upper()
            var.ui.txtDnicli.setText(str(dni))
            check = eventos.Eventos.validarDNI(dni)
            if check:
                var.ui.txtDnicli.setStyleSheet("background-color: rgb(229, 255, 255);")
            else:
                var.ui.txtDnicli.setStyleSheet('background-color:#FFC0CB;')
                var.ui.txtDnicli.setText(None)
                var.ui.txtDnicli.setFocus()
        except Exception as e:
            print("error check cliente",e)

    def altaClientes(self):
        try:
            nuevoCli = [var.ui.txtDnicli.text(), var.ui.txtAltaCli.text(), var.ui.txtApelcli.text(), var.ui.txtNomcli.text(),
                    var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(), var.ui.cmbProvcli.currentText(), var.ui.cmbMunicli.currentText()]
            for i in range(len(nuevoCli)):
                if nuevoCli[i] == "":
                    QtWidgets.QMessageBox.critical(None, 'Error', "Faltan campos por cubrir")
                    return
                else:
                    pass
            if not conexion.Conexion.altaCliente(nuevoCli):
                QtWidgets.QMessageBox.critical(None, 'Error', "Ha ocurrido un error")
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("./img/icono.svg"))
                mbox.setWindowTitle('Aviso')
                mbox.setText("Cliente grabado en la base de datos")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Clientes.cargaTablaClientes(self)
                eventos.Eventos.clearCampos()
        except Exception as e:
            print("error alta cliente",e)


    def checkEmail(nuevo):
        try:
            mail = str(var.ui.txtEmailcli.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailcli.setStyleSheet('background-color: rgb(229, 255, 255);')
                var.ui.txtEmailcli.setText(mail.lower())

            else:
                var.ui.txtEmailcli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtEmailcli.setText(None)
                var.ui.txtEmailcli.setFocus()

        except Exception as error:
            print("error check cliente", error)

    def checkNumero(nuevo):
        try:
            telefono = str(var.ui.txtMovilcli.text())
            if eventos.Eventos.validarTelefono(telefono):
                var.ui.txtMovilcli.setStyleSheet('background-color: rgb(229, 255, 255);')
                var.ui.txtMovilcli.setText(telefono.lower())

            else:
                var.ui.txtMovilcli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtMovilcli.setText(None)
                var.ui.txtMovilcli.setFocus()
        except Exception as e:
            print("error check cliente", e)

    def cargaTablaClientes(self):
        try:
            listado = conexion.Conexion.listadoClientes()
            # listado = conexionserver.ConexionServer.listadoClientes()
            index = 0
            for registro in listado:
                var.ui.tablaClientes.setRowCount(index + 1)
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(registro[0]))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[2]))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(registro[3]))
                var.ui.tablaClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(" " + " " + registro[5] + " " + " "))
                var.ui.tablaClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(registro[7]))
                var.ui.tablaClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(registro[8]))
                var.ui.tablaClientes.setItem(index, 6, QtWidgets.QTableWidgetItem(registro[9]))
                var.ui.tablaClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1
        except Exception as e:
            print("Error carga tabla clientes ", e)


    def cargaOneCliente(self):
        try:
            fila = var.ui.tablaClientes.selectedItems()
            datos =  [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneCliente(str(datos[0]))
            listado = [var.ui.txtDnicli, var.ui.txtAltaCli, var.ui.txtApelcli, var.ui.txtNomcli,
             var.ui.txtEmailcli, var.ui.txtMovilcli, var.ui.txtDircli, var.ui.cmbProvcli, var.ui.cmbMunicli]
            for i in range(len(listado)):
                if i == 7 or i == 8:
                    listado[i].setCurrentText(registro[i])
                else:
                    listado[i].setText(registro[i])
            #Clientes.cargarCliente(registro)
        except Exception as error:
            print("error carga cliente",error)


    def modifCliente(self):
        try:
            modifcli = [var.ui.txtDnicli.text(), var.ui.txtAltaCli.text(), var.ui.txtApelcli.text(),
                        var.ui.txtNomcli.text(),
                        var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(),
                        var.ui.cmbProvcli.currentText(), var.ui.cmbMunicli.currentText()]
            conexion.Conexion.modifCliente(modifcli)
            clientes.Clientes.cargaTablaClientes(self)
        except Exception as error:
            print("error al modificar clientes",error)











