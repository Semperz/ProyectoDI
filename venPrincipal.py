# Form implementation generated from reading ui file '.\templates\venPrincipal.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(1058, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(venPrincipal.sizePolicy().hasHeightForWidth())
        venPrincipal.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/a23sergiopg/.designer/backup/img/icono.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        venPrincipal.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.panPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.panPrincipal.setObjectName("panPrincipal")
        self.pesClientes = QtWidgets.QWidget()
        self.pesClientes.setObjectName("pesClientes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pesClientes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line = QtWidgets.QFrame(parent=self.pesClientes)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 4, 0, 1, 1)
        self.tabClientes = QtWidgets.QTableWidget(parent=self.pesClientes)
        self.tabClientes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabClientes.setObjectName("tabClientes")
        self.tabClientes.setColumnCount(7)
        self.tabClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(6, item)
        self.tabClientes.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tabClientes, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.chkHistoriacli = QtWidgets.QCheckBox(parent=self.pesClientes)
        self.chkHistoriacli.setObjectName("chkHistoriacli")
        self.gridLayout.addWidget(self.chkHistoriacli, 1, 12, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 6, 1, 1)
        self.txtDnicli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDnicli.setMinimumSize(QtCore.QSize(120, 0))
        self.txtDnicli.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txtDnicli.setStyleSheet("background-color:rgb(229, 255, 255);")
        self.txtDnicli.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDnicli.setObjectName("txtDnicli")
        self.gridLayout.addWidget(self.txtDnicli, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 3, 1, 1)
        self.lblDnicli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblDnicli.setObjectName("lblDnicli")
        self.gridLayout.addWidget(self.lblDnicli, 0, 1, 1, 1)
        self.txtEmailcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtEmailcli.setMinimumSize(QtCore.QSize(200, 0))
        self.txtEmailcli.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtEmailcli.setStyleSheet("background-color:rgb(229, 255, 255);")
        self.txtEmailcli.setObjectName("txtEmailcli")
        self.gridLayout.addWidget(self.txtEmailcli, 2, 2, 1, 1)
        self.txtNomcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtNomcli.setMinimumSize(QtCore.QSize(200, 0))
        self.txtNomcli.setMaximumSize(QtCore.QSize(250, 16777215))
        self.txtNomcli.setStyleSheet("background-color:rgb(229, 255, 255);")
        self.txtNomcli.setObjectName("txtNomcli")
        self.gridLayout.addWidget(self.txtNomcli, 1, 5, 1, 7)
        self.lblEmailcli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblEmailcli.setObjectName("lblEmailcli")
        self.gridLayout.addWidget(self.lblEmailcli, 2, 1, 1, 1)
        self.txtMovilcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtMovilcli.setMinimumSize(QtCore.QSize(120, 0))
        self.txtMovilcli.setMaximumSize(QtCore.QSize(80, 16777215))
        self.txtMovilcli.setStyleSheet("background-color:rgb(229, 255, 255);")
        self.txtMovilcli.setText("")
        self.txtMovilcli.setObjectName("txtMovilcli")
        self.gridLayout.addWidget(self.txtMovilcli, 2, 5, 1, 4)
        self.lblProvcli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblProvcli.setObjectName("lblProvcli")
        self.gridLayout.addWidget(self.lblProvcli, 3, 7, 1, 1)
        self.txtApelcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtApelcli.setMinimumSize(QtCore.QSize(250, 0))
        self.txtApelcli.setMaximumSize(QtCore.QSize(350, 16777215))
        self.txtApelcli.setStyleSheet("background-color:rgb(229, 255, 255);")
        self.txtApelcli.setObjectName("txtApelcli")
        self.gridLayout.addWidget(self.txtApelcli, 1, 2, 1, 1)
        self.lblApelcli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblApelcli.setObjectName("lblApelcli")
        self.gridLayout.addWidget(self.lblApelcli, 1, 1, 1, 1)
        self.lblMovilcli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblMovilcli.setObjectName("lblMovilcli")
        self.gridLayout.addWidget(self.lblMovilcli, 2, 4, 1, 1)
        self.lblNomcli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblNomcli.setObjectName("lblNomcli")
        self.gridLayout.addWidget(self.lblNomcli, 1, 4, 1, 1)
        self.cmbProvcli = QtWidgets.QComboBox(parent=self.pesClientes)
        self.cmbProvcli.setMinimumSize(QtCore.QSize(150, 0))
        self.cmbProvcli.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cmbProvcli.setStyleSheet("background-color:rgb(229, 255, 255);")
        self.cmbProvcli.setObjectName("cmbProvcli")
        self.gridLayout.addWidget(self.cmbProvcli, 3, 8, 1, 1)
        self.txtDircli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDircli.setMinimumSize(QtCore.QSize(300, 0))
        self.txtDircli.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.txtDircli.setStyleSheet("background-color:rgb(229, 255, 255);")
        self.txtDircli.setObjectName("txtDircli")
        self.gridLayout.addWidget(self.txtDircli, 3, 2, 1, 4)
        self.lblDircli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblDircli.setObjectName("lblDircli")
        self.gridLayout.addWidget(self.lblDircli, 3, 1, 1, 1)
        self.lblMunicli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblMunicli.setObjectName("lblMunicli")
        self.gridLayout.addWidget(self.lblMunicli, 3, 11, 1, 1)
        self.cmbMunicli = QtWidgets.QComboBox(parent=self.pesClientes)
        self.cmbMunicli.setMinimumSize(QtCore.QSize(200, 0))
        self.cmbMunicli.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cmbMunicli.setStyleSheet("background-color:rgb(229, 255, 255);")
        self.cmbMunicli.setObjectName("cmbMunicli")
        self.gridLayout.addWidget(self.cmbMunicli, 3, 12, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 4, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 13, 4, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 10, 1, 1)
        self.lblFechaAltacli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblFechaAltacli.setObjectName("lblFechaAltacli")
        self.gridLayout.addWidget(self.lblFechaAltacli, 0, 6, 1, 1)
        self.btnAltaCli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnAltaCli.setMinimumSize(QtCore.QSize(25, 25))
        self.btnAltaCli.setMaximumSize(QtCore.QSize(25, 25))
        self.btnAltaCli.setStyleSheet("")
        self.btnAltaCli.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\templates\\../img/calendario.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAltaCli.setIcon(icon1)
        self.btnAltaCli.setIconSize(QtCore.QSize(25, 25))
        self.btnAltaCli.setCheckable(False)
        self.btnAltaCli.setObjectName("btnAltaCli")
        self.gridLayout.addWidget(self.btnAltaCli, 0, 8, 1, 1)
        self.txtAltaCli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtAltaCli.setMinimumSize(QtCore.QSize(80, 0))
        self.txtAltaCli.setMaximumSize(QtCore.QSize(80, 16777215))
        self.txtAltaCli.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtAltaCli.setObjectName("txtAltaCli")
        self.gridLayout.addWidget(self.txtAltaCli, 0, 7, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 9, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.btnGrabarcli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnGrabarcli.setMinimumSize(QtCore.QSize(80, 25))
        self.btnGrabarcli.setMaximumSize(QtCore.QSize(80, 25))
        self.btnGrabarcli.setObjectName("btnGrabarcli")
        self.horizontalLayout.addWidget(self.btnGrabarcli)
        self.btnModifcli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnModifcli.setMinimumSize(QtCore.QSize(80, 25))
        self.btnModifcli.setMaximumSize(QtCore.QSize(80, 25))
        self.btnModifcli.setObjectName("btnModifcli")
        self.horizontalLayout.addWidget(self.btnModifcli)
        self.btnDelcli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnDelcli.setMinimumSize(QtCore.QSize(80, 25))
        self.btnDelcli.setMaximumSize(QtCore.QSize(80, 25))
        self.btnDelcli.setObjectName("btnDelcli")
        self.horizontalLayout.addWidget(self.btnDelcli)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.panPrincipal.addTab(self.pesClientes, "")
        self.tabConstruccion = QtWidgets.QWidget()
        self.tabConstruccion.setObjectName("tabConstruccion")
        self.label = QtWidgets.QLabel(parent=self.tabConstruccion)
        self.label.setGeometry(QtCore.QRect(400, 270, 131, 31))
        self.label.setObjectName("label")
        self.panPrincipal.addTab(self.tabConstruccion, "")
        self.gridLayout_2.addWidget(self.panPrincipal, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 0, 2, 1, 1)
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=venPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 21))
        self.menubar.setObjectName("menubar")
        self.menuSalir = QtWidgets.QMenu(parent=self.menubar)
        self.menuSalir.setObjectName("menuSalir")
        self.menuHerramientas = QtWidgets.QMenu(parent=self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        venPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(parent=venPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSalir_2 = QtGui.QAction(parent=venPrincipal)
        self.actionSalir_2.setObjectName("actionSalir_2")
        self.actSalir = QtGui.QAction(parent=venPrincipal)
        self.actSalir.setObjectName("actSalir")
        self.actionCrear_Backup = QtGui.QAction(parent=venPrincipal)
        self.actionCrear_Backup.setObjectName("actionCrear_Backup")
        self.actionRestaurar_Backup = QtGui.QAction(parent=venPrincipal)
        self.actionRestaurar_Backup.setObjectName("actionRestaurar_Backup")
        self.menuSalir.addAction(self.actSalir)
        self.menuHerramientas.addAction(self.actionCrear_Backup)
        self.menuHerramientas.addAction(self.actionRestaurar_Backup)
        self.menubar.addAction(self.menuSalir.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())

        self.retranslateUi(venPrincipal)
        self.panPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)
        venPrincipal.setTabOrder(self.txtDnicli, self.txtAltaCli)
        venPrincipal.setTabOrder(self.txtAltaCli, self.txtApelcli)
        venPrincipal.setTabOrder(self.txtApelcli, self.txtNomcli)
        venPrincipal.setTabOrder(self.txtNomcli, self.txtEmailcli)
        venPrincipal.setTabOrder(self.txtEmailcli, self.txtMovilcli)
        venPrincipal.setTabOrder(self.txtMovilcli, self.txtDircli)
        venPrincipal.setTabOrder(self.txtDircli, self.cmbProvcli)
        venPrincipal.setTabOrder(self.cmbProvcli, self.cmbMunicli)
        venPrincipal.setTabOrder(self.cmbMunicli, self.chkHistoriacli)
        venPrincipal.setTabOrder(self.chkHistoriacli, self.btnAltaCli)
        venPrincipal.setTabOrder(self.btnAltaCli, self.btnGrabarcli)
        venPrincipal.setTabOrder(self.btnGrabarcli, self.btnModifcli)
        venPrincipal.setTabOrder(self.btnModifcli, self.btnDelcli)
        venPrincipal.setTabOrder(self.btnDelcli, self.tabClientes)
        venPrincipal.setTabOrder(self.tabClientes, self.panPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "InmoTeis"))
        item = self.tabClientes.horizontalHeaderItem(0)
        item.setText(_translate("venPrincipal", "Apellidos"))
        item = self.tabClientes.horizontalHeaderItem(1)
        item.setText(_translate("venPrincipal", "Nombre"))
        item = self.tabClientes.horizontalHeaderItem(2)
        item.setText(_translate("venPrincipal", "Email"))
        item = self.tabClientes.horizontalHeaderItem(3)
        item.setText(_translate("venPrincipal", "Móvil"))
        item = self.tabClientes.horizontalHeaderItem(4)
        item.setText(_translate("venPrincipal", "Provincia"))
        item = self.tabClientes.horizontalHeaderItem(5)
        item.setText(_translate("venPrincipal", "Municipio"))
        item = self.tabClientes.horizontalHeaderItem(6)
        item.setText(_translate("venPrincipal", "Fecha de Baja"))
        self.chkHistoriacli.setText(_translate("venPrincipal", "Historico"))
        self.lblDnicli.setText(_translate("venPrincipal", "DNI/CIF:"))
        self.lblEmailcli.setText(_translate("venPrincipal", "Email:"))
        self.lblProvcli.setText(_translate("venPrincipal", "Provincia:"))
        self.lblApelcli.setText(_translate("venPrincipal", "Apellidos:"))
        self.lblMovilcli.setText(_translate("venPrincipal", "Móvil:"))
        self.lblNomcli.setText(_translate("venPrincipal", "Nombre:"))
        self.lblDircli.setText(_translate("venPrincipal", "Dirección:"))
        self.lblMunicli.setText(_translate("venPrincipal", "Municipio:"))
        self.lblFechaAltacli.setText(_translate("venPrincipal", "Fecha Alta:"))
        self.btnGrabarcli.setText(_translate("venPrincipal", "Grabar"))
        self.btnModifcli.setText(_translate("venPrincipal", "Modificar"))
        self.btnDelcli.setText(_translate("venPrincipal", "Eliminar"))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.pesClientes), _translate("venPrincipal", "Clientes"))
        self.label.setText(_translate("venPrincipal", "PANEL EN CONSTRUCCIÓN"))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.tabConstruccion), _translate("venPrincipal", "Tab 2"))
        self.menuSalir.setTitle(_translate("venPrincipal", "Archivo"))
        self.menuHerramientas.setTitle(_translate("venPrincipal", "Herramientas"))
        self.actionSalir.setText(_translate("venPrincipal", "Salir"))
        self.actionSalir_2.setText(_translate("venPrincipal", "Salir"))
        self.actSalir.setText(_translate("venPrincipal", "Salir"))
        self.actionCrear_Backup.setText(_translate("venPrincipal", "Crear Backup"))
        self.actionRestaurar_Backup.setText(_translate("venPrincipal", "Restaurar Backup"))
