import random 


def sal(pixeles, intensidad,altura,anchura):

	
	for i in range(0,altura) :
		for j in range (0,anchura) :
			sal = random.uniform(0.1,1.0) 
			pimienta = random.randint(0,1) 

			if sal <=  intensidad : 
				
				if pimienta == 1 :
					pixeles[i,j] = (0,0,0)	
				else:  
				 	pixeles[i,j] = (255,255,255)
							

	return pixeles