from datetime import datetime

from PyQt6 import QtWidgets, QtGui, QtCore

import clientes
import conexion
import conexionserver
import eventos
import var

class Clientes:

    def checkDNI(dni):
        """

               :param dni: dni: dni a verificar
               :type dni: str

               Llama a eventos.Eventos.validarDNI para validar el dni pasado por parámetros
               Si no es valido, colorea de forma rojiza la caja de texto y borra el dni erróneo al hacer
               click en otro lado o darle al Intro

               """
        try:
            dni = str(dni).upper()
            var.ui.txtDnicli.setText(str(dni))
            check = eventos.Eventos.validarDNI(dni)
            if check:
                var.ui.txtDnicli.setStyleSheet("background-color: rgb(229, 255, 255);")
            else:
                var.ui.txtDnicli.setStyleSheet('background-color:#FFC0CB;')
                var.ui.txtDnicli.setText(None)
                var.ui.txtDnicli.setFocus()
        except Exception as e:
            print("error check cliente",e)

    def altaClientes(self):
        """

            :param self: clase clientes
            :type self: class

            Lee los datos del cliente de la interfaz
            comprueba si se verifican las restricciones necesarias y si se completaron todos los campos necesarios
            y llama a Conexion.altaCliente para guardar la información en la base de datos
            mostrando un mensaje con el resultado

               """

        try:

            # nuevoCliServer = [var.ui.txtDnicli.text(), var.ui.txtAltaCli.text(), var.ui.txtApelcli.text().title(), var.ui.txtNomcli.text().title(),var.ui.txtDircli.text().title(),
            #         var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.cmbProvcli.currentText(), var.ui.cmbMunicli.currentText()]
            nuevoCli = [var.ui.txtDnicli.text(), var.ui.txtAltaCli.text(), var.ui.txtApelcli.text(), var.ui.txtNomcli.text(),
                     var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(), var.ui.cmbProvcli.currentText(), var.ui.cmbMunicli.currentText()]
            camposObligatorios = [var.ui.txtDnicli.text(), var.ui.txtAltaCli.text(), var.ui.txtApelcli.text(), var.ui.txtNomcli.text(),
                                    var.ui.txtMovilcli.text(), var.ui.txtDircli.text(), var.ui.cmbProvcli.currentText(), var.ui.cmbMunicli.currentText()]
            for i in range(len(camposObligatorios)):
                if camposObligatorios[i] == "":
                    QtWidgets.QMessageBox.critical(None, 'Error', "Faltan campos por cubrir")
                    return
                else:
                    pass

            #if not conexionserver.ConexionServer.altaCliente(nuevoCliServer):
            if not conexion.Conexion.altaCliente(nuevoCli):
                QtWidgets.QMessageBox.critical(None, 'Error', "Ha ocurrido un error")
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("./img/icono.svg"))
                mbox.setWindowTitle('Aviso')
                mbox.setText("Cliente grabado en la base de datos")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Clientes.cargaTablaClientes(self)
                clientes.Clientes.clearCamposCliente()
        except Exception as e:
            print("error alta cliente",e)

    @staticmethod
    def clearCamposCliente():

        """

        Limpia los campos de texto de la interfaz de clientes

        """
        var.ui.txtDnicli.setText(None)
        var.ui.txtApelcli.setText(None)
        var.ui.txtNomcli.setText(None)
        var.ui.txtMovilcli.setText(None)
        var.ui.txtEmailcli.setText(None)
        var.ui.txtAltaCli.setText(None)
        var.ui.txtDircli.setText(None)
        var.ui.cmbProvcli.setCurrentIndex(0)

    def checkEmail(nuevo):
        """

        Lee el email de la caja de texto correspondiente de clientes
        y llama a eventos.Eventos.validarMail para comprobar si es válido
        Si no es valido, colorea de forma rojiza la caja de texto y borra el email erróneo al hacer
        click en otro lado o darle al Intro

        """
        try:
            mail = str(var.ui.txtEmailcli.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailcli.setStyleSheet('background-color: rgb(229, 255, 255);')
                var.ui.txtEmailcli.setText(mail.lower())

            else:
                var.ui.txtEmailcli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtEmailcli.setText(None)
                var.ui.txtEmailcli.setFocus()

        except Exception as error:
            print("error check cliente", error)

    def checkNumero(nuevo):

        """

            Lee el móvil de la caja de texto correspondiente de clientes
            y llama a eventos.Eventos.validarMovil para comprobar si es válido
            Si no es valido, colorea de forma rojiza la caja de texto y borra el numero erróneo al hacer
            click en otro lado o darle al Intro

               """
        try:
            telefono = str(var.ui.txtMovilcli.text())
            if eventos.Eventos.validarTelefono(telefono):
                var.ui.txtMovilcli.setStyleSheet('background-color: rgb(229, 255, 255);')
                var.ui.txtMovilcli.setText(telefono.lower())

            else:
                var.ui.txtMovilcli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtMovilcli.setText(None)
                var.ui.txtMovilcli.setFocus()
        except Exception as e:
            print("error check cliente", e)

    def cargaTablaClientes(self):
        """
            :param self: clase clientes
            :type self: class

            Recupera la lista de clientes mediante Conexion.listadoClientes
            y muestra dicha información en la tabla de clientes

               """
        try:
            var.ui.tablaClientes.setRowCount(0)
            listado = conexion.Conexion.listadoClientes()
            total_items = len(listado)
            start_index = var.current_page_cli * var.items_per_page_cli
            end_index = start_index + var.items_per_page_cli
            paginated_list = listado[start_index:end_index]
            #listado = conexionserver.ConexionServer.listadoClientes(self)

            for index, registro in enumerate(paginated_list):
                var.ui.tablaClientes.insertRow(index)
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(registro[0]))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[2]))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(registro[3]))
                var.ui.tablaClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(" " + " " + registro[5] + " " + " "))
                var.ui.tablaClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(registro[7]))
                var.ui.tablaClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(registro[8]))
                var.ui.tablaClientes.setItem(index, 6, QtWidgets.QTableWidgetItem(registro[9]))
                var.ui.tablaClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.btnSiguientecli.setEnabled(end_index < total_items)
            var.ui.btnAnteriorcli.setEnabled(var.current_page_cli > 0)
        except Exception as e:
            print("Error carga tabla clientes ", e)

    def siguientePaginaClientes(self):

        """

        :param self: clase clientes
        :type self: class

        Pasa a la siguiente pagina de clientes en caso de que la longitud pase de 15 elementos

        """
        var.current_page_cli += 1
        Clientes.cargaTablaClientes(self)


    def anteriorPaginaClientes(self):
        """

        :param self: clase clientes
        :type self: class

        Pasa a la pagina anterior de clientes en caso de que no sea la primera pagina

        """
        if var.current_page_cli > 0:
            var.current_page_cli -= 1
        Clientes.cargaTablaClientes(self)


    def cargaOneCliente(self):


        """

        :param self: clase clientes
        :type self: class

        Lee los datos del cliente seleccionado en la tabla clientes
        busca en la base de datos el resto de la información del cliente
        y la muestra en los elementos de la interfaz correspondientes

        """

        try:
            fila = var.ui.tablaClientes.selectedItems()
            datos =  [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneCliente(str(datos[0]))
            #registro = conexionserver.ConexionServer.datosOneCliente(str(datos[0]))
            #registro = [x if x != 'None' else '' for x in registro]
            listado = [var.ui.txtDnicli, var.ui.txtAltaCli, var.ui.txtApelcli, var.ui.txtNomcli,
              var.ui.txtEmailcli, var.ui.txtMovilcli, var.ui.txtDircli, var.ui.cmbProvcli, var.ui.cmbMunicli, var.ui.txtBajaCli]

            # listadoServer = [var.ui.txtDnicli, var.ui.txtAltaCli, var.ui.txtApelcli, var.ui.txtNomcli,
            #            var.ui.txtEmailcli, var.ui.txtDircli, var.ui.txtMovilcli , var.ui.cmbProvcli, var.ui.cmbMunicli,
            #            var.ui.txtBajaCli]
            '''
            Enlace con ventas
            '''
            var.ui.txtDnicliven.setText(registro[0])
            var.ui.lblFechafac.setText(None)
            var.ui.lblNumfac.setText(None)
            '''
            Enlace con alquileres
            '''
            var.ui.txtDniclialqui.setText(registro[0])
            var.ui.txtApelclialqui.setText(registro[2])
            var.ui.txtNomclialqui.setText(registro[3])


            for i in range(len(listado)):
                if i == 7 or i == 8:
                    listado[i].setCurrentText(registro[i])
                else:
                    listado[i].setText(registro[i])
            #Clientes.cargarCliente(registro)
        except Exception as error:
            print("error carga cliente",error)

    def modifCliente(self):

        """

        :param self: clase clientes
        :type self: class

        Lee los datos del cliente de la interfaz
        comprueba si se verifican las restricciones necesarias
        y llama a Conexion.modifCliente para modificar la información en la base de datos

        """

        try:
            modifcli = [var.ui.txtDnicli.text(), var.ui.txtAltaCli.text(), var.ui.txtApelcli.text(),
                        var.ui.txtNomcli.text(),
                        var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(),
                        var.ui.cmbProvcli.currentText(), var.ui.cmbMunicli.currentText(), var.ui.txtBajaCli.text()]

            # modifcliserver = [var.ui.txtAltaCli.text(), var.ui.txtApelcli.text().title(),
            #              var.ui.txtNomcli.text().title(),
            #                   var.ui.txtDircli.text().title(),
            #              var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(),
            #              var.ui.cmbProvcli.currentText(), var.ui.cmbMunicli.currentText(), var.ui.txtBajaCli.text(),
            #                   var.ui.txtDnicli.text()]
            #if conexionserver.ConexionServer.modifCliente(modifcliserver):
            validarFechaBaja = Clientes.checkFechaValidaCli()
            if (validarFechaBaja == False):
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "La fecha de baja no puede ser anterior a la fecha de alta.")

            elif conexion.Conexion.modifCliente(modifcli) and not conexion.Conexion.modifCliente(modifcli[0]):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Cliente modificado')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Clientes.cargaTablaClientes(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error cliente modificado')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Clientes.cargaTablaClientes(self)
            clientes.Clientes.cargaTablaClientes(self)
        except Exception as error:
            print("error al modificar clientes",error)

    def bajaCliente(self):
        """
            :param self: clase clientes
            :type self: class

            Lee el dni de la interfaz del cliente y llama a Conexion.bajaCliente
            para dar al vendedor de baja con la fecha actual

            """
        try:
            datos = [var.ui.txtBajaCli.text(), var.ui.txtDnicli.text()]
            #if conexionserver.ConexionServer.bajaCliente(datos):
            if conexion.Conexion.bajaCliente(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Cliente dado de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Clientes.cargaTablaClientes(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error baja cliente: Cliente no existe o ya está dado de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Clientes.cargaTablaClientes(self)
        except Exception as error:
            print("error bajaCliente", error)

    def historicoCli(self):

        """

        :param self: clase clientes
        :type self: class

        Recarga la tabla de clientes tras clickar el checkbox de histórico
        reseteando la página de la tabla clientes a cero para evitar problemas al mostrar datos

        """

        try:
            if var.ui.chkHistoriacli.isChecked():
                var.historico = 0
            else:
                var.historico = 1
            Clientes.cargaTablaClientes(self)
        except (Exception) as error:
            print("error al historico cliente",error)

    def cargaOneClienteBusqueda(self):
        """

        :param self: clase clientes
        :type self: class

        Lee el dni escrito en la caja de texto correspondiente de cliente
        busca la información del cliente asociado y la carga en los elementos de la interfaz

        """
        try:
            dni = var.ui.txtDnicli.text().upper()
            registro = conexion.Conexion.datosOneCliente(str(dni))
            if registro == []:
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "No existe esa persona.")
                var.ui.btnBuscarcli.setChecked(False)
                Clientes.cargaTablaClientes(self)

            else:
                listado = [var.ui.txtDnicli, var.ui.txtAltaCli, var.ui.txtApelcli, var.ui.txtNomcli,
                  var.ui.txtEmailcli, var.ui.txtMovilcli, var.ui.txtDircli, var.ui.cmbProvcli, var.ui.cmbMunicli, var.ui.txtBajaCli]
                for i in range(len(listado)):
                    if i == 7 or i == 8:
                        listado[i].setCurrentText(registro[i])
                    else:
                        listado[i].setText(registro[i])
        except Exception as error:
            print("error carga cliente",error)

    def filtroBusquedaCliente(self):

        """

        :param self: clase clientes
        :type self: class

        Recarga la tabla al buscar un cliente por DNI
        """
        try:
            Clientes.cargaTablaClientes(self)
            Clientes.cargaOneClienteBusqueda(self)
        except Exception as e:
            print(e)


    @staticmethod
    def checkFechaValidaCli():

        """

        :return: True si la fecha de baja es posterior a la fecha de alta, False en caso contrario
        :rtype: bool

        Comprueba si la fecha de baja es anterior a la fecha de alta
        """
        try:
            if var.ui.txtBajaCli.text() == "" or var.ui.txtBajaCli.text() is None:
                return True
            else:
                fechaBaja = datetime.strptime(var.ui.txtBajaCli.text(), "%d/%m/%Y")
                fechaAlta = datetime.strptime(var.ui.txtAltaCli.text(), "%d/%m/%Y")
                if fechaBaja < fechaAlta:
                    return False
                else:
                    return True

        except Exception as e:
            print("error check fecha baja", e)



