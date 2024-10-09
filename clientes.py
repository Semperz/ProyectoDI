from PyQt6 import QtWidgets, QtGui

import conexion
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
            '''for i in len(nuevoCli):
                if nuevoCli[i] == "":
                    QtWidgets.QMessageBox.critical(None, 'Error', "Ha ocurrido un error")
                else:
                    pass'''
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
        except Exception as e:
            print("error alta cliente",e)


    def checkEmail(nuevo):
        try:
            mail = str(var.ui.txtEmailcli.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailcli.setStyleSheet('background-color: rgb(255, 255, 255);')
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
                var.ui.txtMovilcli.setStyleSheet('background-color: rgb(255, 255, 255);')
                var.ui.txtMovilcli.setText(telefono.lower())

            else:
                var.ui.txtMovilcli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtMovilcli.setText(None)
                var.ui.txtMovilcli.setFocus()
        except Exception as e:
            print("error check cliente", e)
