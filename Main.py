import os
import glob
import configparser
import Compare
import setup


#Comprueba si existen las carpetas, si no existen, las crea
stp= setup.stp()
print(stp)

while 1:
	#Toma como variable la cantidad de muestras en la carpeta
	ttl= len(glob.glob("Muestras/*.jpg"))

	#Toma como variable el valor que se encuentra en el archivo init
	#Como si fuera un cache con el valor anterior de ttl
	cache= configparser.ConfigParser()
	cache.read("config.ini")
	cnum = cache.getint("var", "ttl")
	if ttl == 0:
		continue
	else:
		#Compara si la cant en la carpeta es diferente al cache
		if ttl != cnum:
			#Si es diferente ejecuta las comparaciones de muestra
			res= Compare.comparar(ttl)
			cnums= str(ttl)
			cache.set('var', 'ttl', cnums)
			#Y actualiza el valor en el cache por el valor actual
			with open('config.ini', 'w') as configfile:
				cache.write(configfile)

			print(res)
		else:
			continue
