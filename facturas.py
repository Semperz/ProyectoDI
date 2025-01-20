from PyQt6 import QtWidgets, QtGui

import conexion
import var


class Facturas:
    def altaFactura(self):
        try:
            nuevafactura = [var.ui.lblFechafac.text(), var.ui.txtDnicliven.text()]
            if conexion.Conexion.altaFactura(nuevafactura) and var.ui.txtDnicliven.text() != '':
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

    @staticmethod
    def clearCamposFacturas():
        var.ui.lblFechafac.setText(None)
        var.ui.lblNumfac.setText(None)
        var.ui.txtDnicliven.setText(None)
        var.ui.txtApelcliven.setText(None)
        var.ui.txtNomcliven.setText(None)
        var.ui.txtdirpropven.setText(None)
        var.ui.txtcodpropven.setText(None)
        var.ui.txtTipopropven.setText(None)
        var.ui.txtpreciopropven.setText(None)
        var.ui.txtlocalpropven.setText(None)
        var.ui.txtIDven.setText(None)



