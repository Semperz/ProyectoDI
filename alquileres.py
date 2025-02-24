from PyQt6 import QtWidgets

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


