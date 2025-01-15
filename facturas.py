from PyQt6.uic.properties import QtWidgets, QtGui

import conexion
import var


class Facturas:
    def altaFactura(self):
        try:
            nuevafactura = [var.ui.txtfechafac.text(), var.ui.txtDnicliven.text()]
            if (conexion.Conexion.altaFactura(nuevafactura)):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Factura creada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Error')
                mbox.setText('Error al crear la factura')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
        except Exception as error:
            print('Error alta factura: %s' % str(error))
