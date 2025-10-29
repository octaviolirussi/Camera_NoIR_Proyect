# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#QtCore → funcionalidades básicas de Qt (objetos, geometría, alineación, señales, etc.).
#QtGui → manejo de imágenes, colores, pixmaps, fuentes, paletas y pintura de widgets.
#QtWidgets → todos los widgets de la interfaz: ventanas, botones, labels, layouts, listas, tabs, etc.

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget, QLabel, QVBoxLayout, QListWidget, QListView, QListWidgetItem)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow): #Recibe como parámetro la ventana principal (MainWindow) y agrega los widgets adentro
        if not MainWindow.objectName(): #configuracion de la ventana princial
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 617)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.tabWidget = QTabWidget(self.centralwidget) #crea el contenedor de tabs
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 601))

        self.tab = QWidget() # primer tab que tiene la camara
        self.tab.setObjectName(u"tab")
        self.labelCamara = QLabel(self.tab)
        self.labelCamara.setObjectName("labelCamara")
        self.labelCamara.setScaledContents(True) 

        layout = QVBoxLayout(self.tab) #centra la camara dentro del tab, agrega la camara al tab
        layout.addWidget(self.labelCamara)
        layout.setAlignment(self.labelCamara, Qt.AlignCenter)
        self.tab.setLayout(layout)

        self.labelCamara.setMinimumSize(640, 480)#tamanio minimo y maximo de la camara
        self.labelCamara.setMaximumSize(800, 600)

        self.pushButton = QPushButton(self.tab)#crea el boton y lo pone dentro del tab
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(650, 530, 141, 41)) #x, y, w, h
        
        self.tabWidget.addTab(self.tab, "")#agrega el tab al widget principal

        self.tab_2 = QWidget()#crea el otro tab
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.listaFotos = QListWidget(self.tab_2) # crea el listado de fotos y lo agreaga al tab 2
        self.listaFotos.setObjectName("listaFotos")
        self.listaFotos.setViewMode(QListView.IconMode) # para que se vea una lista de iconos
        self.listaFotos.setIconSize(QSize(120, 90))  # tamaño de miniatura
        self.listaFotos.setResizeMode(QListView.Adjust)
        self.listaFotos.setSpacing(10)  # espacio entre ítems

        self.botonEliminar = QPushButton(self.tab_2) #boton para eliminar fotos
        self.botonEliminar.setObjectName(u"DeletePicture")
        self.botonEliminar.setGeometry(QRect(620, 520, 141, 41))

       
        layout_tab2 = QVBoxLayout(self.tab_2)
        layout_tab2.addWidget(self.listaFotos)
        self.tab_2.setLayout(layout_tab2)
        
        self.statusbar = QStatusBar(MainWindow) #crea la barra inferior de la ventana
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)


        #Metodos que permiten mostrar la ventana, traducir la interfaz y permite conectar los eventos que ocurran
        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"TakePicture", None))
        self.botonEliminar.setText(QCoreApplication.translate("MainWindow", u"DeletePicture", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Folder", None))
    # retranslateUi

    def agregar_foto_a_lista(self, listaWidget, ruta_archivo, ancho=120, alto=90):#agrega iconos de las fotos
        """Agrega una miniatura con nombre debajo al QListWidget"""
        pixmap = QPixmap(ruta_archivo)
        icono = QIcon(pixmap.scaled(ancho, alto, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        nombre = ruta_archivo.split("/")[-1]
        item = QListWidgetItem(nombre)
        item.setIcon(icono)
        item.setData(Qt.UserRole, ruta_archivo)  # Guardamos ruta para abrir luego
        listaWidget.addItem(item)