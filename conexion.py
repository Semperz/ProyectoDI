import os
import sqlite3
from datetime import datetime

from PyQt6 import QtSql, QtWidgets, QtCore
from PyQt6 import QtGui
import var


class Conexion:


    @staticmethod
    def db_conexion(self):
        """

        :param None
        :type None
        :return: False or True
        :rtype: Boolean

        Módulo de conexión a la base de datos
        Si exito True, else False

        """
        # Verifica si el archivo de base de datos existe
        if not os.path.isfile('bbdd.sqlite'):
            QtWidgets.QMessageBox.critical(None, 'Error', 'El archivo de la base de datos no existe.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        # Crear la conexión con la base de datos SQLite
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')

        if db.open():
            # Verificar si la base de datos contiene tablas
            query = QtSql.QSqlQuery()
            query.exec("SELECT name FROM sqlite_master WHERE type='table';")

            if not query.next():  # Si no hay tablas
                QtWidgets.QMessageBox.critical(None, 'Error', 'Base de datos vacía o no válida.',
                                               QtWidgets.QMessageBox.StandardButton.Cancel)
                return False
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('img/icono.svg'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Conexión Base de Datos realizada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                return True
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', 'No se pudo abrir la base de datos.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False

    @staticmethod
    def listarProvincias():
        """
        :return: lista provincias
        :rtype: bytearray

        Metodo que devuelve una lista de provincias
        """
        listaProv = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM provincias")
        if query.exec():
            while query.next():
                listaProv.append(query.value(1))
        return listaProv
    @staticmethod
    def listarMunicipios(provincia):
        """

        :param provincia:
        :type provincia: str
        :return: lista municipios
        :rtype: bytearray

        Metodo que devuelve una lista de municipios de una provincia
        """
        listaMuni = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM municipios"
                      " WHERE fk_idprov = (SELECT idprov FROM provincias WHERE provincia = :provincia)")
        query.bindValue(":provincia", provincia)
        if query.exec():
            while query.next():
                listaMuni.append(query.value(1))
        return listaMuni

    @staticmethod
    def listarMuniSinProv():
        """

        :return: lista municipios
        :rtype: bytearray
        """

        listaMuni = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM municipios")
        if not query.exec():
            print("Error ejecutando la consulta:", query.lastError().text())
        else:
            while query.next():
                listaMuni.append(query.value(1))
        return listaMuni

    def altaCliente(nuevoCli):
        """

        :return: true o false
        :rtype: boolean

        Metodo que da de alta un cliente en la base de datos
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into clientes (dnicli, altacli, apelcli, nomecli, emailcli, movilcli, "
                          " dircli, provcli, municli ) VALUES (:dnicli, :altacli, :apelcli, :nomecli, "
                          " :emailcli, :movilcli, :dircli, :provcli, :municli)")
            columnas = ['dnicli', 'altacli', 'apelcli', 'nomecli', 'emailcli', 'movilcli', 'dircli', 'provcli',
                        'municli']
            for i in range(len(columnas)):
                query.bindValue(":"+str(columnas[i]), nuevoCli[i])
            if query.exec():
                return True
            else:
                return False
        except sqlite3.IntegrityError:
            return False
    @staticmethod
    def listadoClientes():
        """

        :return: listado de clientes
        :rtype: bytearray

        """
        searchBtn = var.ui.btnBuscarcli.isChecked()
        DniCliente = var.ui.txtDnicli.text().upper()
        historicocli = var.ui.chkHistoriacli.isChecked()
        listado = []
        try:
            if searchBtn:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM clientes WHERE dnicli = :dnicli ORDER BY apelcli, nomecli ASC")
                query.bindValue(":dnicli", DniCliente)
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado
            if not historicocli:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM clientes WHERE bajacli is NULL ORDER BY apelcli, nomecli ASC ")
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado
            elif historicocli:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM clientes ORDER BY apelcli, nomecli ASC")
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado

        except Exception as e:
            print("error listado en conexión", e)

    def datosOneCliente(DNI):
        """
        :param dni cliente
        :type dni: str
        :return: datos de un cliente
        :rtype: bytearray

        Devuelve los datos de un cliente
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM clientes WHERE dnicli = :DNI")
            query.bindValue(":DNI", str(DNI))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("error datos un cliente", error)

    def modifCliente(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from clientes where dnicli = :dni")
            query.bindValue(":dni", str(registro[0]))
            if query.exec():
                if query.next() and query.value(0) > 0:
                    if query.exec():
                        query2 = QtSql.QSqlQuery()
                        query2.prepare("UPDATE clientes set altacli = :altacli, apelcli = :apelcli, nomecli = :nomecli, "
                                      " emailcli = :emailcli, movilcli = :movilcli, dircli = :dircli, provcli = :provcli, "
                                      " municli = :municli, bajacli = :bajacli where dnicli = :dnicli")
                        query2.bindValue(":dnicli", str(registro[0]))
                        query2.bindValue(":altacli", str(registro[1]))
                        query2.bindValue(":apelcli", str(registro[2]))
                        query2.bindValue(":nomecli", str(registro[3]))
                        query2.bindValue(":emailcli", str(registro[4]))
                        query2.bindValue(":movilcli", str(registro[5]))
                        query2.bindValue(":dircli", str(registro[6]))
                        query2.bindValue(":provcli", str(registro[7]))
                        query2.bindValue(":municli", str(registro[8]))
                        if registro[9] == "":
                            query2.bindValue(":bajacli", QtCore.QVariant())
                        else:
                            query2.bindValue(":bajacli", str(registro[9]))
                        if query2.exec():
                            print(query2.numRowsAffected())
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except Exception as error:
            print("error modificar cliente", error)

    def bajaCliente(datos):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE clientes set bajacli = :bajacli "
                          "where dnicli = :dnicli")
            query.bindValue(":bajacli", datetime.now().strftime("%d/%m/%Y"))
            query.bindValue(":dnicli", str(datos[1]))
            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error baja cliente", error)

    def clienteExistente(DNI):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT COUNT(*) FROM clientes WHERE dnicli = :DNI")
            query.bindValue(":DNI", str(DNI))
            if query.exec() and query.value(0) == 1:
                return True
            else:
                return False
        except Exception as error:
            print("error baja cliente", error)

    """
    Gestión de propiedades
    """

    def altaTipoprop(tipo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into tipoprop (tipo) VALUES (:tipo)")
            query.bindValue(":tipo", tipo)
            if query.exec():
                registro = Conexion.cargarTipoprop(self=None)
                return registro
            else:
                return False
        except Exception as error:
            print("error alta tipo", error)

    
    def bajaTipoprop(tipo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE from tipoprop where tipo = :tipo")
            query.bindValue(":tipo", tipo)
            if query.exec():
                query = QtSql.QSqlQuery()
                query.prepare("SELECT tipo FROM tipoprop order by tipo ASC")
                if query.exec():
                    registro = []
                    while query.next():
                        registro.append(str(query.value(0)))
                    return registro
            else:
                return False
        except Exception as error:
            print("error alta tipo", error)


    def cargarTipoprop(self):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM tipoprop order by tipo ASC")
            if query.exec():
                while query.next():
                    registro.append(str(query.value(0)))
                return registro
        except Exception as error:
            print("error cargar tipo", error)


    def altaPropiedad(propiedad):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into propiedades (fechaprop, dirprop, provpro, muniprop, tipoprop, "
                          " habprop, banosprop, superprop, prealquilerprop, prevenprop, CPprop, descriprop,"
                          "tipoperprop, estadoprop, nomeprop, movilprop ) VALUES (:fechaprop, :dirprop, :provpro, :muniprop, "
                          " :tipoprop, :habprop, :banosprop, :superprop, :prealquilerprop, :prevenprop, :CPprop,"
                          " :descriprop, :tipoperprop, :estadoprop, :nomeprop, :movilprop)")
            columnas = ['fechaprop', 'dirprop', 'provpro', 'muniprop', 'tipoprop'
                , 'habprop', 'banosprop', 'superprop', 'prealquilerprop', 'prevenprop'
                , 'CPprop', 'descriprop', 'tipoperprop', 'estadoprop', 'nomeprop', 'movilprop']
            for i in range(len(columnas)):
                if columnas[i] == 'habprop' or columnas[i] == 'banosprop' or columnas[i] == 'movilprop':
                    query.bindValue(":" + str(columnas[i]), int(propiedad[i]))
                elif columnas[i] == 'tipoperprop':
                    query.bindValue(":" + str(columnas[i]), ",".join((propiedad[i])))
                else:
                    query.bindValue(":" + str(columnas[i]), str(propiedad[i]))
            if query.exec():
                return True
            else:
                return False
        except sqlite3.IntegrityError:
            return False
    @staticmethod
    def listadoPropiedades():
        listado = []
        historicoprop = var.ui.chkHistoricoprop.isChecked()
        muniActual = var.ui.cmbMuniprop.currentText()
        tipoProp = var.ui.cmbTipoprop.currentText()
        searchBtn = var.ui.btnBuscartipoprop.isChecked()
        try:
            if historicoprop and not searchBtn:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM propiedades ORDER BY idprop ASC")
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado

            elif historicoprop and searchBtn:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM propiedades WHERE muniprop = :muniprop AND tipoprop = :tipoprop ORDER BY idprop ASC")
                query.bindValue(":muniprop", muniActual)
                query.bindValue(":tipoprop", tipoProp)
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado

            elif not historicoprop and searchBtn:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM propiedades WHERE bajaprop IS NULL AND muniprop = :muniprop AND tipoprop = :tipoprop "
                              "ORDER BY idprop ASC")
                query.bindValue(":muniprop", muniActual)
                query.bindValue(":tipoprop", tipoProp)
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado

            else:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM propiedades WHERE bajaprop IS NULL ORDER BY idprop ASC")
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado

        except Exception as e:
            print("error listado en conexión", e)

    def datosOnePropiedad(ID):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM propiedades WHERE idprop = :ID")
            query.bindValue(":ID", str(ID))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("error datos un cliente", error)


    def bajaPropiedad(datos):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE propiedades set bajaprop = :bajaprop "
                          "where idprop = :idprop")
            query.bindValue(":bajaprop", datetime.now().strftime("%d/%m/%Y"))
            query.bindValue(":idprop", str(datos[1]))
            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error baja propiedad", error)

    def modifPropiedad(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from propiedades where idprop = :idprop")
            query.bindValue(":idprop", int(registro[0]))
            if query.exec():
                if query.next() and query.value(0) > 0:
                    if query.exec():
                        query2 = QtSql.QSqlQuery()
                        query2.prepare("UPDATE propiedades set fechaprop = :fechaprop, bajaprop = :bajaprop, dirprop = :dirprop, provpro = :provpro, "
                                      " muniprop = :muniprop, tipoprop = :tipoprop, habprop = :habprop, banosprop = :banosprop, "
                                      " superprop = :superprop, prealquilerprop = :prealquilerprop, prevenprop = :prevenprop, CPprop = :CPprop, "
                                       "descriprop = :descriprop, tipoperprop = :tipoperprop, estadoprop = :estadoprop, nomeprop = :nomeprop, movilprop = :movilprop where idprop = :idprop")

                        columnas = ['idprop','fechaprop', 'bajaprop', 'dirprop', 'provpro', 'muniprop', 'tipoprop'
                            , 'habprop', 'banosprop', 'superprop', 'prealquilerprop', 'prevenprop'
                            , 'CPprop', 'descriprop', 'tipoperprop', 'estadoprop', 'nomeprop', 'movilprop']
                        for i in range(len(columnas)):
                            if columnas[i] == 'idprop' or  columnas[i] == 'habprop' or columnas[i] == 'banosprop' or columnas[i] == 'movilprop':
                                query2.bindValue(":" + str(columnas[i]), int(registro[i]))
                            elif columnas[i] == 'bajaprop':
                                if registro[2] == "":
                                    query2.bindValue(":bajaprop", QtCore.QVariant())
                                else:
                                    query2.bindValue(":" + str(columnas[i]), str(registro[i]))
                            elif columnas[i] == 'tipoperprop':
                                query2.bindValue(":" + str(columnas[i]), ",".join((registro[i])))
                            else:
                                query2.bindValue(":" + str(columnas[i]), str(registro[i]))

                        if query2.exec():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except Exception as error:
            print("error modificar cliente", error)
    @staticmethod
    def listadoAllPropiedades():
        listado = []
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM propiedades ORDER BY idprop ASC")
            if query.exec():
                while query.next():
                    fila = [query.value(i) for i in range(query.record().count())]
                    listado.append(fila)
            return listado
        except Exception as e:
            print("error listado en conexión", e)



    '''
    Pestaña vendedores
    '''


    def altaVendedor(nuevoVen):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into vendedor (dniVendedor, altaVendedor, nombreVendedor, mailVendedor, movilVendedor, "
                          " delegacionVendedor) VALUES (:dniVendedor, :altaVendedor, :nombreVendedor, :mailVendedor, "
                          " :movilVendedor, :delegacionVendedor)")
            columnas = ['dniVendedor', 'altaVendedor', 'nombreVendedor',
                        'mailVendedor', 'movilVendedor', 'delegacionVendedor']
            for i in range(len(columnas)):
                query.bindValue(":"+str(columnas[i]), nuevoVen[i])
            if query.exec():
                return True
            else:
                return False
        except sqlite3.IntegrityError:
            return False

    @staticmethod
    def listadoVendedores():
        searchBtn = var.ui.btnBuscarven.isChecked()
        movilven = var.ui.txtMovilven.text()
        historicoven = var.ui.chkHistoricoven.isChecked()
        listado = []
        try:
            if searchBtn:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM vendedor WHERE movilVendedor = :movilVendedor ORDER BY idVendedor ASC")
                query.bindValue(":movilVendedor", movilven)
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado
            if not historicoven:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM vendedor WHERE bajaVendedor is NULL ORDER BY idVendedor ASC ")
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado
            elif historicoven:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM vendedor ORDER BY idVendedor ASC")
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado

        except Exception as e:
            print("error listado en conexión", e)

    @staticmethod
    def listarDNIven():
        try:
            listaDNIs = []
            query = QtSql.QSqlQuery()
            query.prepare(
                "SELECT dniVendedor FROM vendedor")
            if query.exec():
                while query.next():
                    listaDNIs.append(query.value(0))
                return listaDNIs
            else:
                return []
        except sqlite3.IntegrityError:
            return False

    def modifVendedor(modifVen):

        try:

            query2 = QtSql.QSqlQuery()
            query2.prepare("UPDATE vendedor set altaVendedor = :altaVendedor, nombreVendedor = :nombreVendedor, "
                          " mailVendedor = :emailVendedor, movilVendedor = :movilVendedor, delegacionVendedor = :delegacionVendedor, "
                          " bajaVendedor = :bajaVendedor where dniVendedor = :dniVendedor")
            query2.bindValue(":dniVendedor", str(modifVen[0]))
            query2.bindValue(":altaVendedor", str(modifVen[1]))
            query2.bindValue(":nombreVendedor", str(modifVen[2]))
            query2.bindValue(":emailVendedor", str(modifVen[3]))
            query2.bindValue(":movilVendedor", str(modifVen[4]))
            query2.bindValue(":delegacionVendedor", str(modifVen[5]))
            if modifVen[6] == "":
                query2.bindValue(":bajaVendedor", QtCore.QVariant())
            else:
                query2.bindValue(":bajaVendedor", str(modifVen[6]))
            if query2.exec() and  query2.numRowsAffected()>0:
                return True
            else:
                return False
        except Exception as error:
            print("error modificar vendedor", error)


    def datosOneVendedor(idVen):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT idVendedor, dniVendedor, nombreVendedor, altaVendedor, bajaVendedor, movilVendedor, mailVendedor, delegacionVendedor"
                          " FROM vendedor WHERE idVendedor = :ID")
            query.bindValue(":ID", str(idVen))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("error datos un vendedor", error)

    def datosOneVendedorMovil(movilVen):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT dniVendedor, nombreVendedor, altaVendedor, bajaVendedor, movilVendedor, mailVendedor, delegacionVendedor"
                          " FROM vendedor WHERE movilVendedor = :movil")
            query.bindValue(":movil", str(movilVen))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("error datos un vendedor", error)


    def bajaVendedor(datos):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE vendedor set bajaVendedor = :bajaVendedor "
                          "where dniVendedor = :dniVendedor")
            query.bindValue(":bajaVendedor", datetime.now().strftime("%d/%m/%Y"))
            query.bindValue(":dniVendedor", str(datos[1]))
            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error baja cliente", error)


    '''
    Zona facturacion
    '''
    def altaFactura(factura):
        try:
            if factura[0] == "":
                factura[0] = datetime.now().strftime("%d/%m/%Y")
            if factura[1] == "":
                return False
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into facturas (fechafac, dnifac) VALUES (:fechaFactura, :dniCliente)")
            columnas = ['fechaFactura', 'dniCliente']
            for i in range(len(columnas)):
                query.bindValue(":"+str(columnas[i]), factura[i])
            if query.exec():
                return True
            else:
                return False
        except sqlite3.IntegrityError:
            return False

    @staticmethod
    def listadoFacturas():
        listado = []
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM facturas ORDER BY id ASC")
            if query.exec():
                while query.next():
                    fila = [query.value(i) for i in range(query.record().count())]
                    listado.append(fila)
            return listado
        except Exception as e:
            print("error listado facturas en conexión ", e)