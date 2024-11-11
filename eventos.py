import locale
import os.path
import sys
import time
import re
from datetime import datetime

from PyQt6 import QtWidgets, QtGui
import zipfile
import shutil

import clientes
import conexion
import conexionserver
import eventos
import propiedades
import var


#Establecer configuracion regional
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

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
    @staticmethod
    def cargarProv():
        var.ui.cmbProvcli.clear()
        listado = conexion.Conexion.listarProvincias()
        #listado = conexionserver.ConexionServer.listaProv()
        var.ui.cmbProvcli.addItems(listado)
    @staticmethod
    def cargarMuni():
        var.ui.cmbMunicli.clear()
        provActual = var.ui.cmbProvcli.currentText()
        listado = conexion.Conexion.listarMunicipios(provActual)
        #listado = conexionserver.ConexionServer.listaMuniProv(provActual)
        var.ui.cmbMunicli.addItems(listado)

    def validarDNI(dni):
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
            time.sleep(0.2)
            var.uicalendar.hide()
            return data
        except Exception as error:
            print("error en cargar fecha: ", error)


    def validarMail(mail):
        mail = mail.lower()
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, mail) or mail == "":
            return True
        else:
            return False

    def validarTelefono(telefono):
        regex = r"^[67]\d{8}$"
        if re.match(regex, telefono):
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
                eventos.Eventos.cargarProv()
                #conexionserver.ConexionServer.listadoClientes(self)
                clientes.Clientes.cargaTablaClientes(self)
        except Exception as error:
            print("error en restaurar backup: ", error)


    def limpiarPanel(self):
        clientes.Clientes.clearCamposCliente()
        propiedades.Propiedades.clearCamposPropiedades()
        # objetosPanelCli = [var.ui.txtDnicli, var.ui.txtAltaCli, var.ui.txtApelcli,
        #             var.ui.txtNomcli,
        #             var.ui.txtEmailcli, var.ui.txtMovilcli, var.ui.txtDircli,
        #             var.ui.cmbProvcli, var.ui.cmbMunicli, var.ui.txtBajaCli]
        #
        # for i, dato in enumerate(objetosPanelCli):
        #     if i == 7 or i == 8:
        #         dato.setCurrentIndex(0)
        #     else:
        #         dato.setText(None)
        # eventos.Eventos.cargarProv()
    """
    Pagina propiedades
    """
    def abrirTipoprop(self):
        try:
            var.dlggestion.show()
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

    def cargarTipoprop(self):
        try:
            registro = conexion.Conexion.cargarTipoprop(self)
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

    def buscarPropiedadPorTipo(self):
        propiedades.Propiedades.filtroBusqueda(self)