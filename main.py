from calendar import Calendar

import conexionserver
import informes
import propiedades
import vendedores
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
        var.dlggestion = dlgGestionprop()
        var.dlgabout = dlgAboutprop()
        var.dlgbuscalocal = dlgBuscaLocal()
        self.setStyleSheet(styles.load_stylesheet())
        conexion.Conexion.db_conexion(self)
        var.historico = 0
        var.current_page_cli = 0
        var.current_page_prop = 0
        var.items_per_page_cli = 15
        var.items_per_page_prop = 15
        #conexionserver.ConexionServer.crear_conexion(self)
        clientes.Clientes.cargaTablaClientes(self)
        vendedores.Vendedores.cargarTablaVendedores(self)
        propiedades.Propiedades.cargaTablaPropiedades(self)
        propiedades.Propiedades.checkDisponibilidad(self)
        '''
        Eventos formulario
        '''
        var.ui.txtFechabajaprop.textChanged.connect(propiedades.Propiedades.checkDisponibilidad)
        var.ui.txtPrecioventaprop.textChanged.connect(propiedades.Propiedades.checkDisponibilidad)
        var.ui.txtPrecioalquilerprop.textChanged.connect(propiedades.Propiedades.checkDisponibilidad)

        '''
        eventos de tablas
        '''
        eventos.Eventos.resizeTablaClientes()
        eventos.Eventos.resizeTablaPropiedades()
        vendedores.Vendedores.resizeTablaVendedores()

        var.ui.tablaVendedores.clicked.connect(vendedores.Vendedores.cargaOneVendedor)
        var.ui.tablaClientes.clicked.connect(clientes.Clientes.cargaOneCliente)
        var.ui.tablaPropiedades.clicked.connect(propiedades.Propiedades.cargaOnePropiedad)
        '''
        zona de eventos del menubar
        '''
        var.ui.actSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionCrear_Backup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(eventos.Eventos.restaurarBackup)
        var.ui.actionTipo_de_propiedades.triggered.connect(eventos.Eventos.abrirTipoprop)
        var.ui.actionExportar_Clientes_CSV.triggered.connect(eventos.Eventos.exportCSVprop)
        var.ui.actionExportar_Clientes_JSON.triggered.connect(eventos.Eventos.exportJSONprop)
        var.ui.actionAcercade.triggered.connect(eventos.Eventos.abrirAboutprop)

        var.ui.actionListado_Clientes.triggered.connect(informes.Informes.reportClientes)
        var.ui.actionListado_Propiedades.triggered.connect(eventos.Eventos.abrirBuscaLocal)
        '''
        eventos de botones
        '''
        var.ui.btnAltaven.clicked.connect(vendedores.Vendedores.altaVendedores)
        var.ui.btnFechaaltaven.clicked.connect(lambda: eventos.Eventos.abrirCalendar(2,0))
        var.ui.btnFechabajaven.clicked.connect(lambda: eventos.Eventos.abrirCalendar(2,1))
        var.ui.btnBajaven.clicked.connect(vendedores.Vendedores.bajaVendedor)
        var.ui.btnModifven.clicked.connect(vendedores.Vendedores.modifVendedor)
        var.ui.btnBuscarven.clicked.connect(vendedores.Vendedores.filtroBusquedaVendedor)

        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaClientes)
        var.ui.btnAltaCli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0, 0))
        var.ui.btnBajaCli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0, 1))
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifCliente)
        var.ui.btnDelcli.clicked.connect(clientes.Clientes.bajaCliente)
        var.ui.btnBuscarcli.clicked.connect(clientes.Clientes.filtroBusquedaCliente)
        var.ui.btnSiguientecli.clicked.connect(clientes.Clientes.siguientePaginaClientes)
        var.ui.btnAnteriorcli.clicked.connect(clientes.Clientes.anteriorPaginaClientes)

        var.ui.btnGrabarprop.clicked.connect(propiedades.Propiedades.altaPropiedad)
        var.ui.btnFechaprop.clicked.connect(lambda: eventos.Eventos.abrirCalendar(1, 0))
        var.ui.btnBajaprop.clicked.connect(lambda: eventos.Eventos.abrirCalendar(1, 1))
        var.ui.btnDelprop.clicked.connect(propiedades.Propiedades.bajaPropiedad)
        var.ui.btnModifprop.clicked.connect(propiedades.Propiedades.modifProp)
        var.ui.btnBuscartipoprop.clicked.connect(propiedades.Propiedades.filtroBusqueda)
        var.ui.btnSiguienteprop.clicked.connect(propiedades.Propiedades.siguientePaginaProp)
        var.ui.btnAnteriorprop.clicked.connect(propiedades.Propiedades.anteriorPaginaProp)
        '''
        eventos de cajas de texto
        '''
        var.ui.txtDniven.editingFinished.connect(lambda: vendedores.Vendedores.checkDNIven(var.ui.txtDniven.text()))
        var.ui.txtEmailven.editingFinished.connect(lambda: vendedores.Vendedores.checkEmail(var.ui.txtEmailven.text()))
        var.ui.txtMovilven.editingFinished.connect(lambda: vendedores.Vendedores.checkNumero(var.ui.txtMovilven.text()))

        var.ui.txtDnicli.editingFinished.connect(lambda: clientes.Clientes.checkDNI(var.ui.txtDnicli.text()))
        var.ui.txtEmailcli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailcli.text()))
        var.ui.txtMovilcli.editingFinished.connect(lambda: clientes.Clientes.checkNumero(var.ui.txtMovilcli.text()))
        var.ui.txtMovilprop.editingFinished.connect(lambda: propiedades.Propiedades.checkNumeroProp(var.ui.txtMovilprop.text()))
        '''
        combobox events
        '''
        eventos.Eventos.cargarProv()
        eventos.Eventos.cargarMuni()
        vendedores.Vendedores.cargarDelegacionven()
        var.ui.cmbProvcli.currentIndexChanged.connect(eventos.Eventos.cargarMuni)
        eventos.Eventos.cargarProvprop()
        eventos.Eventos.cargarMuniprop()
        var.ui.cmbProvprop.currentIndexChanged.connect(eventos.Eventos.cargarMuniprop)
        eventos.Eventos.cargarTipoprop(self)

        '''
        eventos del ToolBar
        '''
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionbarLimpiar.triggered.connect(eventos.Eventos.limpiarPanel)
        var.ui.actionbarBuscar.triggered.connect(eventos.Eventos.buscarPorFiltro)

        '''
        eventos checkBox
        '''
        var.ui.chkHistoricoven.stateChanged.connect(vendedores.Vendedores.historicoVen)

        var.ui.chkHistoriacli.stateChanged.connect(clientes.Clientes.historicoCli)
        var.ui.chkHistoricoprop.stateChanged.connect(propiedades.Propiedades.filtroBusquedaHistorico)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())