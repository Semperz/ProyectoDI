from PyQt6 import QtWidgets, QtGui, QtCore
from datetime import datetime
import conexionserver
import eventos
import conexion
import propiedades
import var
from conexion import Conexion


class Propiedades():
    def altaTipoPropiedad(self):
        try:
            tipo =  var.dlggestion.ui.txtGestionprop.text().title()
            registro = conexion.Conexion.altaTipoprop(tipo)
            if registro:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad añadida a la base de datos')
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
                var.ui.cmbTipoprop.clear()
                var.ui.cmbTipoprop.addItems(registro)
                var.dlggestion.ui.txtGestionprop.setText("")
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad Existe')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
        except Exception as e:
            print(e)


    def bajaTipoPropiedad(self):
        try:
            tipo =  var.dlggestion.ui.txtGestionprop.text().title()
            registro = conexion.Conexion.bajaTipoprop(tipo)
            if registro:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad eliminada de la base de datos')
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
                var.ui.cmbTipoprop.clear()
                var.ui.cmbTipoprop.addItems(registro)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad no existente')
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
            var.dlggestion.ui.txtGestionprop.setText("")
        except Exception as e:
            print(e)



    def altaPropiedad(self):
        try:
            # propiedad = [var.ui.txtFechaprop.text(), var.ui.txtDirprop.text().title(), var.ui.cmbProvprop.currentText(),
            #              var.ui.cmbMuniprop.currentText(), var.ui.cmbTipoprop.currentText(),
            #              var.ui.spnHabprop.text(), var.ui.spnBanosprop.text(), var.ui.txtSuperprop.text(),
            #              var.ui.txtPrecioalquilerprop.text(), var.ui.txtPrecioventaprop.text(), var.ui.txtCPprop.text(),
            #              var.ui.areatxtDescriprop.toPlainText()]

            propiedad = [var.ui.txtFechaprop.text(), var.ui.txtDirprop.text().title(), var.ui.cmbProvprop.currentText(),
                         var.ui.cmbMuniprop.currentText(), var.ui.cmbTipoprop.currentText(),
                         var.ui.spnHabprop.text(), var.ui.spnBanosprop.text(), var.ui.txtSuperprop.text(),
                         var.ui.txtPrecioalquilerprop.text(), var.ui.txtPrecioventaprop.text(), var.ui.txtCPprop.text(),
                         var.ui.areatxtDescriprop.toPlainText()]

            validarFechaBaja = Propiedades.checkFechaValida()
            if (validarFechaBaja == False):
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "La fecha de baja no puede ser anterior a la fecha de alta.")
            elif var.ui.txtFechabajaprop.text().isalpha() or var.ui.txtFechaprop.text().isalpha():
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "La fecha de baja solo puede ser una fecha.")
            elif not eventos.Eventos.validar_numero_decimal(var.ui.txtPrecioventaprop.text()) or not eventos.Eventos.validar_numero_decimal(var.ui.txtPrecioalquilerprop.text()) or not '':
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "El precio solo puede ser un número.")
            elif not var.ui.txtCPprop.text().isdigit():
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "El código postal solo puede ser un número.")
            elif not eventos.Eventos.validar_numero_decimal(var.ui.txtSuperprop.text()):
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "La superficie solo puede ser un número.")
            else:
                tipooper = []
                if var.ui.chkAlquilerprop.isChecked():
                    tipooper.append(var.ui.chkAlquilerprop.text())
                if var.ui.chkVentaprop.isChecked():
                    tipooper.append(var.ui.chkVentaprop.text())
                if var.ui.chkInterprop.isChecked():
                    tipooper.append(var.ui.chkInterprop.text())
                propiedad.append(tipooper)
                if var.ui.rbtDisponibleprop.isChecked():
                    propiedad.append(var.ui.rbtDisponibleprop.text())
                if var.ui.rbtAlquiladoprop.isChecked():
                    propiedad.append(var.ui.rbtAlquiladoprop.text())
                if var.ui.rbtVendidoprop.isChecked():
                    propiedad.append(var.ui.rbtVendidoprop.text())

                propiedad.append(var.ui.txtNomeprop.text().title())
                propiedad.append(var.ui.txtMovilprop.text())

                if conexion.Conexion.altaPropiedad(propiedad):
                #if conexionserver.ConexionServer.altaPropiedad(propiedad):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon("./img/icono.svg"))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText("Propiedad grabada en la base de datos")
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Propiedades.cargaTablaPropiedades(self)
                    propiedades.Propiedades.clearCamposPropiedades()
                else:
                    QtWidgets.QMessageBox.critical(None, 'Error', "Faltan campos por cubrir o hay datos mal puestos.")
        except Exception as error:
            print(error)

    def checkNumeroProp(nuevo):
        try:
            telefono = str(var.ui.txtMovilprop.text())
            if eventos.Eventos.validarTelefono(telefono):
                var.ui.txtMovilprop.setStyleSheet('background-color: rgb(229, 255, 255);')
                var.ui.txtMovilprop.setText(telefono.lower())

            else:
                var.ui.txtMovilprop.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtMovilprop.setText(None)
                var.ui.txtMovilprop.setFocus()
        except Exception as e:
            print("error numero propiedad", e)

    def cargaTablaPropiedades(self):
         try:
            var.ui.tablaPropiedades.setRowCount(0)
            #listado = conexionserver.ConexionServer.listadoPropiedades()
            #listado = [x if x != 'None' else '' for x in listado]
            listado = conexion.Conexion.listadoPropiedades()
            total_items = len(listado)
            start_index = var.current_page_prop * var.items_per_page_prop
            end_index = start_index + var.items_per_page_prop
            paginated_list = listado[start_index:end_index] if listado else []
            var.ui.tablaPropiedades.setRowCount(len(paginated_list))
            if not listado:
                var.ui.tablaPropiedades.setRowCount(1)
                var.ui.tablaPropiedades.setItem(0, 2, QtWidgets.QTableWidgetItem("No hay propiedades que mostrar"))
                var.ui.tablaPropiedades.item(0, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            else:
                for index,registro in enumerate(paginated_list):
                    var.ui.tablaPropiedades.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                    var.ui.tablaPropiedades.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[5])))
                    var.ui.tablaPropiedades.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[6])))
                    var.ui.tablaPropiedades.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[7])))
                    var.ui.tablaPropiedades.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[8])))
                    if registro[10] == '' or registro[10] is None or registro == 0.0:
                        registro[10] = '-'
                    if registro[11] == '' or registro[10] is None or registro == 0.0:
                        registro[11] = '-'
                    var.ui.tablaPropiedades.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[10]) + " €"))
                    var.ui.tablaPropiedades.setItem(index, 6, QtWidgets.QTableWidgetItem(str(registro[11]) + " €"))
                    var.ui.tablaPropiedades.setItem(index, 7, QtWidgets.QTableWidgetItem(str(registro[14])))
                    var.ui.tablaPropiedades.setItem(index, 8, QtWidgets.QTableWidgetItem(str(registro[2])))
                    var.ui.tablaPropiedades.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tablaPropiedades.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                    var.ui.tablaPropiedades.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                    var.ui.tablaPropiedades.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tablaPropiedades.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tablaPropiedades.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tablaPropiedades.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tablaPropiedades.item(index, 7).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                    var.ui.tablaPropiedades.item(index, 8).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.btnSiguienteprop.setEnabled(end_index < total_items)
                var.ui.btnAnteriorprop.setEnabled(var.current_page_prop > 0)
         except Exception as e:
            print("Error carga tabla propiedades ", e)


    def siguientePaginaProp(self):
        var.current_page_prop += 1
        Propiedades.cargaTablaPropiedades(self)


    def anteriorPaginaProp(self):
        if var.current_page_prop > 0:
            var.current_page_prop -= 1
        Propiedades.cargaTablaPropiedades(self)


    def cargaOnePropiedad(self):
        try:
            fila = var.ui.tablaPropiedades.selectedItems()
            datos =  [dato.text() for dato in fila]
            #registro = conexionserver.ConexionServer.datosOnePropiedad(str(datos[0]))
            #registro = ["" if x == 'None' else x for x in registro]
            registro = conexion.Conexion.datosOnePropiedad(str(datos[0]))
            listado = [var.ui.txtFechaprop, var.ui.txtFechabajaprop, var.ui.txtDirprop, var.ui.cmbProvprop,
             var.ui.cmbMuniprop, var.ui.cmbTipoprop,
             var.ui.spnHabprop, var.ui.spnBanosprop, var.ui.txtSuperprop,
             var.ui.txtPrecioalquilerprop, var.ui.txtPrecioventaprop, var.ui.txtCPprop,
             var.ui.areatxtDescriprop, var.ui.chkAlquilerprop, var.ui.chkInterprop, var.ui.chkVentaprop,
             var.ui.rbtDisponibleprop, var.ui.rbtVendidoprop, var.ui.rbtAlquiladoprop]
            var.ui.lblIDprop.setText(registro[0])

            '''
            conexión con ventas
            '''
            var.ui.txtcodpropven.setText(registro[0])
            var.ui.txtTipopropven.setText(registro[6])
            var.ui.txtpreciopropven.setText(registro[11] + " €")
            var.ui.txtdirpropven.setText(registro[3])
            var.ui.txtlocalpropven.setText(registro[5])

            for i in range(len(listado)):
                if i == 3 or i == 4 or i == 5:
                    listado[i].setCurrentText(registro[i + 1])
                elif i == 6 or i == 7:
                    listado[i].setValue(int(registro[i + 1]))
                elif i == 13 or i == 14 or i == 15 :
                    if 'Alquiler' in (registro[14]):
                        listado[13].setChecked(True)
                    else:
                        listado[13].setChecked(False)
                    if 'Intercambio' in (registro[14]):
                        listado[14].setChecked(True)
                    else:
                        listado[14].setChecked(False)
                    if 'Venta' in (registro[14]):
                        listado[15].setChecked(True)
                    else:
                        listado[15].setChecked(False)
                elif i == 16 or i == 17 or i == 18:
                    if 'Disponible' in (registro[15]):
                        listado[16].setChecked(True)
                    if 'Vendido' in (registro[15]):
                        listado[17].setChecked(True)
                    if 'Alquilado' in (registro[15]):
                        listado[18].setChecked(True)
                else:
                    listado[i].setText(str(registro[i + 1]))
                var.ui.txtNomeprop.setText(registro[16])
                var.ui.txtMovilprop.setText(registro[17])
        except Exception as error:
            print("error carga propiedad",error)

    def bajaPropiedad(self):
        try:
            datos = [var.ui.txtFechabajaprop.text(), var.ui.lblIDprop.text()]
            if conexion.Conexion.bajaPropiedad(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad dada de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Propiedades.cargaTablaPropiedades(self)
                propiedades.Propiedades.clearCamposPropiedades()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error baja propiedad: Propiedad no existe o ya está dada de baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Propiedades.cargaTablaPropiedades(self)
        except Exception as error:
            print("error baja propiedad", error)

    @staticmethod
    def clearCamposPropiedades():
        var.ui.lblIDprop.setText(None)
        var.ui.txtFechaprop.setText(None)
        var.ui.txtFechabajaprop.setText(None)
        var.ui.txtDirprop.setText(None)
        var.ui.cmbProvprop.setCurrentIndex(0)
        var.ui.cmbTipoprop.setCurrentIndex(0)
        var.ui.spnHabprop.setValue(0)
        var.ui.spnBanosprop.setValue(0)
        var.ui.txtSuperprop.setText(None)
        var.ui.txtPrecioalquilerprop.setText(None)
        var.ui.txtPrecioventaprop.setText(None)
        var.ui.txtCPprop.setText(None)
        var.ui.areatxtDescriprop.setText(None)
        var.ui.chkVentaprop.setChecked(False)
        var.ui.chkInterprop.setChecked(False)
        var.ui.chkAlquilerprop.setChecked(False)
        var.ui.rbtDisponibleprop.setChecked(True)
        var.ui.rbtAlquiladoprop.setChecked(False)
        var.ui.rbtVendidoprop.setChecked(False)
        var.ui.txtNomeprop.setText(None)
        var.ui.txtMovilprop.setText(None)


    def modifProp(self):
        try:
            modifprop = [var.ui.lblIDprop.text(), var.ui.txtFechaprop.text(), var.ui.txtFechabajaprop.text(),
                         var.ui.txtDirprop.text(), var.ui.cmbProvprop.currentText(),
                         var.ui.cmbMuniprop.currentText(), var.ui.cmbTipoprop.currentText(),
                         var.ui.spnHabprop.text(), var.ui.spnBanosprop.text(), var.ui.txtSuperprop.text(),
                         var.ui.txtPrecioalquilerprop.text(), var.ui.txtPrecioventaprop.text(),
                         var.ui.txtCPprop.text(), var.ui.areatxtDescriprop.toPlainText()]

            validarFechaBaja = Propiedades.checkFechaValida()
            if (validarFechaBaja == False):
                QtWidgets.QMessageBox.critical(None, 'Error', "La fecha de baja no puede ser anterior a la fecha de alta.")

            elif var.ui.txtFechabajaprop.text().isalpha() or var.ui.txtFechaprop.text().isalpha():
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "La fecha de baja solo puede ser una fecha.")
            elif not eventos.Eventos.validar_numero_decimal(
                    var.ui.txtPrecioventaprop.text()) or not eventos.Eventos.validar_numero_decimal(
                    var.ui.txtPrecioalquilerprop.text()):
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "El precio solo puede ser un número.")
            elif not var.ui.txtCPprop.text().isdigit():
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "El código postal solo puede ser un número.")
            elif not eventos.Eventos.validar_numero_decimal(var.ui.txtSuperprop.text()):
                QtWidgets.QMessageBox.critical(None, 'Error',
                                               "La superficie solo puede ser un número.")
            else:
                tipooper = []
                if var.ui.chkAlquilerprop.isChecked():
                    tipooper.append(var.ui.chkAlquilerprop.text())
                if var.ui.chkVentaprop.isChecked():
                    tipooper.append(var.ui.chkVentaprop.text())
                if var.ui.chkInterprop.isChecked():
                    tipooper.append(var.ui.chkInterprop.text())
                modifprop.append(tipooper)
                if var.ui.rbtDisponibleprop.isChecked():
                    modifprop.append(var.ui.rbtDisponibleprop.text())
                if var.ui.rbtAlquiladoprop.isChecked():
                    modifprop.append(var.ui.rbtAlquiladoprop.text())
                if var.ui.rbtVendidoprop.isChecked():
                    modifprop.append(var.ui.rbtVendidoprop.text())

                modifprop.append(var.ui.txtNomeprop.text())
                modifprop.append(var.ui.txtMovilprop.text())



                if conexion.Conexion.modifPropiedad(modifprop):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText('Propiedad modificada')
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Propiedades.cargaTablaPropiedades(self)

                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                    mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText('Error propiedad modificada')
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Propiedades.cargaTablaPropiedades(self)
                Propiedades.cargaTablaPropiedades(self)
        except Exception as error:
            print("error al modificar propiedades",error)

    def filtroBusqueda(self):
        try:
            Propiedades.cargaTablaPropiedades(self)
        except Exception as e:
            print(e)

    def filtroBusquedaHistorico(self):
        try:
            Propiedades.cargaTablaPropiedades(self)
        except Exception as e:
            print(e)


    def checkDisponibilidad(self):

        """

        Habilita o desabilita los botones de radio de disponibilidad
        según haya fecha de baja en la caja de texto o no y los de precio si hay precio
        en la caja de texto o no

        """
        try:
            if var.ui.txtFechabajaprop.text() == "":
                var.ui.rbtDisponibleprop.setEnabled(True)
                var.ui.rbtVendidoprop.setEnabled(False)
                var.ui.rbtAlquiladoprop.setEnabled(False)
                var.ui.rbtDisponibleprop.setChecked(True)
            else:
                var.ui.rbtDisponibleprop.setEnabled(False)
                var.ui.rbtVendidoprop.setEnabled(True)
                var.ui.rbtAlquiladoprop.setEnabled(True)
                var.ui.rbtVendidoprop.setChecked(True)


            if var.ui.txtPrecioventaprop.text() == "":
                var.ui.chkVentaprop.setChecked(False)
                var.ui.chkVentaprop.setEnabled(False)
            else:
                var.ui.chkVentaprop.setChecked(True)
                var.ui.chkVentaprop.setEnabled(True)

            if var.ui.txtPrecioalquilerprop.text() == "":
                var.ui.chkAlquilerprop.setChecked(False)
                var.ui.chkAlquilerprop.setEnabled(False)
            else:
                var.ui.chkAlquilerprop.setChecked(True)
                var.ui.chkAlquilerprop.setEnabled(True)
        except Exception as error:
            print("error al disponibilidad",error)

    @staticmethod
    def checkFechaValida():
        try:
            if var.ui.txtFechabajaprop.text() == "" or var.ui.txtFechabajaprop.text() is None:
                return True
            else:
                fechaBaja = datetime.strptime(var.ui.txtFechabajaprop.text(), "%d/%m/%Y")
                fechaAlta = datetime.strptime(var.ui.txtFechaprop.text(), "%d/%m/%Y")
                if fechaBaja < fechaAlta:
                    return False
                else:
                    return True

        except Exception as e:
            print("error check fecha baja", e)

