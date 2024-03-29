# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 3 - Mejorando las imágenes
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow, noise
import cv2
import numpy as np
from matplotlib import pyplot as plt

# -------------------------------------------------------------------------
# Escribe tu código aquí:

img = cv2.imread("./img/7.jpg")
imshow("Foto", img)

ruido = noise(img)
imshow("ruido" , ruido)

kernel = np.ones((15,15),np.float32)/(15*15)
desenfoque = cv2.filter2D(img,-1,kernel)
imshow("desenfoque",desenfoque)


kernel = -1*np.ones((5,5),np.float32)
kernel[2,2] = 25
enfoque = cv2.filter2D(desenfoque,-1,kernel)
imshow("enfoque", enfoque)


contraste = 5.0
brillo = -2
nueva = cv2.convertScaleAbs(img, alpha=contraste, beta=brillo)
imshow("nueva" , nueva)


# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
