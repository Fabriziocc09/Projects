# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 1 - Introducción a las imágenes digitales
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow
import cv2
import numpy as np

# -------------------------------------------------------------------------
# Escribe tu código aquí:

img = cv2.imread("./img/14.jpg")
imshow("imagen" , img)

azul = img[:,:,0]
imshow("azul" , azul)

negro = np.zeros(img.shape , np.uint8)
imshow("negro" , negro)

blanco = 255 * np.ones(img.shape , np.uint8)
imshow("blanco" , blanco)


# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
