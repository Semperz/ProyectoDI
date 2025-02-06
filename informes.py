from datetime import datetime

from PyQt6 import QtSql
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPM
import os

import clientes
import conexion
import var
from PIL import Image



class Informes:
    num_paginas = 1
    total_paginas = 0

    @staticmethod
    def contarPaginas():
        query = QtSql.QSqlQuery()
        query.prepare('select count(*) from clientes')
        if query.exec():
            if query.next():
                total_registros = query.value(0)
                registros_por_pagina = 28  # Ajusta este valor según el número de registros por página
                Informes.total_paginas = (total_registros // registros_por_pagina) + (
                    1 if total_registros % registros_por_pagina > 0 else 0)

    @staticmethod
    def reportClientes():
        try:
            Informes.contarPaginas()
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nompdfcli = fecha + "_listadoclientes.pdf"
            pdf_path = os.path.join(rootPath, nompdfcli)
            var.report = canvas.Canvas(pdf_path)
            titulo = "Listado clientes"
            Informes.topInforme(titulo)

            items = ['DNI', 'APELLIDOS', 'NOMBRE', 'MOVIL', 'PROVINCIA', 'MUNICIPIO']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 650, str(items[0]))
            var.report.drawString(100, 650, str(items[1]))
            var.report.drawString(190, 650, str(items[2]))
            var.report.drawString(285, 650, str(items[3]))
            var.report.drawString(360, 650, str(items[4]))
            var.report.drawString(450, 650, str(items[5]))
            var.report.line(50, 645, 525, 645)

            query = QtSql.QSqlQuery()
            query.prepare('select dnicli, apelcli, nomecli, movilcli, provcli, municli from clientes'
                          ' order by apelcli')

            if query.exec():
                x = 55
                y = 635
                while query.next():
                    if y <= 90:
                        Informes.num_paginas += 1
                        Informes.footInforme(titulo)
                        var.report.setFont("Helvetica-Oblique", size=8)
                        var.report.drawString(450, 80, "Página siguiente...")
                        var.report.showPage()
                        Informes.num_paginas += 1
                        Informes.topInforme(titulo)
                        items = ['DNI', 'APELLIDOS', 'NOMBRE', 'MOVIL', 'PROVINCIA', 'MUNICIPIO']
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(55, 650, str(items[0]))
                        var.report.drawString(100, 650, str(items[1]))
                        var.report.drawString(190, 650, str(items[2]))
                        var.report.drawString(285, 650, str(items[3]))
                        var.report.drawString(360, 650, str(items[4]))
                        var.report.drawString(450, 650, str(items[5]))
                        var.report.line(50, 645, 525, 645)
                        x=55
                        y=625
                    var.report.setFont('Helvetica-Oblique', size=9)
                    dni = '***' + str(query.value(0))[4:7] + '***'
                    var.report.drawCentredString(x + 10, y, str(dni))
                    var.report.drawString(x + 45, y, str(query.value(1)))
                    var.report.drawString(x + 135, y, str(query.value(2)))
                    var.report.drawString(x + 230, y, str(query.value(3)))
                    var.report.drawString(x + 305, y, str(query.value(4)))
                    var.report.drawString(x + 395, y, str(query.value(5)))
                    y -= 20

            Informes.footInforme(titulo)
            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nompdfcli):
                    os.startfile(pdf_path)


        except Exception as e:
            print(e)


    def reportPropiedades(localidad):
        try:
            Informes.total_paginas = 1
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nompdfcli = fecha + "_listadopropiedades.pdf"
            pdf_path = os.path.join(rootPath, nompdfcli)
            var.report = canvas.Canvas(pdf_path)
            titulo = "Listado Propiedades de " + localidad
            Informes.topInforme(titulo)
            items = ['CODIGO', 'TIPO','DIRECCIÓN' ,'OPERACIÓN', 'VENTA (€)', 'ALQUILER (€)']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 650, str(items[0]))
            var.report.drawString(110, 650, str(items[1]))
            var.report.drawString(160, 650, str(items[2]))
            var.report.drawString(280, 650, str(items[3]))
            var.report.drawString(380, 650, str(items[4]))
            var.report.drawString(450, 650, str(items[5]))
            var.report.line(50, 645, 525, 645)

            query = QtSql.QSqlQuery()
            query.prepare('select idprop, tipoprop, dirprop, tipoperprop, prevenprop, prealquilerprop, estadoprop from propiedades'
                          ' where muniprop = :localidad'
                          ' order by idprop ')
            query.bindValue(':localidad', localidad)

            if query.exec():
                x = 55
                y = 635
                while query.next():
                    if y <= 90:
                        Informes.num_paginas += 1
                        Informes.footInforme(titulo)
                        var.report.setFont("Helvetica-Oblique", size=8)
                        var.report.drawString(450, 80, "Página siguiente...")
                        var.report.showPage()
                        Informes.num_paginas += 1
                        Informes.topInforme(titulo)
                        items = ['CODIGO', 'TIPO','DIRECCIÓN' ,'OPERACIÓN', 'VENTA (€)', 'ALQUILER (€)']
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(55, 650, str(items[0]))
                        var.report.drawString(110, 650, str(items[1]))
                        var.report.drawString(160, 650, str(items[2]))
                        var.report.drawString(280, 650, str(items[3]))
                        var.report.drawString(380, 650, str(items[4]))
                        var.report.drawString(450, 650, str(items[5]))
                        var.report.line(50, 645, 525, 645)
                        x=55
                        y=625
                    var.report.setFont('Helvetica-Oblique', size=9)
                    var.report.drawCentredString(x + 10, y, str(query.value(0)))
                    var.report.drawString(x + 45, y, str(query.value(1)))
                    var.report.drawString(x + 100, y, str(query.value(2)))
                    var.report.drawCentredString(x + 250, y, str(query.value(3)))
                    var.report.drawRightString(x + 370, y, str(query.value(4))+ "€")
                    var.report.drawRightString(x + 455, y, str(query.value(5))+ "€")
                    y -= 30

            Informes.footInforme(titulo)
            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nompdfcli):
                    os.startfile(pdf_path)
        except Exception as e:
            print("Error aqui",e)

    def footInforme(titulo):
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s / %s' % (var.report.getPageNumber(), Informes.total_paginas)))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    def topInforme(titulo):
        try:
            ruta_logo_svg = '.\\img\\icono.svg'
            ruta_logo_png = '.\\img\\icono.png'

            # Convertir SVG a PNG
            logo = svg2rlg(ruta_logo_svg)
            renderPM.drawToFile(logo, ruta_logo_png, fmt='PNG')

            # Cargar la imagen PNG
            logo = Image.open(ruta_logo_png)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Inmobiliaria Teis')
                var.report.drawCentredString(300, 675, titulo)
                var.report.line(50, 665, 525, 665)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo_png, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: inmoteis@gmail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo_png}')
        except Exception as error:
            print('Error en cabecera informe:', error)



    def reportVentas(idFac):
        try:
            Informes.total_paginas = 1
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nompdfcli = fecha + "_listadoVentas.pdf"
            pdf_path = os.path.join(rootPath, nompdfcli)
            var.report = canvas.Canvas(pdf_path)
            query = QtSql.QSqlQuery()
            query.exec("select fechafac from facturas where id = '" + idFac + "'")
            query.next()
            fechaFac = str(query.value(0))
            var.report.setFont('Helvetica', size=9)
            var.report.drawString(55, 670, 'Fecha Factura: ' + fechaFac)

            #Datos del cliente
            dni = var.ui.txtDnicliven.text()
            cliente = conexion.Conexion.datosOneCliente(dni)
            print(cliente)
            var.report.setFont('Helvetica-Bold', size=8)
            var.report.drawString(300, 770, 'DNI Cliente:')
            var.report.drawString(300, 752, 'Nombre:')
            var.report.drawString(300, 734, 'Dirección:')
            var.report.drawString(300, 716, 'Localidad:')
            var.report.setFont('Helvetica', size=8)
            var.report.drawString(360, 770, cliente[0])
            var.report.drawString(360, 752, cliente[3] + " " + cliente[2])
            var.report.drawString(360, 734, cliente[6])
            var.report.drawString(360, 716, cliente[8])

            titulo = "Factura " + str(idFac)
            Informes.topInforme(titulo)
            items = ['VENTA', 'PROPIEDAD', 'TIPO', 'DIRECCIÓN', 'LOCALIDAD', 'PRECIO']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 650, str(items[0]))
            var.report.drawString(100, 650, str(items[1]))
            var.report.drawString(200, 650, str(items[2]))
            var.report.drawString(260, 650, str(items[3]))
            var.report.drawString(365, 650, str(items[4]))
            var.report.drawString(480, 650, str(items[5]))
            var.report.line(50, 645, 525, 645)

            query = QtSql.QSqlQuery()
            query.prepare(
                "SELECT v.idventa, v.codprop, p.tipoprop, p.dirprop, p.muniprop, p.prevenprop FROM ventas as v "
                "INNER JOIN propiedades as p ON v.codprop = p.idprop where v.facventa = :facventa")
            query.bindValue(":facventa", idFac)

            if query.exec():
                total = 0
                x = 55
                y = 625
                while query.next():

                    var.report.setFont('Helvetica-Oblique', size=9)
                    var.report.drawCentredString(x + 10, y, str(query.value(0)))
                    var.report.drawString(x + 70, y, str(query.value(1)))
                    var.report.drawString(x + 140, y, str(query.value(2)))
                    var.report.drawString(x + 200, y, str(query.value(3)))
                    var.report.drawString(x + 310, y, str(query.value(4)))
                    compra = "-" if not str(query.value(5)) else str(query.value(5)) + '€'
                    var.report.drawRightString(x + 465, y, compra)
                    total += query.value(5)
                    y -= 30

                var.report.line(50, 110, 525, 110)
                var.report.drawString(400, 100, "Subtotal: ")
                var.report.drawString(400, 80, "Impuestos: ")
                var.report.drawString(400, 60, "Total: ")
                var.report.drawRightString(525, 100, str(total) + "€")
                var.report.drawRightString(525, 80, str(round(total * 0.1, 3)) + "€")
                var.report.drawRightString(525, 60, str(round(total * 1.1, 3)) + "€")

            Informes.footInforme(titulo)
            var.report.save()
            for file in os.listdir(rootPath):
                if file.endswith(nompdfcli):
                    os.startfile(pdf_path)
        except Exception as e:
            print("Error aqui", e)


