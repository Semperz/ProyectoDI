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
                Facturas.cargarTablaFacturas()
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
                Facturas.cargarTablaFacturas()
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

    @staticmethod
    def cargarTablaFacturas():
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
                botondelfac.clicked.connect( lambda checked, idFactura=str(registro[0]) : Facturas.eliminarFactura(idFactura))
                contenedor = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout()
                layout.addWidget(botondelfac)
                layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0,0,0,0)
                contenedor.setLayout(layout)
                var.ui.tablaFacturas.setCellWidget(index, 3, contenedor)

        except Exception as error:
            print('Error cargar tabla facturas: %s' % str(error))


    def eliminarFactura(idFac):
        try:
            if conexion.Conexion.eliminarFactura(idFac):
                Facturas.cargarTablaFacturas()
        except Exception as error:
            print('Error eliminar factura: %s' % str(error))


    def cargarOneFactura(self):
        try:
            fila = var.ui.tablaFacturas.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneFactura(str(datos[0]))
            registroVen = conexion.Conexion.datosOneCliente(str(datos[1]))
            var.ui.txtNomcliven.setText(registroVen[3])
            var.ui.txtApelcliven.setText(registroVen[2])
            listado = [var.ui.lblNumfac, var.ui.lblFechafac, var.ui.txtDnicliven]
            for index in range(len(listado)):
                listado[index].setText(registro[index])

        except Exception as error:
            print("error carga factura", error)


    def grabarVenta(self):
        try:
            nuevaventa = [var.ui.lblNumfac.text(), var.ui.txtcodpropven.text(), var.ui.txtIDven.text()]
            if nuevaventa[0] == '' or nuevaventa[1] == '' or nuevaventa[2] == '':
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "Faltan datos para grabar la venta")
                return
            if var.ui.txtpreciopropven.text() == "Propiedad en intercambio/alquiler":
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "La venta no se puede grabar, la propiedad no tiene precio de compra")
                return
            if conexion.Conexion.grabarVenta(nuevaventa):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Venta grabada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Facturas.cargarTablaFacturas()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Error')
                mbox.setText('Error al grabar la venta')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Facturas.cargarTablaFacturas()
        except Exception as error:
            print("error grabar Venta", error)