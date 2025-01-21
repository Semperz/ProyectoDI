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
                Facturas.cargarTablaFacturas(self)
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
                Facturas.cargarTablaFacturas(self)
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

                botondelfac = QtWidgets.QPushButton()
                botondelfac.setFixedSize(30,24)
                botondelfac.setIcon(QtGui.QIcon('img/basura.png'))
                botondelfac.setProperty("row", index)
                botondelfac.clicked.connect(Facturas.eliminarFactura)
                contenedor = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout()
                layout.addWidget(botondelfac)
                layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0,0,0,0)
                contenedor.setLayout(layout)
                var.ui.tablaFacturas.setCellWidget(index, 3, contenedor)

        except Exception as error:
            print('Error cargar tabla facturas: %s' % str(error))


    def eliminarFactura(self):
        try:
            fila = var.ui.tablaFacturas.currentRow()
            if fila == -1:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Seleccione una factura')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
            else:
                numfac = var.ui.tablaFacturas.item(fila, 0).text()
                conexion.Conexion.eliminarFactura(numfac)
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Informacion')
                mbox.setText('Factura eliminada')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Facturas.cargarTablaFacturas(self)
        except Exception as error:
            print('Error eliminar factura: %s' % str(error))


    def cargarOneFactura(self):
        try:
            fila = var.ui.tablaFacturas.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneFactura(str(datos[0]))

            listado = [var.ui.lblNumfac, var.ui.lblFechafac, var.ui.txtDnicliven]

            for index in range(len(listado)):
                    listado[index].setText(registro[index])
        except Exception as error:
            print("error carga factura", error)

