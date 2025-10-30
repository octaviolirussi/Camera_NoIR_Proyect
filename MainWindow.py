# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt, QSize, QMetaObject
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QStatusBar, QTabWidget, QWidget,
    QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QListView, QListWidgetItem
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
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

        self.labelCamara = QLabel(self.tab)
        self.labelCamara.setObjectName("labelCamara")
        self.labelCamara.setScaledContents(True)
        self.labelCamara.setMinimumSize(640, 480)

        self.pushButton = QPushButton("Take Picture", self.tab)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFixedSize(160, 50)

        # Layout dinámico del tab de cámara
        layoutCamara = QVBoxLayout(self.tab)
        layoutCamara.addWidget(self.labelCamara, stretch=1)  
        botonesLayout = QHBoxLayout()
        botonesLayout.addStretch()
        botonesLayout.addWidget(self.pushButton, alignment=Qt.AlignRight)
        layoutCamara.addLayout(botonesLayout)

        self.tab.setLayout(layoutCamara)
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
        self.botonEliminar.setFixedSize(160, 50)

        # Layout dinámico del tab de fotos
        layoutFotos = QVBoxLayout(self.tab_2)
        layoutFotos.addWidget(self.listaFotos, stretch=1)

        botonesLayout2 = QHBoxLayout()
        botonesLayout2.addStretch()
        botonesLayout2.addWidget(self.botonEliminar, alignment=Qt.AlignRight)
        layoutFotos.addLayout(botonesLayout2)

        self.tab_2.setLayout(layoutFotos)
        self.tabWidget.addTab(self.tab_2, "Folder")

        # ---- Status Bar ----
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setCentralWidget(self.centralwidget)

        # ---- Conectar señales y traducciones ----
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
