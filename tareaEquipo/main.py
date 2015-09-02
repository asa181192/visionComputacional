import cv2
import numpy as np
import random 
import argparse 
import sys

np.set_printoptions(threshold=sys.maxint) #Resuelve el error de los puntos suspensivos en la impresion de la imagen

def sal(pixeles, intensidad,altura,anchura): # se obtiene por parametros la imagen , la intesidad que es una probabilidad 
					     # en float de 0.1 a -1 , la altura y la anchura de la imagen para recorrer 
					     # su matriz . 

	
	for i in range(0,altura) : #se recorre todos los pixeles de la imagen 
		for j in range (0,anchura) :
			sal = random.uniform(0.1,1.0) #se genera una probabilidad de que aparesca en el pixel ruido de 0.1 - 1 
			pimienta = random.randint(0,1) # se genera otra probabilidad de que aparesca een el pixel un negro o blanco 

			if sal <=  intensidad : 
				
				if pimienta == 1 :
					pixeles[i,j] = (0,0,0)	
				else:  
				 	pixeles[i,j] = (255,255,255)
							

	return pixeles # regresamos la matriz de la iamgen 
	
	
ap =argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True ,help="Path to the image")
args =  vars(ap.parse_args())

image = cv2.imread(args["image"])#accedemos a al ruta donde se encuentra la imagen
image2 = cv2.imread(args["image"])
(h,w) =image2.shape[:2] # se obtiene la altura y la anchura de la matriz por el metodo shape 
ruidos = sal(image2,0.30,w,h) ;  # se envia al metodo sal la imagen con la probabilidad y sus dimensiones . 

matriz = np.hstack([image,ruidos]) # se unen las dos imagenes la original y modificada en un solo vector para mostrarse
                                   #en una sola ventana
sys.stdout = open('matriz.txt', 'w')
print ruidos				#imprime la imagen a un documento de texto 			 
cv2.imshow("Ruido",matriz)
cv2.imwrite(args["image"]+"mod.jpg",ruidos); #Guarda la imagen que fue modificada 
cv2.waitKey(0)


