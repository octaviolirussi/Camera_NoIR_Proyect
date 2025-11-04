import sys
import os
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from MainWindow import Ui_MainWindow
from camara import Camara 

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):# crea la ventana y construye los widgets de MainWindow
        super().__init__() 
        self.setupUi(self)

        # Inicializamos la cámara
        self.camara = Camara(self.labelCamara)
        self.camara.iniciar() 

        # evento para tomar fotos y abrir fotos
        self.pushButton.clicked.connect(self.sacar_foto)
        self.listaFotos.itemDoubleClicked.connect(self.abrir_foto)# el item que fue clickeado se pasa automaticamente

        # Cargar fotos existentes de la carpeta al iniciar
        self.cargar_fotos_existentes()

        self.botonEliminar.clicked.connect(self.eliminar_foto)

        self.botonSalir.clicked.connect(QtWidgets.QApplication.quit)

    #=========================================================== Metodos ===================================================================

    def sacar_foto(self):#Llama a capturar_foto de Camara y recibe la imagen
        archivo = self.camara.capturar_foto()
        if archivo:
            self.agregar_foto_a_lista(self.listaFotos, archivo)  # pasamos la lista
            QtWidgets.QMessageBox.information(self, "Foto guardada", f"Se guardó la foto en:\n{archivo}")

    def cargar_fotos_existentes(self): #carga las fotos ya existentes desde la carpeta fotos
        carpeta = self.camara.carpeta_fotos
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        archivos = [f for f in os.listdir(carpeta) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        for f in archivos:
            ruta_completa = os.path.join(carpeta, f)
            self.agregar_foto_a_lista(self.listaFotos, ruta_completa)
            self.camara.fotos_guardadas.append(ruta_completa)
    
    def abrir_foto(self, item):#abre la imagen dependiendo el SO
        import subprocess, platform
        ruta = item.data(Qt.UserRole) #obtiene la ruta de la imagen para abrirla
        if platform.system() == "Windows":
            subprocess.run(["explorer", ruta])
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", ruta])
        else:  # Linux
            subprocess.run(["xdg-open", ruta])

    def cerrar_aplicacion(self):
        self.camara.detener()         
        QtWidgets.QApplication.quit() 
    
    def eliminar_foto(self):
        item = self.listaFotos.currentItem()  # obtiene el item seleccionado
        if not item:
            QtWidgets.QMessageBox.warning(self, "Eliminar foto", "Por favor, selecciona una foto para eliminar.")
            return

        ruta = item.data(Qt.UserRole)

        # Confirmar antes de eliminar
        respuesta = QtWidgets.QMessageBox.question(
            self, "Confirmar eliminación",
            f"¿Deseas eliminar esta foto?\n{ruta}",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if respuesta == QtWidgets.QMessageBox.Yes:
            try:
                if os.path.exists(ruta):
                    os.remove(ruta)
                self.listaFotos.takeItem(self.listaFotos.row(item))  # eliminar de la lista
                if ruta in self.camara.fotos_guardadas:
                    self.camara.fotos_guardadas.remove(ruta)
                QtWidgets.QMessageBox.information(self, "Foto eliminada", "La foto fue eliminada correctamente.")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo eliminar la foto:\n{e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    window.show()
    sys.exit(app.exec())
