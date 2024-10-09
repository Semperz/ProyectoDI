from calendar import Calendar
from venAux import *
import clientes
import conexion
import eventos
import styles
from venPrincipal import *
import sys
import var

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        var.uicalendar = Calendar()
        self.setStyleSheet(styles.load_stylesheet())
        conexion.Conexion.db_conexion(self)
        eventos.Eventos.cargarProv(self)
        eventos.Eventos.cargarMuni(self)

        '''
        zona de eventos del menubar
        '''
        var.ui.actSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        '''
        eventos de botones
        '''
        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaClientes)
        var.ui.btnAltaCli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0))

        '''
        eventos de cajas de texto
        '''
        var.ui.txtDnicli.editingFinished.connect(lambda: clientes.Clientes.checkDNI(var.ui.txtDnicli.text()))
        var.ui.txtEmailcli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailcli.text()))
        var.ui.txtMovilcli.editingFinished.connect(lambda: clientes.Clientes.checkNumero(var.ui.txtMovilcli.text()))
        '''
        combobox events
        '''
        var.ui.cmbProvcli.currentIndexChanged.connect(eventos.Eventos.cargarMuni)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())