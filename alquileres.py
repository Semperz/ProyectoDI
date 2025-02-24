from PyQt6 import QtWidgets
from PyQt6 import QtCore, QtGui

import conexion
import eventos
import var


class Alquileres:

    def altaAlquiler(self):
        try:
            registro = [var.ui.txtcodpropalqui.text(),var.ui.txtDniclialqui.text(),var.ui.txtIniciocontrato.text(),var.ui.txtFincontrato.text(), var.ui.txtIDvenalqui.text()]
            isAlquilada = conexion.Conexion.propiedadIsAlquilada(var.ui.txtcodpropalqui.text())
            isVendida = conexion.Conexion.propiedadIsVendida(var.ui.txtcodpropalqui.text())
            precio = var.ui.txtpreciopropalqui.text()
            if isAlquilada or isVendida:
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "La propiedad seleccionada ya se encuentra alquilada. No es posible crear el contrato.")
            elif not Alquileres.hasCamposObligatorios(registro):
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "No se ha podido crear el contrato. Alguno de los campos necesarios está vacío. Recuerde seleccionar una propiedad, un cliente, un vendedor y fecha de inicio y fin de contrato.")
            elif precio == "":
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "La propiedad seleccionada no está disponible para alquiler. Se debe modificar la actual o seleccionar otra disponible para alquiler.")
            elif  conexion.Conexion.altaAlquiler(registro):
                QtWidgets.QMessageBox.information(None, 'Información',
                                               "Contrato de alquiler creado correctamente.")
                eventos.Eventos.limpiarPanel(self)
                Alquileres.cargaTablaContratos()
            else:
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "Se ha producido un error inesperado y no es posible generar un nuevo contrato de alquiler.")

        except Exception as e:
            print("Error alta alquiler en alquileres",str(e))

    @staticmethod
    def hasCamposObligatorios(registro):
        for dato in registro:
            if dato is None or dato == '':
                return False
            else:
                return True

    @staticmethod
    def cargaTablaContratos():

        try:
            var.ui.tablaContrato.setRowCount(0)
            listado = conexion.Conexion.listadoAlquileres()
            for index, registro in enumerate(listado):
                var.ui.tablaContrato.insertRow(index)
                var.ui.tablaContrato.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaContrato.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tablaContrato.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaContrato.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                botondelcontrato = QtWidgets.QPushButton()
                botondelcontrato.setFixedSize(30, 24)
                botondelcontrato.setIcon(QtGui.QIcon('img/basura.png'))
                botondelcontrato.setProperty("row", index)
                botondelcontrato.clicked.connect(
                    lambda checked, idContrato=str(registro[0]): Alquileres.eliminarAlquiler(idContrato))
                contenedor = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout()
                layout.addWidget(botondelcontrato)
                layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                contenedor.setLayout(layout)
                var.ui.tablaContrato.setCellWidget(index, 2, contenedor)

        except Exception as error:
            print('Error cargar tabla facturas: %s' % str(error))


    @staticmethod
    def clearCamposAlquileres():
        var.ui.lblNumcontrato.setText(None)
        var.ui.txtIDvenalqui.setText(None)
        var.ui.txtDniclialqui.setText(None)
        var.ui.txtcodpropalqui.setText(None)
        var.ui.txtIniciocontrato.setText(None)
        var.ui.txtFincontrato.setText(None)
        var.ui.txtApelclialqui.setText(None)
        var.ui.txtNomclialqui.setText(None)
        var.ui.txtTipopropalqui.setText(None)
        var.ui.txtDirpropalqui.setText(None)
        var.ui.txtpreciopropalqui.setText(None)
        var.ui.txtlocalpropalqui.setText(None)


    def eliminarAlquiler(idContrato):
        try:
            if QtWidgets.QMessageBox.question(None, 'Eliminar contrato',
                                              '¿Desea eliminar el contrato seleccionado?',
                                              QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No) == QtWidgets.QMessageBox.StandardButton.Yes:
                if conexion.Conexion.eliminarAlquiler(idContrato):
                    QtWidgets.QMessageBox.information(None, 'Información',
                                                   "Contrato eliminado correctamente.")
                    Alquileres.cargaTablaContratos()
                else:
                    QtWidgets.QMessageBox.critical(None, 'Error',
                                               "Se ha producido un error inesperado y no es posible eliminar el contrato seleccionado.")
        except Exception as e:
            print("Error eliminar contrato en alquileres",str(e))

