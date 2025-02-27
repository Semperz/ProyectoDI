import datetime
import locale

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHBoxLayout, QWidget

import conexion
import eventos
import informes
import var
from propiedades import Propiedades

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")


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
            elif  conexion.Conexion.altaAlquiler(registro) and Alquileres.generarMensualidades(registro):
                QtWidgets.QMessageBox.information(None, 'Información',
                                               "Contrato de alquiler creado correctamente.")
                eventos.Eventos.limpiarPanel(self)
                Alquileres.cargaTablaContratos()
                Propiedades.clearCamposPropiedades()
                Propiedades.cargaTablaPropiedades()
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
            print('Error cargar tabla contrtos: %s' % str(error))


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
        var.ui.txtdirpropalqui.setText(None)
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


    def cargaOneContrato(self):
        try:
            fila = var.ui.tablaContrato.selectedItems()
            datos = [dato.text() for dato in fila]

            registro = conexion.Conexion.datosOneAlquiler(str(datos[0]))
            listado = [var.ui.lblNumcontrato, var.ui.txtIniciocontrato, var.ui.txtFincontrato, var.ui.txtIDvenalqui,
                       var.ui.txtDniclialqui, var.ui.txtNomclialqui ,var.ui.txtApelclialqui ,var.ui.txtcodpropalqui,
                       var.ui.txtTipopropalqui, var.ui.txtpreciopropalqui, var.ui.txtlocalpropalqui, var.ui.txtdirpropalqui]
            for index in range(len(listado)):
                if index == 9:
                    listado[index].setText(str(registro[index]) + " €")
                else:
                    listado[index].setText(str(registro[index]))
            Alquileres.cargaTablaContratos()
            Alquileres.cargarTablaMensualidades(registro[0], registro[7], registro[9])
        except Exception as error:
            print("error carga contrato", error)

    @staticmethod
    def generarMensualidades(registro):
        """

        :param registro: datos de un contrato de alquiler
        :type registro: list
        :return: éxito o no al generar las mensualidades
        :rtype: bool

        Genera las mensualidades del contrato

        """
        try:
            codPropiedad = registro[0]
            dniCliente = registro[1]
            fechaInicioStr = registro[2]
            fechaFinalStr = registro[3]
            idAlquiler = conexion.Conexion.idOneAlquiler(codPropiedad, dniCliente)

            fechaInicio = datetime.datetime.strptime(fechaInicioStr, "%d/%m/%Y")
            fechaFinal = datetime.datetime.strptime(fechaFinalStr, "%d/%m/%Y")

            while fechaInicio <= fechaFinal:
                mes = fechaInicio.strftime("%B").capitalize()
                mes_ano = f"{mes} {fechaInicio.year}"
                registro = [idAlquiler, mes_ano, 0]
                if not conexion.Conexion.altaMensualidad(registro):
                    return False
                fechaInicio = Alquileres.sumar_un_mes(fechaInicio)
            return True

        except ValueError as e:
            print("Error: Las fechas no tienen el formato correcto o no son válidas.", e)
            return False
        except TypeError as e:
            print("Error: Se esperaba una cadena de texto para la fecha.", e)
            return

    @staticmethod
    def sumar_un_mes(fecha):
        """

        :param fecha: fecha
        :type fecha: datetime
        :return: fecha con un mes más añadido
        :rtype: datetime

        Suma un mes a una fecha determinada.

        """
        mes = fecha.month + 1
        ano = fecha.year
        if mes > 12:
            mes = 1
            ano += 1
        dia = 1
        return fecha.replace(year=ano, month=mes, day=dia)


    @staticmethod
    def cargarTablaMensualidades(idAlquiler, codPropiedad, precio):
        """

        :param idAlquiler: el id del contrato de alquiler
        :type idAlquiler: int
        :param codPropiedad: el id de la propiedad
        :type codPropiedad: int
        :param precio: precio mensual de alquiler
        :type precio: float

        Carga todas las mensualidades en la tabla

        """
        try:
            var.ui.btnModificarcontrato.setDisabled(False)
            listado = conexion.Conexion.listarMensualidades(idAlquiler)
            var.ui.tabAlquiler.setRowCount(0)


            for index, registro in enumerate(listado):
                var.ui.tabAlquiler.insertRow(index)
                var.ui.tabAlquiler.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabAlquiler.setItem(index, 1, QtWidgets.QTableWidgetItem(str(codPropiedad)))
                var.ui.tabAlquiler.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabAlquiler.setItem(index, 3, QtWidgets.QTableWidgetItem(str(precio) + " €"))
                var.ui.tabAlquiler.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabAlquiler.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabAlquiler.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabAlquiler.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                botonAlq = QtWidgets.QCheckBox()
                botonAlq.setFixedSize(20,20)
                botonAlq.setProperty("row", index)
                botonAlq.setChecked(registro[2] == 1)
                botonAlq.clicked.connect(
                    lambda checked, checkbox=botonAlq, idMensualidad=registro[0],: Alquileres.pagarMensualidad(
                        idMensualidad, checked, checkbox))
                container = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout()
                layout.addWidget(botonAlq)
                layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                container.setLayout(layout)
                var.ui.tabAlquiler.setCellWidget(index, 4, container)

                #Creamos un boton para generar el informe
                botonInforme = QtWidgets.QPushButton()
                botonInforme.setFixedSize(20,20)
                botonInforme.setIconSize(QtCore.QSize(20, 20))
                botonInforme.setIcon(QtGui.QIcon('./img/icoFactura.png'))

                #creamos layout para centrar el boton
                layout2 = QHBoxLayout()
                layout2.addWidget(botonInforme)
                layout2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                layout2.setContentsMargins(0, 0, 0, 0)
                layout2.setSpacing(0)

                container2 = QWidget()
                container2.setLayout(layout2)
                var.ui.tabAlquiler.setCellWidget(index, 5, container2)
                botonInforme.clicked.connect( lambda checked, idMensualidad=registro[0], idAlquilerInforme = idAlquiler: informes.Informes.reportReciboMes(idAlquilerInforme,idMensualidad))

        except Exception as e:
            print("Error al cargar tabla mensualidades",str(e))

    @staticmethod
    def pagarMensualidad(idMensualidad, checked,checkbox):
        """

        :param idMensualidad: identificador de la mensualidad
        :type idMensualidad: int
        :param checked: si esta marcado o no el botón checkbox de la tabla mensualidades
        :type checked: bool
        :param checkbox: referencia al boton checkbox de la tabla mensualidades
        :type checkbox: checkbox button

        Registra como pagada una mensualidad y mostrar los cambios en la tabla

        """
        if not checked:
            QtWidgets.QMessageBox.critical(None,"Error al pagar","No se puede modificar un recibo ya pagado.")
            checkbox.setChecked(True)
        elif conexion.Conexion.pagarMensualidad(idMensualidad):
            QtWidgets.QMessageBox.information(None,"Aviso","Se ha registrado el pago mensual.")
        else:
            QtWidgets.QMessageBox.critical(None,"Error","Se ha producido un error.")



