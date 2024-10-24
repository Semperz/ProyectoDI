from calendar import Calendar

import conexionserver
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
        var.dlgabrir = FileDialogAbrir()
        self.setStyleSheet(styles.load_stylesheet())
        conexion.Conexion.db_conexion(self)
        var.historico = 0
        #conexionserver.ConexionServer.crear_conexion(self)
        clientes.Clientes.cargaTablaClientes(self)
        '''
        eventos de tablas
        '''
        eventos.Eventos.resizeTablaClientes()
        var.ui.tablaClientes.clicked.connect(clientes.Clientes.cargaOneCliente)

        '''
        zona de eventos del menubar
        '''
        var.ui.actSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionCrear_Backup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(eventos.Eventos.restaurarBackup)
        var.ui.actionTipo_de_propiedades.triggered.connect(eventos.Eventos.abrirTipoprop)
        '''
        eventos de botones
        '''
        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaClientes)
        var.ui.btnAltaCli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0, 0))
        var.ui.btnBajaCli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0, 1))
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifCliente)
        var.ui.btnDelcli.clicked.connect(clientes.Clientes.bajaCliente)

        '''
        eventos de cajas de texto
        '''
        var.ui.txtDnicli.editingFinished.connect(lambda: clientes.Clientes.checkDNI(var.ui.txtDnicli.text()))
        var.ui.txtEmailcli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailcli.text()))
        var.ui.txtMovilcli.editingFinished.connect(lambda: clientes.Clientes.checkNumero(var.ui.txtMovilcli.text()))
        '''
        combobox events
        '''
        eventos.Eventos.cargarProv()
        eventos.Eventos.cargarMuni()
        var.ui.cmbProvcli.currentIndexChanged.connect(eventos.Eventos.cargarMuni)

        '''
        eventos del ToolBar
        '''
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionbarLimpiar.triggered.connect(eventos.Eventos.limpiarPanel)

        '''
        eventos checkBox
        '''
        var.ui.chkHistoriacli.stateChanged.connect(clientes.Clientes.historicoCli)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())