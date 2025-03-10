import os
import sqlite3
from datetime import datetime

from PyQt6 import QtSql, QtWidgets, QtCore
from PyQt6 import QtGui
import var


class Conexion:


    @staticmethod
    def db_conexion():
        """

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

        :param: provincia
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

        :param: dni cliente
        :type dni: str
        :return: datos de un cliente
        :rtype: list

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
        """

        :param: datos del cliente a modificar
        :type registro: list
        :return: éxito de la operación
        :rtype: bool

        Modifica los datos de un cliente
        Devuelve true si se realiza correctamente, sino false

        """
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
        """

          :param: dni del cliente y fecha de baja
          :type datos: list
          :return: éxito de la operación
          :rtype: bool

          Da de baja al cliente
          No elimina al cliente de la base de datos
          Devuelve true si se realiza correctamente, sino false


        """
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


    """
    Gestión de propiedades
    """

    def altaTipoprop(tipo):
        """

        :param: nombre del tipo de propiedad
        :type tipo: str
        :return: operacion exitosa
        :rtype: bool

        Añade el tipo de propiedad, devolviendo true
        Devuelve false si ya existe

        """
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
        """

        :param: tipo de propiedad a eliminar
        :type tipo: str
        :return: operacion exitosa
        :rtype: bool

        Elimina el tipo de prop si existe, devolviendo true
        Devuelve false si no existe

        """
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
        """

        :return: listado de tipos de propiedad
        :rtype: list

        Devuelve los tipos de propiedades almacenados en la base de datos

        """
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
        """

         :param propiedad: datos de la propiedad a dar de alta
         :type propiedad: list
         :return: operacion exitosa
         :rtype: bool

         Da de alta una propiedad con los datos pasados por parámetro
         Devuelve true si la operación es exitosa, false en caso contrario

         """
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
        """

        :return: lista de propiedades registradas siguiendo condiciones
        :rtype: list

        Devuelve la lista de propiedades que existen en la base de datos
        siguiendo X condiciones (botón de historico, buscar por tipo de propiedad...)
        para mostrarla en la tabla

        """
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
        """

        :param: identificador de una propiedad
        :type ID: int
        :return: datos de la propiedad
        :rtype: list

        Devuelve la información de una propiedad a partir de su código identificativo

        """
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

        """

               :param: lista de código de la propiedad, y su fecha de baja
               :type datos: list
               :return: operación exitosa
               :rtype: bool

               Da de baja (no elimina) a la propiedad del código especificado
               devuelve true si la operación se realiza correctamente, false en caso contrario

        """
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
        """

               :param: datos modificados de la propiedad
               :type registro: list
               :return: operacion existosa
               :rtype: bool

               Modifica los datos de la propiedad pasada por parámetros
               Devuelve true si la operación se realiza correctamente, false en caso contrario

       """
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
        """

              :return: lista de todas las propiedades registradas
              :rtype: list

              Devuelve la lista de propiedades que existen en la base de datos

              """
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
        """

        :param: datos del nuevo vendedor
        :type nuevoVen: list
        :return: operacion exitosa
        :rtype: bool

        Graba un vendedor en la base de datos con la información del parámetro
        Devuelve true si se realiza correctamente, sino false

        """
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
        """

        :return: lista de vendedores
        :rtype: list

        Devuelve una lista con los datos de los vendedores de la base de datos

        """
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
        """

        :return: lista de vendedores
        :rtype: list

        Devuelve una lista con los dnis de vendedores existentes en la base de datos
        para comprobar si ya hay uno

        """
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
        """

        :param: datos del vendedor a modificar
        :type modifVen: list
        :return: operacion exitosa
        :rtype: bool

        Modifica los datos de un cliente con los pasados por parámetros
        Devuelve true si se realiza correctamente, sino false

        """
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
        """

        :param: id del vendedor a buscar
        :type idVen: int
        :return: datos de un vendedor
        :rtype: list

        Recupera la información del vendedor cuyo id es el pasado por parámetros

        """
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
        """

        :param: móvil del vendedor
        :type movilVen: str
        :return: datos del vendedor
        :rtype: list

        Recupera los datos de un cliente a partir de su móvil, pasado por parámetro

        """
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
        """

        :param: datos del vendedor a dar de baja
        :type datos: list
        :return: operacion exitosa
        :rtype: bool

        Da de baja al cliente especificado, poniendo la fecha del día actual
        No elimina al cliente de la base de datos
        Devuelve true si se realiza correctamente, sino false

        """
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
        """

         :param: dni del cliente y fecha de la factura
         :type factura: list
         :return: éxito de la operación
         :rtype: bool

         """
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
        """

        :return: lista de facturas
        :rtype: list

        Devuelve una lista con los datos de las facturas de la base de datos

        """
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



    def eliminarFactura(numFac):

        """

        :param: ID de la factura
        :type numFac: int
        :return: operacion exitosa
        :rtype: bool

        Elimina de la base de datos esa factura
        Devuelve true si se realiza correctamente, sino false

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM facturas WHERE id = :id")
            query.bindValue(":id", numFac)
            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error eliminar factura", error)


    def datosOneFactura(idFac):

        """

                :param: ID de la factura
                :type idFac: int
                :return: datos de la factura
                :rtype: list

                Recupera los datos de una factura y los devuelve en los campos correspondientes

                """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT id, fechafac, dnifac"
                          " FROM facturas WHERE id = :ID")
            query.bindValue(":ID", str(idFac))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("error datos una fac", error)


    def grabarVenta(nuevaventa):

        fechaventa = var.ui.lblFechafac.text()
        """

         :param: numero de la factura. codigo de la propiedad y el ID del vendedor
         :type nuevaventa: list
         :return: éxito de la operación
         :rtype: bool

         """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into ventas (facventa, codprop, agente)"
                          " VALUES (:facventa, :codprop, :agente)")
            columnas = ['facventa', 'codprop', 'agente']
            for i in range(len(columnas)):
                query.bindValue(":"+str(columnas[i]), nuevaventa[i])
            if query.exec():
                query.prepare("UPDATE propiedades set estadoprop = 'Vendido', bajaprop = :fechafac "
                              "where idprop = :idprop")
                query.bindValue(":idprop", nuevaventa[1])
                query.bindValue(":fechafac", fechaventa)
                if query.exec():
                    return True
                else:
                    return False
            else:
                return False
        except Exception as error:
            print("error grabar Venta", error)


    def listadoVentas(facventa):
        """

        :return: lista de ventas
        :rtype: list

        Devuelve una lista con los datos de las ventas de la base de datos

        """
        listado = []
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT v.idventa, v.codprop, p.dirprop, p.muniprop, p.tipoprop, p.prevenprop FROM ventas as v "
                          "INNER JOIN propiedades as p ON v.codprop = p.idprop where v.facventa = :facventa")
            query.bindValue(":facventa", facventa)
            if query.exec():
                while query.next():
                    fila = [query.value(i) for i in range(query.record().count())]
                    listado.append(fila)
            return listado
        except Exception as e:
            print("error listado ventas en conexión ", e)


    def datosOneVenta(idventa):

        """

                       :param: ID de la venta
                       :type idventa: int
                       :return: datos de la venta
                       :rtype: list

                       Recupera los datos de una venta y los devuelve en los campos correspondientes

                       """

        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare(
                "SELECT v.codprop, p.dirprop, p.muniprop, p.tipoprop, p.prevenprop, v.agente "
                "FROM ventas as v "
                "INNER JOIN propiedades as p ON v.codprop = p.idprop "
                "where v.idventa = :idventa")
            query.bindValue(":idventa", str(idventa))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("error datos una venta", error)


    def eliminarVenta(data):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM ventas WHERE idventa = :id")
            query.bindValue(":id", data[0])
            if query.exec():
                query.prepare("UPDATE propiedades SET estadoprop= 'Disponible', bajaprop = :baja where idprop = :idprop")
                query.bindValue(":baja", QtCore.QVariant())
                query.bindValue(":idprop", data[1])
                if query.exec():
                    return True
                else:
                    return False
            else:
                return False
        except Exception as error:
            print("error eliminar factura", error)


    '''
      GESTIÓN DE ALQUILERES
      '''

    @staticmethod
    def altaAlquiler(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                "INSERT INTO alquileres(propiedad_id,cliente_dni,fecha_inicio,fecha_fin,vendedor) values (:codigoprop,:dnicli,:fecha_inicio,:fecha_fin,:vendedor)")
            query.bindValue(":codigoprop", str(registro[0]))
            query.bindValue(":dnicli", str(registro[1]))
            query.bindValue(":fecha_inicio", str(registro[2]))
            query.bindValue(":fecha_fin", str(registro[3]))
            query.bindValue(":vendedor", str(registro[4]))
            if query.exec():
                query_propiedad = QtSql.QSqlQuery()
                query_propiedad.prepare(
                    "UPDATE propiedades SET estadoprop = 'Alquilado', bajaprop = :fecha_baja WHERE  idprop = :codigo")
                query_propiedad.bindValue(":codigo", str(registro[0]))
                query_propiedad.bindValue(":fecha_baja", str(registro[2]))
                if query_propiedad.exec():
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print("Error en altaAlquiler en conexion", e)

    @staticmethod
    def propiedadIsAlquilada(codigo):
        """

        :param codigo: codigo identificador de propiedad
        :type codigo: str
        :return: si la propiedad se encuentra alquilada o no
        :rtype: bool

        Comprobación de si una propiedad se encuentra alquilada o no

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT estado FROM propiedades WHERE codigo = :codigo")
            query.bindValue(":codigo", str(codigo))
            if query.exec() and query.next():
                estado = query.value(0)
                return estado == "Alquilado"
            else:
                return False
        except Exception as e:
            print("Error en propiedadIsVendida en conexion", str(e))

    @staticmethod
    def listadoAlquileres():
        try:
            listado = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT id, cliente_dni FROM alquileres")
            if query.exec():
                while query.next():
                    fila = [query.value(i) for i in range(query.record().count())]
                    listado.append(fila)
            return listado
        except Exception as e:
            print("Error listando alquileres en listadoAlquileres - conexión", str(e))

    @staticmethod
    def datosOneAlquiler(idAlquiler):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare(
                "SELECT a.id, a.fecha_inicio, a.fecha_fin, a.vendedor, c.dnicli, c.nomecli,"
                " c.apelcli, p.idprop, p.tipoprop, p.prealquilerprop, p.muniprop, p.dirprop "
                "FROM alquileres as a INNER JOIN propiedades as p "
                "ON a.propiedad_id = p.idprop "
                "INNER JOIN clientes as c "
                "ON a.cliente_dni = c.dnicli "
                "WHERE a.id = :idAlquiler")
            query.bindValue(":idAlquiler", str(idAlquiler))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as e:
            print("Error en datosOneAlquiler en conexion", str(e))

    @staticmethod
    def propiedadIsVendida(codigo):
        """

        :param codigo: codigo identificador de propiedad
        :type codigo: str
        :return: si la propiedad se encuentra vendida o no
        :rtype: bool

        Comprobar si una propiedad se encuentra vendida o no

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT estadoprop FROM propiedades WHERE idprop = :codigo")
            query.bindValue(":codigo", str(codigo))
            if query.exec() and query.next():
                estado = query.value(0)
                return estado == "Vendido"
            else:
                return False
        except Exception as e:
            print("Error en propiedadIsVendida en conexion", str(e))


    @staticmethod
    def eliminarAlquiler(idContrato):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("DELETE FROM mensualidades WHERE idalquiler = :id")
            query.bindValue(":id", idContrato)
            if not query.exec():
                return False
            query_prop = QtSql.QSqlQuery()
            query_prop.prepare(
                "UPDATE propiedades SET estadoprop = 'Disponible', bajaprop = NULL WHERE idprop = ( SELECT propiedad_id FROM alquileres WHERE id = :id) ")
            query_prop.bindValue(":id", idContrato)
            if not query_prop.exec():
                return False

            query_alq = QtSql.QSqlQuery()
            query_alq.prepare("DELETE FROM alquileres WHERE id = :id")
            query_alq.bindValue(":id", idContrato)
            if query_alq.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error eliminar alquiler", error)



    @staticmethod
    def altaMensualidad(registro):
        """

        :param registro: datos de una mensualidad
        :type registro: list
        :return: éxito al insertar una nueva mensualidad
        :rtype: bool

        Registra una nueva mensualidad respecto de un contrato de alquiler

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO mensualidades(idalquiler, mes, pagado) VALUES (:idalquiler,:mes,:pagado)")
            query.bindValue(":idalquiler", str(registro[0]))
            query.bindValue(":mes", str(registro[1]))
            query.bindValue(":pagado", str(registro[2]))
            if query.exec():
                return True
            else:
                return False
        except Exception as e:
            print("Error al grabar nueva mensualidad en conexion", str(e))

    @staticmethod
    def idOneAlquiler(codPropiedad, dniCliente):
        """

        :param codPropiedad: identificador de propiedad
        :type codPropiedad: int
        :param dniCliente: el identificador de un cliente, su DNI
        :type dniCliente: str
        :return: el identificador de un contrato de alquiler
        :rtype: id

        Obtiene el id de un contrato de alquiler en función del id de la propiedad y el id del cliente
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT id FROM alquileres WHERE cliente_dni = :dniCliente AND propiedad_id = :codPropiedad")
            query.bindValue(":dniCliente", str(dniCliente))
            query.bindValue(":codPropiedad", str(codPropiedad))
            if query.exec():
                while query.next():
                    return query.value(0)
        except Exception as e:
            print("Error en idOneAlquiler en conexion", str(e))


    @staticmethod
    def listarMensualidades(idAlq):
        """

                :param idAlq: identificador de un contrato de alquiler
                :type idAlq: int
                :return: todos los datos las mensualidades de un contrato de alquiler
                :rtype: list

                Obtiene todos los datos de las mensualidades relacionadas con un contrato de alquiler

                """
        try:
            listado = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT idmensualidad, mes, pagado FROM mensualidades WHERE idalquiler = :idalq")
            query.bindValue(":idalq", str(idAlq))
            if query.exec():
                while query.next():
                    fila = [query.value(i) for i in range(query.record().count())]
                    listado.append(fila)
            return listado
        except Exception as e:
            print("Error en listarMensualidades - conexion", str(e))

    @staticmethod
    def pagarMensualidad(idMensualidad):
        """

        :param idMensualidad: identificador de mensualidad
        :type idMensualidad: int
        :return: éxito al marcar como pagada una mensualidad
        :rtype: bool

        Registra en la base de datos el pago de una mensualidad

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE mensualidades SET pagado = 1 WHERE idmensualidad = :idMensualidad")
            query.bindValue(":idMensualidad", idMensualidad)
            if query.exec():
                return True
            else:
                return False
        except Exception as e:
            print("Error en pagar mensualidad", str(e))
