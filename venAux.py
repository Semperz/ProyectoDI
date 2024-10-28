from datetime import datetime
from dlgCalendar import *
import eventos
import var
from dlgGestionprop import *
from propiedades import Propiedades


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
        var.dlggestion = Ui_dlgTipoProp()
        var.dlggestion.setupUi(self)
        var.dlggestion.btnAltatipoprop.clicked.connect(Propiedades.altaTipopropiedad)
