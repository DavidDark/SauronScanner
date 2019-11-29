import cv2
import numpy as np
#Para los soniditos
#from pydub import AudioSegment
#from pydub.playback import play
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def comparar(ttl):
	ttl= ttl -1
	
	imagen1 = cv2.imread("Correcto.jpg")
	imagen2 = cv2.imread("Muestras/temp_{}.jpg".format(ttl))

	difference = cv2.subtract(imagen1, imagen2)

	result = not np.any(difference) #if difference is all zeros it will return False
		
	if result is True:
			print ("Las imagen {} es idéntica.".format(ttl))

	else:
			
		cv2.imwrite("Resultados/temporal_{}.jpg".format(ttl), difference)
		#Codigo para el sonidito
		#fname = "/home/nimperii/SauronScanner/OOT_Navi_Hello1.wav"
		#mysong = AudioSegment.from_mp3(fname)
		#play(mysong)

		print ("Las imagen {} es diferente.".format(ttl))
		
		img=mpimg.imread("Resultados/temporal_{}.jpg".format(ttl))
		imgplot = plt.imshow(img)
		plt.show()
	return("Done")