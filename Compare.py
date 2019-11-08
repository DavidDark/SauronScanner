import cv2
import numpy as np
import glob
import os
import shutil
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

if not os.path.exists("Resultados"):
	os.mkdir("Resultados")
else:
	try:
		shutil.rmtree("Resultados")
		os.mkdir("Resultados")
	except OSError as e:
		print ("Error: %s - %s." % (e.filename, e.strerror))


#res= len(glob.glob("Resultados/*.jpg"))
ttl= len(glob.glob("Muestras/*.jpg"))
imagen1 = cv2.imread("Correcto.jpg")

for i in range(0,ttl):

	imagen2 = cv2.imread("Muestras/temp_{}.jpg".format(i))

	difference = cv2.subtract(imagen1, imagen2)

	result = not np.any(difference) #if difference is all zeros it will return False
	
	if result is True:
		print ("Las imagen {} es idéntica.".format(i))

	else:
		
		cv2.imwrite("Resultados/temporal_{}.jpg".format(i), difference)
		print ("Las imagen {} es diferente.".format(i))
	
		#img=mpimg.imread("Resultados/temporal_{}.jpg".format(res))
		#imgplot = plt.imshow(img)
		#plt.show()