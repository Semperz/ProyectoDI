from PyQt6 import QtWidgets, QtGui, QtCore

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
                self.cargarTablaFacturas()
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
                self.cargarTablaFacturas()
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


    def cargarTablaFacturas(self):
        try:
            var.ui.tablaFacturas.setRowCount(0)
            listado = conexion.Conexion.listadoFacturas()
            for index, registro in enumerate(listado):
                var.ui.tablaFacturas.insertRow(index)
                var.ui.tablaFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(" " + " " +str(registro[0]) + " " + " "))
                var.ui.tablaFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tablaFacturas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tablaFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaFacturas.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaFacturas.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)

        except Exception as error:
            print('Error cargar tabla facturas: %s' % str(error))



