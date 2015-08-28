import cv2
import numpy as np
import random 
import ruido

image = cv2.imread('test.jpg')#accedemos a al ruta donde se encuentra la imagen
image2 = cv2.imread('test.jpg')
(h,w) =image2.shape[:2] # se obtiene la altura y la anchura de la matriz por el metodo shape 
ruidos = ruido.sal(image2,0.40,w,h) ;  # se envia al metodo sal la imagen con la probabilidad y sus dimensiones . 

matriz = np.hstack([image,ruidos]) # se unen las dos imagenes la original y modificada en un solo vector para mostrarse
                                   #en una sola ventana 
cv2.imshow("Ruido",matriz)
cv2.waitKey(0)
