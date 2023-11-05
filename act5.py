import cv2
import numpy as np

# Carga la imagen
img = cv2.imread('pinguino.jpg')

# Aumenta o disminuye el brillo y el contraste (ajusta los valores según sea necesario)
alpha = 1  # Factor de contraste
beta = 20    # Factor de brillo

# Aplica la transformación lineal para cambiar el brillo y el contraste
imagen_ajustada = cv2.convertScaleAbs(img, alpha=2, beta=20)

# Muestra la imagen original y la imagen ajustada en ventanas separadas
cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen Ajustada', imagen_ajustada)

# Espera a que se presione una tecla y luego cierra las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
