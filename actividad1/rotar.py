import cv2
import numpy as np
import argparse
#Todos los codigos hacen uos de la libreria opencv 
#Alfredo SAntiago Alvarado

image = cv2.imread('test.jpg')#accedemos a al ruta donde se encuentra la imagen
image2 = cv2.imread('test.jpg')

(h,w) =image2.shape[:2] #Obtiene el el ancho y la altura de la imagen y las guarda en h , w 
center = (w/2,h/2) #se obtiene el centro de la imagen dividiendo en tre dos la altura y la anchura
print center
M = cv2.getRotationMatrix2D(center,180,1.0) # se genera una matriz de rotacion pasando por parametros el centro , los grados y la escala de la iamgen 
rotated= cv2.warpAffine(image2,M,(w,h))

matriz = np.hstack([image,rotated]) 
cv2.imshow("Rotated",matriz)

cv2.waitKey(0)


