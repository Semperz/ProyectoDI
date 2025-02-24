import csv
import json
import locale
import os.path

import sys
import time
import re
from datetime import datetime

from PyQt6 import QtWidgets, QtGui
import zipfile
import shutil

from PyQt6.uic.properties import QtCore

import alquileres
import facturas
import vendedores
import clientes
import conexion
import conexionserver
import propiedades
import var

#Establecer configuracion regional
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Eventos:



    def mensajeSalir(self=None):
        """

        Muestra un mensaje de confirmación para salir de la aplicación
        Si se marca si se cierra la aplicación
        """
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
    @staticmethod
    def cargarProv():
        """

        Carga la lista de provincias de la base de datos
        en los combobox de provincias de clientes

        """
        var.ui.cmbProvcli.clear()
        listado = conexion.Conexion.listarProvincias()
        #listado = conexionserver.ConexionServer.listaProv()
        var.ui.cmbProvcli.addItems(listado)
    @staticmethod
    def cargarMuni():
        """

        Carga la lista de municipios de la base de datos
        en los combobox de municipios de clientes dependiendo de la provincia que esté seleccionada
        """
        var.ui.cmbMunicli.clear()
        provActual = var.ui.cmbProvcli.currentText()
        listado = conexion.Conexion.listarMunicipios(provActual)
        #listado = conexionserver.ConexionServer.listaMuniProv(provActual)
        var.ui.cmbMunicli.addItems(listado)

    def validarDNI(dni):

        """
        :param: dni del cliente
        :type dni: str
        :return: éxito de la validación
        :rtype: bool
        """
        try:
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if dni.isdigit() and tabla[int(dni) % 23] == dig_control:
                    return True
                else:
                    return False
            else:
                return False

        except Exception as error:
            print("error en validar dni ", error)


    def abrirCalendar(op, btn):
        """

        :param: da un boton dependiendo del panel en el que se encuentre
        :type int

        Abre una ventana emergente del calendario, independiente para cada panel
        """
        try:
            var.panel=op
            var.btn = btn
            var.uicalendar.show()
        except Exception as error:
            print("error en abrir calendar ", error)

    def cargaFecha(qDate):


        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            if var.panel == 0 and var.btn == 0:
                var.ui.txtAltaCli.setText(str(data))
            elif var.panel == 0 and var.btn == 1:
                var.ui.txtBajaCli.setText(str(data))
            elif var.panel == 1 and var.btn == 0:
                    var.ui.txtFechaprop.setText(str(data))
            elif var.panel == 1 and var.btn == 1:
                    var.ui.txtFechabajaprop.setText(str(data))
            elif var.panel == 2 and var.btn == 0:
                    var.ui.txtAltaven.setText(str(data))
            elif var.panel == 2 and var.btn == 1:
                    var.ui.txtBajaven.setText(str(data))
            elif var.panel == 3 and var.btn == 0:
                var.ui.lblFechafac.setText(str(data))
            time.sleep(0.2)
            var.uicalendar.hide()
            return data
        except Exception as error:
            print("error en cargar fecha: ", error)


    def validarMail(mail):
        """

               :param mail: email a validar
               :type mail: str
               :return: resultado validación
               :rtype: bool

               Comprueba si el email sigue un formato válido

               """
        mail = mail.lower()
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, mail) or mail == "":
            return True
        else:
            return False

    def validarTelefono(telefono):
        """

              :param movil: móvil a validar
              :type movil: str
              :return: resultado validacion
              :rtype: bool

              Comprueba si el móvil sigue un formato válido para España

              """
        regex = r"^[67]\d{8}$"
        if re.match(regex, telefono):
            return True
        else:
            return False

    def validar_numero_decimal(string):
        """

               :param string: string a validar
               :type string: str
               :return: resultado validacion
               :rtype: bool

               Comprueba si el numero tipo string tiene 2 decimales

               """
        regex = r'^\d+(\.\d{1,2})?$'
        if re.match(regex, string):
            return True
        else:
            return False

    @staticmethod
    def resizeTablaClientes():
        try:
            header = var.ui.tablaClientes.horizontalHeader()
            for i in range(header.count()):
                if i not in (0,3,6):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_item = var.ui.tablaClientes.horizontalHeaderItem(i)
                font = header_item.font()
                font.setBold(True)
                header_item.setFont(font)
        except Exception as error:
            print("error en resize tabla clientes: ", error)



    def crearBackup(self):
        try:
            fecha = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            copia = str(fecha)+"_backup.zip"
            directorio, fichero = var.dlgabrir.getSaveFileName(None, "Guardar Copia Seguridad",copia, ".zip")
            print(directorio)
            if var.dlgabrir.accept and fichero:
                fichzip = zipfile.ZipFile(fichero, 'w')
                fichzip.write("bbdd.sqlite", os.path.basename("bbdd.sqlite"), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(fichero, directorio)
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("./img/icono.svg"))
                mbox.setWindowTitle('Copia seguridad')
                mbox.setText("Copia de seguridad guardada")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
        except Exception as error:
            print("error en crear backup: ", error)

    def restaurarBackup(self):
        try:
            filename = var.dlgabrir.getOpenFileName(None, "Restaurar Copia Seguridad", "", "*.zip;;All Files (*)")
            file = filename[0]
            if file:
                with zipfile.ZipFile(file, "r") as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("./img/icono.svg"))
                mbox.setWindowTitle('Copia seguridad')
                mbox.setText("Copia de seguridad restaurada")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                conexion.Conexion.db_conexion(self)
                Eventos.cargarProv()
                #conexionserver.ConexionServer.listadoClientes(self)
                clientes.Clientes.cargaTablaClientes(self)
        except Exception as error:
            print("error en restaurar backup: ", error)


    def limpiarPanel(self):
        if var.ui.panPrincipal.currentIndex() == 0:
            clientes.Clientes.clearCamposCliente()
        elif var.ui.panPrincipal.currentIndex() == 1:
            propiedades.Propiedades.clearCamposPropiedades()
            propiedades.Propiedades.checkDisponibilidad(self)
        elif var.ui.panPrincipal.currentIndex() == 2:
            vendedores.Vendedores.clearCamposVendedores()
        elif var.ui.panPrincipal.currentIndex() == 3:
            facturas.Facturas.clearCamposFacturas()
        elif var.ui.panPrincipal.currentIndex() == 4:
            facturas.Facturas.clearCamposFacturas()
        elif var.ui.panPrincipal.currentIndex() == 5:
            alquileres.Alquileres.clearCamposAlquileres()

    """
    Pagina propiedades
    """
    def abrirTipoprop(self):
        try:
            var.dlggestion.show()
        except Exception as error:
            print(error)

    def abrirBuscaLocal(self):
        try:
            var.dlgbuscalocal.show()
        except Exception as error:
            print(error)

    def abrirAboutprop(self):
        try:
            var.dlgabout.show()
        except Exception as error:
            print(error)

    def cerrarVentanaAbout(self):
        try:
            var.dlgabout.close()
        except Exception as error:
            print(error)


    @staticmethod
    def resizeTablaPropiedades():
        try:
            header = var.ui.tablaPropiedades.horizontalHeader()
            for i in range(header.count()):
                if i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

                header_item = var.ui.tablaPropiedades.horizontalHeaderItem(i)
                font = header_item.font()
                font.setBold(True)
                header_item.setFont(font)
        except Exception as e:
            print("error en resize tabla propiedades", e)

    @staticmethod
    def resizeTablaVentas():
        try:
            header = var.ui.tabVenta.horizontalHeader()
            for i in range(header.count()):
                if i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

                header_item = var.ui.tabVenta.horizontalHeaderItem(i)
                font = header_item.font()
                font.setBold(True)
                header_item.setFont(font)
        except Exception as e:
            print("error en resize tabla propiedades", e)

    def cargarTipoprop(self):
        try:
            registro = conexion.Conexion.cargarTipoprop(self)
            #registro = conexionserver.ConexionServer.cargarTipoprop(self)
            var.ui.cmbTipoprop.clear()
            var.ui.cmbTipoprop.addItems(registro)
        except Exception as e:
            print("error en cargar tipoprop", e)

    @staticmethod
    def cargarProvprop():
        var.ui.cmbProvprop.clear()
        listado = conexion.Conexion.listarProvincias()
        #listado = conexionserver.ConexionServer.listaProv()
        var.ui.cmbProvprop.addItems(listado)
    @staticmethod
    def cargarMuniprop():
        var.ui.cmbMuniprop.clear()
        provActual = var.ui.cmbProvprop.currentText()
        listado = conexion.Conexion.listarMunicipios(provActual)
        #listado = conexionserver.ConexionServer.listaMuniProv(provActual)
        var.ui.cmbMuniprop.addItems(listado)

    def buscarPorFiltro(self):
        if var.ui.panPrincipal.currentIndex() == 0:
            checked = var.ui.btnBuscarcli.isChecked()
            var.ui.btnBuscarcli.setChecked(not checked)
            clientes.Clientes.cargaTablaClientes(self)
            clientes.Clientes.cargaOneClienteBusqueda(self)
        elif var.ui.panPrincipal.currentIndex() == 1:
            checked = var.ui.btnBuscartipoprop.isChecked()
            var.ui.btnBuscartipoprop.setChecked(not checked)
            propiedades.Propiedades.filtroBusqueda(self)
        elif var.ui.panPrincipal.currentIndex() == 2:
            checked = var.ui.btnBuscarven.isChecked()
            var.ui.btnBuscarven.setChecked(not checked)
            vendedores.Vendedores.filtroBusquedaVendedor(self)





    def exportCSVprop(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime("%d-%m-%Y")
            file = (str(fecha) + "_DatosPropiedades.csv")
            directorio, fichero = var.dlgabrir.getSaveFileName(None, "Exportar datos en CSV", file, ".csv")
            if fichero:
                registros = conexion.Conexion.listadoPropiedades()
                with open(fichero, "w", newline="", encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["Codigo", "Alta", "Baja", "Dirección", "Provincia", "Municipio", "Tipo",
                                     "Nº Habitaciones", "Nº Baños", "Superficie", "Pecio alquiler", "Precio compra",
                                     "Código Postal", "Observaciones", "Operación", "Estado", "Propietario", "Móvil"])
                    for registro in registros:
                        writer.writerow(registro)
                shutil.move(fichero, directorio)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error al exportar a CSV')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
        except Exception as e:
            print("error en exportar propiedades", e)

    def exportCSVprop(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime("%d-%m-%Y")
            file = (str(fecha) + "_DatosPropiedades.csv")
            directorio, fichero = var.dlgabrir.getSaveFileName(None, "Exportar datos en CSV", file, ".csv")
            if fichero:
                registros = conexion.Conexion.listadoAllPropiedades()
                with open(fichero, "w", newline="", encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["Codigo", "Alta", "Baja", "Dirección", "Provincia", "Municipio", "Tipo",
                                     "Nº Habitaciones", "Nº Baños", "Superficie", "Pecio alquiler", "Precio compra",
                                     "Código Postal", "Observaciones", "Operación", "Estado", "Propietario",
                                     "Móvil"])
                    for registro in registros:
                        writer.writerow(registro)
                shutil.move(fichero, directorio)
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Exportado correctamente a CSV')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error al exportar a CSV')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
        except Exception as e:
            print("error en exportar propiedades", e)


    def exportJSONprop(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime("%d-%m-%Y")
            file = (str(fecha) + "_DatosPropiedades.json")
            directorio, fichero = var.dlgabrir.getSaveFileName(None, "Exportar datos en JSON", file, ".json")
            if fichero:
                keys = ["Codigo", "Alta", "Baja", "Dirección", "Provincia", "Municipio", "Tipo",
                                     "Nº Habitaciones", "Nº Baños", "Superficie", "Pecio alquiler", "Precio compra",
                                     "Código Postal", "Observaciones", "Operación", "Estado", "Propietario",
                                     "Móvil"]
                registros = conexion.Conexion.listadoAllPropiedades()
                listaPropiedades = [dict(zip(keys, registro)) for registro in registros]
                with open(fichero, "w", newline="", encoding="utf-8") as jsonfile:
                    json.dump(listaPropiedades, jsonfile, ensure_ascii=False, indent=4)
                shutil.move(fichero, directorio)
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Exportado correctamente a JSON')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error al exportar a JSON')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
        except Exception as e:
            print("error en exportar propiedades", e)

