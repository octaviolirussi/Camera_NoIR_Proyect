import cv2
from PySide6.QtCore import QTimer #para actualizar la imagen de la cámara en tiempo real
from PySide6.QtGui import QImage, QPixmap
import datetime  
import os

class Camara:
    def __init__(self, label, carpeta_fotos="fotos"):
        self.label = label # es donde se mostrará la cámara
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer() # Temporizador que llamará actualizar_frame cada cierto intervalo
        self.timer.timeout.connect(self.actualizar_frame)
        self.fotos_guardadas = []

        # Crear carpeta para guardar fotos
        self.carpeta_fotos = carpeta_fotos
        os.makedirs(self.carpeta_fotos, exist_ok=True)

        if not self.cap.isOpened():
            raise Exception("No se pudo acceder a la cámara")

    #permite mostrar en tiempo real la vista previa
    def iniciar(self):
        self.timer.start(30)

    def detener(self):
        self.timer.stop()
        if self.cap.isOpened():
            self.cap.release()
        self.label.clear()

    def actualizar_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print("No se pudo leer frame de la cámara")
            return
        
        # Voltear horizontalmente para que no sea espejo
        frame = cv2.flip(frame, 1) 

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convierte de BGR a RGB 
        h, w, ch = frame_rgb.shape #h=alto, w=ancho, ch=canales de color (3)
        bytes_per_line = ch * w # se utiliza para saber cuantos bytes hay en cada linea de la imagen, pixeles por linea
        qimg = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888) # transformamos el array para que pyside lo pueda mostrar
        self.label.setPixmap(QPixmap.fromImage(qimg)) #mustra la imagen

        # Guardamos el último frame en memoria, esto para capturarlo despues ya que sera la foto
        self.ultimo_frame = frame

    def capturar_foto(self):
        if hasattr(self, "ultimo_frame"):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") #Genera un nombre de archivo único con la fecha y hora
            nombre_archivo = os.path.join(self.carpeta_fotos, f"foto_{timestamp}.png") 
            cv2.imwrite(nombre_archivo, self.ultimo_frame) #Guarda la foto en la carpeta
            self.fotos_guardadas.append(nombre_archivo)  # agregamos a la lista de fotos_guardadas
            return nombre_archivo #Devuelve el nombre del archivo para usarlo en la interfaz
        else:
            print("No hay frame disponible para capturar")
            return None
