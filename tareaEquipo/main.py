import cv2
import numpy as np
import random 
import ruido

image = cv2.imread('test.jpg')#accedemos a al ruta donde se encuentra la imagen
image2 = cv2.imread('test.jpg')
(h,w) =image2.shape[:2] # se obtiene la altura y la anchura de la matriz por el metodo shape 
ruidos = ruido.sal(image2,0.30,w,h) ;  # se envia al metodo sal la imagen con la probabilidad y sus dimensiones . 

matriz = np.hstack([image,ruidos]) # se unen las dos imagenes la original y modificada en un solo vector para mostrarse
                                   #en una sola ventana 
cv2.imshow("Ruido",matriz)
cv2.waitKey(0)


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
