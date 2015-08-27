import cv2
import numpy as np
import random 
import ruido

image = cv2.imread('test.jpg')#accedemos a al ruta donde se encuentra la imagen
image2 = cv2.imread('test.jpg')
#cv2.imshow("Original",image)#Cargamos un frame con la primer imagen a mostrar 
(h,w) =image2.shape[:2]
ruidos = ruido.sal(image2,0.40,w,h) ; 

matriz = np.hstack([image,ruidos]) 
cv2.imshow("Ruido",matriz)
cv2.waitKey(0)