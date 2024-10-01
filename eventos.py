import sys
from PyQt6 import QtWidgets, QtGui

import conexion
import var


class Eventos:
    def mensajeSalir(self=None):
        mbox = QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
        mbox.setWindowIcon(QtGui.QIcon("./img/icono.svg"))
        mbox.setWindowTitle('Salir')
        mbox.setText("Desea salir?")
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')

        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()

    def cargarProv(self):
        var.ui.cmbProvcli.clear()
        listado = conexion.Conexion.listarProvincias(self)
        var.ui.cmbProvcli.addItems(listado)
    def cargarMuni(self):
        var.ui.cmbMunicli.clear()
        listado = conexion.Conexion.listarMunicipios(self)
        var.ui.cmbMunicli.addItems(listado)

    def validarDNI(dni):
        try:
            dni = str(dni).upper()
            var.ui.txtDnicli.setText(str(dni))
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    return True
                else:
                    var.ui.txtDnicli.setStyleSheet('background-color:#FFC0CB;')
                    var.ui.txtDnicli.setText(None)
                    var.ui.txtDnicli.setFocus()
            else:
                var.ui.txtDnicli.setStyleSheet('background-color:#FFC0CB;')
                var.ui.txtDnicli.setText(None)
                var.ui.txtDnicli.setFocus()

        except Exception as error:
            print("error en validar dni ", error)