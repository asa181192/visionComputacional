import random 


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
