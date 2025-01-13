from calendar import calendar
from datetime import datetime

import informes
import propiedades
from dlgAbout import Ui_windowAbout
from dlgBuscaLocal import Ui_dlgBuscaLocal
from dlgCalendar import *
import eventos
import var
from dlgGestionprop import *



class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.uicalendar = Ui_dlgCalendar()
        var.uicalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year

        var.uicalendar.Calendar.setSelectedDate((QtCore.QDate(dia, mes, ano)))
        var.uicalendar.Calendar.clicked.connect(eventos.Eventos.cargaFecha)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()

class dlgGestionprop(QtWidgets.QDialog):
    def __init__(self):
        super(dlgGestionprop, self).__init__()
        self.ui = Ui_dlgTipoProp()
        self.ui.setupUi(self)
        self.ui.btnAltatipoprop.clicked.connect(propiedades.Propiedades.altaTipoPropiedad)
        self.ui.btnBajatipoprop.clicked.connect(propiedades.Propiedades.bajaTipoPropiedad)


class dlgAboutprop(QtWidgets.QDialog):
    def __init__(self):
        super(dlgAboutprop, self).__init__()
        self.ui = Ui_windowAbout()
        self.ui.setupUi(self)
        self.ui.btnCerrar.clicked.connect(eventos.Eventos.cerrarVentanaAbout)

class dlgBuscaLocal(QtWidgets.QDialog):
    def __init__(self):
        super(dlgBuscaLocal, self).__init__()
        self.ui = Ui_dlgBuscaLocal()
        self.ui.setupUi(self)
        self.ui.btnGenInforme.clicked.connect(informes.Informes.reportPropiedades)
