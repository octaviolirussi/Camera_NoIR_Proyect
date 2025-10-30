# -*- coding: utf-8 -*-
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QIcon, QPixmap)
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QStatusBar, QTabWidget, QWidget,
    QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QListView, QListWidgetItem
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 617)

        # ---- Central Widget ----
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ---- Tabs ----
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 601))

        # ================= TAB 1: CÁMARA =================
        self.tab = QWidget()
        self.tab.setObjectName("tab")

        self.labelCamara = QLabel(self.tab)
        self.labelCamara.setObjectName("labelCamara")
        self.labelCamara.setScaledContents(True)
        self.labelCamara.setMinimumSize(640, 480)
        self.labelCamara.setMaximumSize(800, 600)

        # --- Botón para tomar foto ---
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFixedSize(160, 50)  

        # Layout de cámara 
        layoutCamara = QVBoxLayout(self.tab)
        layoutCamara.addWidget(self.labelCamara, alignment=Qt.AlignCenter)

        botonesLayout = QHBoxLayout()
        botonesLayout.addStretch()  
        botonesLayout.addWidget(self.pushButton, alignment=Qt.AlignRight)
        layoutCamara.addLayout(botonesLayout)
        self.tab.setLayout(layoutCamara)

        self.tabWidget.addTab(self.tab, "")

        # ================= TAB 2: FOTOS =================
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")

        self.listaFotos = QListWidget(self.tab_2)
        self.listaFotos.setObjectName("listaFotos")
        self.listaFotos.setViewMode(QListView.IconMode)
        self.listaFotos.setIconSize(QSize(120, 90))
        self.listaFotos.setResizeMode(QListView.Adjust)
        self.listaFotos.setSpacing(10)

        self.botonEliminar = QPushButton(self.tab_2)
        self.botonEliminar.setObjectName("DeletePicture")
        self.botonEliminar.setFixedSize(160, 50) 

        # Layout de lista + botón eliminar 
        layout_tab2 = QVBoxLayout(self.tab_2)
        layout_tab2.addWidget(self.listaFotos)

        botonesLayout2 = QHBoxLayout()
        botonesLayout2.addStretch()
        botonesLayout2.addWidget(self.botonEliminar, alignment=Qt.AlignRight)
        layout_tab2.addLayout(botonesLayout2)
        self.tab_2.setLayout(layout_tab2)

        self.tabWidget.addTab(self.tab_2, "")

        # ---- Status Bar ----
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setCentralWidget(self.centralwidget)

        # ---- Traducción y conexiones ----
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Camera", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "Take Picture", None))
        self.botonEliminar.setText(QCoreApplication.translate("MainWindow", "Delete Picture", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", "Camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", "Folder", None))

    def agregar_foto_a_lista(self, listaWidget, ruta_archivo, ancho=120, alto=90):
        """Agrega una miniatura con nombre debajo al QListWidget"""
        pixmap = QPixmap(ruta_archivo)
        icono = QIcon(pixmap.scaled(ancho, alto, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        nombre = ruta_archivo.split("/")[-1]
        item = QListWidgetItem(nombre)
        item.setIcon(icono)
        item.setData(Qt.UserRole, ruta_archivo)
        listaWidget.addItem(item)
