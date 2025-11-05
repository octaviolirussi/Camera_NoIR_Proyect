# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt, QSize, QMetaObject
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QStatusBar, QStackedLayout, QSizePolicy, 
    QTabWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListView, QListWidgetItem, QGridLayout
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)

        # ---- Central Widget ----
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ---- Tabs ----
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        # ================= TAB 1: CÁMARA =================
        self.tab = QWidget()
        self.tab.setObjectName("tab")

        # --- contenedor principal ---
        contenedor = QWidget(self.tab)
        contenedor.setObjectName("contenedorCamara")

        # --- layout en rejilla (superposición total) ---
        layout = QGridLayout(contenedor)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # --- vista previa de cámara ---
        self.labelCamara = QLabel()
        self.labelCamara.setScaledContents(True)
        self.labelCamara.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.labelCamara, 0, 0)  # fondo

        # --- botón sacar foto ---
        self.pushButton = QPushButton("Take Picture")
        self.pushButton.setFixedSize(160, 50)
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 150);
                color: white;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(50, 50, 50, 180);
            }
        """)
        # Alineación: esquina inferior derecha
        layout.addWidget(self.pushButton, 0, 0, Qt.AlignBottom | Qt.AlignRight)

        #================= Boton Salir ==================
        self.botonSalir = QPushButton("✕", self)
        self.botonSalir.setFixedSize(40, 40)
        self.botonSalir.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 0, 0, 180);
                color: white;
                font-size: 20px;
                border: none;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: rgba(255, 50, 50, 200);
            }
        """)

        # Alineación: esquina superior derecha
        layout.addWidget(self.botonSalir, 0, 0, Qt.AlignTop | Qt.AlignRight)

        # --- layout final del tab ---
        layoutTab = QVBoxLayout(self.tab)
        layoutTab.setContentsMargins(0, 0, 0, 0)
        layoutTab.addWidget(contenedor)
        self.tab.setLayout(layoutTab)

        self.tabWidget.addTab(self.tab, "Camera")

        # ================= TAB 2: FOTOS =================
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")

        self.listaFotos = QListWidget(self.tab_2)
        self.listaFotos.setObjectName("listaFotos")
        self.listaFotos.setViewMode(QListView.IconMode)
        self.listaFotos.setIconSize(QSize(120, 90))
        self.listaFotos.setResizeMode(QListView.Adjust)
        self.listaFotos.setSpacing(10)

        self.botonEliminar = QPushButton("Delete Picture", self.tab_2)
        self.botonEliminar.setObjectName("DeletePicture")
        self.botonEliminar.setMinimumSize(160, 50)
        self.botonEliminar.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 150);
                color: white;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(50, 50, 50, 180);
            }
        """)

        # Layout dinámico del tab de fotos
        layoutFotos = QVBoxLayout(self.tab_2)
        layoutFotos.addWidget(self.listaFotos, stretch=1)
        botonesLayout2 = QHBoxLayout()
        botonesLayout2.addStretch()
        botonesLayout2.addWidget(self.botonEliminar, alignment=Qt.AlignRight)
        layoutFotos.addLayout(botonesLayout2)
        self.tab_2.setLayout(layoutFotos)

        self.tabWidget.addTab(self.tab_2, "Folder")

        # ---- Layout principal del central widget ----
        mainLayout = QVBoxLayout(self.centralwidget)
        mainLayout.addWidget(self.tabWidget)
        self.centralwidget.setLayout(mainLayout)

        # ---- Status Bar ----
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setCentralWidget(self.centralwidget)


        # ---- Traducciones y conexiones ----
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Camera")
        self.pushButton.setText("Take Picture")
        self.botonEliminar.setText("Delete Picture")

    def agregar_foto_a_lista(self, listaWidget, ruta_archivo, ancho=120, alto=90):
        """Agrega una miniatura con nombre debajo al QListWidget"""
        pixmap = QPixmap(ruta_archivo)
        icono = QIcon(pixmap.scaled(ancho, alto, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        nombre = ruta_archivo.split("/")[-1]
        item = QListWidgetItem(nombre)
        item.setIcon(icono)
        item.setData(Qt.UserRole, ruta_archivo)
        listaWidget.addItem(item)
