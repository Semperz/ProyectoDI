from datetime import datetime
from dlgCalendar import *
import eventos
import var


class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.uicalendar = Ui_dlgCalendar()
        var.uicalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year

        var.uicalendar.Calendar.setSelectedDate((QtCore.QDate(mes, ano, dia)))
        var.uicalendar.Calendar.clicked.connect(eventos.Eventos.cargaFecha)
