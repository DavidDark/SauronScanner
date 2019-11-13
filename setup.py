import os
import shutil

def stp():
	if not os.path.exists("Resultados"):
		os.mkdir("Resultados")
	else:
		try:
			shutil.rmtree("Resultados")
			os.mkdir("Resultados")
		except OSError as e:
			print ("Error: %s - %s." % (e.filename, e.strerror))
	
	if not os.path.exists("Muestras"):
		os.mkdir("Muestras")

	return("Corriendo Aplicación.")