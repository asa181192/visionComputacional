import cv2
import numpy as np
import argparse
#Todos los codigos hacen uos de la libreria opencv 
#Alfredo SAntiago Alvarado

image = cv2.imread('test.jpg')#accedemos a al ruta donde se encuentra la imagen
image2 = cv2.imread('test.jpg')

print image2
espejo = cv2.flip(image2,1) #accedemos a un metodo de open cv que genera la matriz de flipeo de imagen 
print "start"
print espejo
matriz = np.hstack([image,espejo]) 
cv2.imshow("Espejo",matriz)
cv2.waitKey(0)