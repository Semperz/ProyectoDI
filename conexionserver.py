from datetime import datetime

import mysql.connector
from mysql.connector import Error
import os
from PyQt6 import QtSql, QtWidgets

import var


class ConexionServer():
    def crear_conexion(self):

        try:
            conexion = mysql.connector.connect(
            host='192.168.10.66', # Cambia esto a la IP de tu servidor user='dam', # Usuario creado
            #host='192.168.1.49',
            user='dam',
            password='dam2425',
            database='bbdd',
            charset="utf8mb4",
            collation="utf8mb4_general_ci"  # Asegúrate de que aquí esté configurado
            # Contraseña del usuario database='bbdd' # Nombre de la base de datos
            )
            if conexion.is_connected():
                pass
                #print("Conexión exitosa a la base de datos")
            return conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
        return None

    @staticmethod
    def listaProv():
        listaprov = []
        conexion = ConexionServer().crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM provincias")
                resultados = cursor.fetchall()
                for fila in resultados:
                    listaprov.append(fila[1])  # Asumiendo que el nombre de la provincia está en la segunda columna
                cursor.close()
                conexion.close()

            except Error as e:
                print(f"Error al ejecutar la consulta: {e}")
        return listaprov


    @staticmethod
    def listaMuniProv(provincia):
        try:
            conexion = ConexionServer().crear_conexion()
            listamunicipios = []
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT * FROM municipios WHERE idprov = (SELECT idprov FROM provincias WHERE provincia = %s)",
                (provincia,)
            )
            resultados = cursor.fetchall()
            for fila in resultados:
                listamunicipios.append(fila[1])  # Asumiendo que el nombre de la provincia está en la segunda columna
            cursor.close()
            conexion.close()
            return listamunicipios
        except Exception as error:
            print("error lista muni", error)

    def listadoClientes(self):
        try:
            if var.historico == 1:
                conexion = ConexionServer().crear_conexion()
                listadoclientes = []
                cursor = conexion.cursor()
                cursor.execute("SELECT dnicli, altacli, apelcli, nomecli, emailcli, movilcli, dircli, provcli, municli, bajacli"
                               " FROM clientes WHERE bajacli IS NULL ORDER BY apelcli, nomecli ASC")
                resultados = cursor.fetchall()
                for fila in resultados:      # Procesar cada fila de los resultados y crea una lista con valores de la fila
                    listadoclientes.append(list(fila))  # Convierte la tupla en una lista y la añade a listadoclientes
                cursor.close()    # Cerrar el cursor y la conexión si no los necesitas más
                conexion.close()
                return listadoclientes
            else:
                conexion = ConexionServer().crear_conexion()
                listadoclientes = []
                cursor = conexion.cursor()
                cursor.execute("SELECT dnicli, altacli, apelcli, nomecli, emailcli, movilcli, dircli, provcli, municli, bajacli"
                               " FROM clientes ORDER BY apelcli, nomecli ASC")
                resultados = cursor.fetchall()
                for fila in resultados:  # Procesar cada fila de los resultados y crea una lista con valores de la fila
                    listadoclientes.append(list(fila))  # Convierte la tupla en una lista y la añade a listadoclientes
                cursor.close()  # Cerrar el cursor y la conexión si no los necesitas más
                conexion.close()
                return listadoclientes
        except Exception as e:
            print("error listado en conexion", e)

    def altaCliente(cliente):
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                # Definir la consulta de inserción
                query = """
                INSERT INTO clientes (dnicli, altacli, apelcli, nomecli, dircli, emailcli, movilcli, provcli, municli)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, cliente)          # Ejecutar la consulta pasando la lista directamente
                conexion.commit()  # Confirmar la transacción
                cursor.close()   # Cerrar el cursor y la conexión
                conexion.close()
                return True
        except Error as e:
            print(f"Error al insertar el cliente: {e}")

    def datosOneCliente(dni):
        registro = []  # Inicializa la lista para almacenar los datos del cliente
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                # Definir la consulta de selección
                query = '''SELECT * FROM clientes WHERE dnicli = %s'''  # Usa %s para el placeholder
                cursor.execute(query, (dni,))  # Pasar 'dni' como una tupla
                # Recuperar los datos de la consulta
                for row in cursor.fetchall():
                    registro.extend([str(col) for col in row])
            return registro

        except Exception as e:
            print("Error al obtener datos de un cliente:", e)
            return None  # Devolver None en caso de error


    def bajaCliente(datos):
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                query = '''UPDATE clientes set bajacli = %s where dnicli = %s'''
                cursor.execute(query, (datetime.now().strftime("%d/%m/%Y"), datos[1]))
                conexion.commit()
                cursor.close()
                conexion.close()
                return True

        except Exception as error:
            print("error baja cliente", error)


    def modifCliente(cliente):
        try:
            conexion = ConexionServer().crear_conexion()
            cursor = conexion.cursor()
            query = """
                            select count(*) from clientes where dnicli = %s
                            """
            cursor.execute(query, (cliente[9],))
            if cursor.fetchone()[0] > 0:
                query = """
                UPDATE clientes SET altacli = %s, apelcli = %s, nomecli = %s, dircli = %s,
                 emailcli = %s, movilcli = %s, provcli = %s, municli = %s, bajacli = %s WHERE dnicli = %s
                """
                cursor.execute(query, cliente)          # Ejecutar la consulta pasando la lista directamente
                conexion.commit()  # Confirmar la transacción
                cursor.close()   # Cerrar el cursor y la conexión
                conexion.close()
                return True
            else:
                return False
        except Error as e:
            print(f"Error al insertar el cliente: {e}")

    @staticmethod
    def listadoPropiedades():
        filasProp = []
        listado = []
        historicoprop = var.ui.chkHistoricoprop.isChecked()
        try:
            if historicoprop:
                conexion = ConexionServer().crear_conexion()
                if conexion:
                    cursor = conexion.cursor()
                    query = "SELECT * FROM propiedades ORDER BY codigo ASC"
                    cursor.execute(query)
                    listado = cursor.fetchall()
                    conexion.commit()  # Confirmar la transacción
                    cursor.close()  # Cerrar el cursor y la conexión
                    conexion.close()


            else:
                conexion = ConexionServer().crear_conexion()
                if conexion:
                    cursor = conexion.cursor()
                    query = "SELECT * FROM propiedades WHERE bajaprop IS NULL ORDER BY codigo ASC"
                    cursor.execute(query)
                    listado = cursor.fetchall()
                    conexion.commit()  # Confirmar la transacción
                    cursor.close()  # Cerrar el cursor y la conexión
                    conexion.close()

            for row in listado:
                filasProp.append(row)
            return filasProp


        except Exception as e:
            print("error listado en conexión", e)
