import os
import sqlite3

from PyQt6 import QtSql, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtGui

class Conexion:

    '''

    méttodo de una clase que no depende de una instancia específica de esa clase.
    Se puede llamarlo directamente a través de la clase, sin necesidad de crear un objeto de esa clase. 
    Es útil en comportamientos o funcionalidades que son más a una clase en general que a una instancia en particular.
    
    '''

    @staticmethod
    def db_conexion(self):
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
                QtWidgets.QMessageBox.information(None, 'Aviso', 'Conexión Base de Datos realizada',
                                               QtWidgets.QMessageBox.StandardButton.Ok)
                return True
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', 'No se pudo abrir la base de datos.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False

    @staticmethod
    def listarProvincias():
        listaProv = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM provincias")
        if query.exec():
            while query.next():
                listaProv.append(query.value(1))
        return listaProv
    @staticmethod
    def listarMunicipios(provincia):
        listaMuni = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM municipios"
                      " WHERE fk_idprov = (SELECT idprov FROM provincias WHERE provincia = :provincia)")
        query.bindValue(":provincia", provincia)
        if query.exec():
            while query.next():
                listaMuni.append(query.value(1))
        return listaMuni

    def altaCliente(nuevoCli):
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
        try:
            listado = []
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
            query.prepare("UPDATE clientes set altacli = :altacli, apelcli = :apelcli, nomecli = :nomecli, emailcli = :emailcli,"
                          "movilcli = :movilcli, dircli = :dircli, provcli = :provcli, municli = :municli, bajacli = :bajacli"
                          "where dnicli = :dnicli")
            columnas = ['dnicli', 'altacli', 'apelcli', 'nomecli', 'emailcli', 'movilcli', 'dircli', 'provcli',
                        'municli', 'bajacli']
            for i in range(len(columnas)):
                query.bindValue(":" + str(columnas[i]), str(registro[i]))
            if query.exec():
                return True
            else:
                return False
        except Exception as error:
            print("error modificar cliente", error)

    def bajaCliente(datos):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE clientes set bajacli = :bajacli "
                          "where dnicli = :dnicli")
            query.bindValue(":bajacli", str(datos[0]))
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
