import os
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
    def listarProvincias(self):
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
        except Exception as e:
            print(e)


