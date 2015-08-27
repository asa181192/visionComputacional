import cv2
import numpy as np
import argparse
#Todos los codigos hacen uos de la libreria opencv 
#Alfredo SAntiago Alvarado

image = cv2.imread('test.jpg')#accedemos a al ruta donde se encuentra la imagen
image2 = cv2.imread('test.jpg')


M=np.ones(image2.shape, dtype = "uint8")
M=M*80 #esa matriz se pultiplica por 1 todos sus valores 
substraccion = cv2.subtract(image2,M) #Se realiza una resta de la matriz actual con la matriz creada
matriz = np.hstack([image,substraccion]) 
cv2.imshow("Oscurecer",matriz)# se muestra la imagen oscura 

cv2.waitKey(0)