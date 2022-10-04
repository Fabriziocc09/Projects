# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 4 - Crea tu propio filtro
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow
import cv2
import numpy as np

# -------------------------------------------------------------------------
# Escribe tu código aquí:


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Hola")
        break
    cv2.imshow("frame",frame)
    grises = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bordes = cv2.adaptativeTreshold(grises , 255 , cv2.ADAPTATIVE_TRESH_MEAN_C ,cv2.TRESH_BINARY ,11 ,2)

    kernel = np.ones((3,3), np.uint8)
    dilatacion =cv2.dilate(bordes,kernel)
    cv2.imshow("dilatación" , dilatacion)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
