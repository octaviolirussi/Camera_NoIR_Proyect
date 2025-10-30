#!/bin/bash

echo "=============================="
echo "   Instalación de dependencias"
echo "=============================="

# Actualiza los paquetes del sistema (no afecta al venv)
echo ">>> Actualizando lista de paquetes..."
sudo apt update -y

# Instala dependencias del sistema necesarias para compilar y usar OpenCV y PySide6
echo ">>> Instalando librerías del sistema..."
sudo apt install -y \
  build-essential cmake pkg-config \
  libjpeg-dev libtiff5-dev libpng-dev \
  libavcodec-dev libavformat-dev libswscale-dev \
  libv4l-dev libxvidcore-dev libx264-dev \
  libfontconfig1-dev libcairo2-dev \
  libgdk-pixbuf2.0-dev libpango1.0-dev \
  libgtk2.0-dev libgtk-3-dev \
  libatlas-base-dev gfortran \
  libhdf5-dev libhdf5-serial-dev libhdf5-103 \
  libqt5gui5 libqt5webkit5 libqt5test5 \
  python3-pyqt5 python3-dev

if [ $? -ne 0 ]; then
  echo "❌ Error al instalar dependencias del sistema."
  exit 1
fi

# Instala dependencias Python dentro del entorno virtual
echo ">>> Instalando paquetes de Python en el entorno virtual..."
pip install --upgrade pip setuptools wheel
pip install "picamera[array]" opencv-python PySide6

if [ $? -ne 0 ]; then
  echo "❌ Error al instalar paquetes Python."
  exit 1
fi

echo "=============================="
echo "✅ Instalación completada dentro del entorno virtual"
echo "=============================="