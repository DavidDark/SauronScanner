from skimage.metrics import structural_similarity as compare_ssim
import cv2
import imutils

def comparar(ttl):
	try:
		ttl= ttl -1
		
		imagen1 = cv2.imread("Correcto.jpg")
		imagen2 = cv2.imread("Muestras/temp_{}.jpg".format(ttl))
		gray1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
		gray2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)

		(score,diff) = compare_ssim(gray1,gray2, full=True)
		diff = (diff * 255).astype("uint8")
		#Debug
		#print("SSIM: {}".format(score))

		if score == 1:
				print ("Las imagen {} es idéntica.".format(ttl))

		else:
			print ("Las imagen {} es diferente.".format(ttl))

			thresh = cv2.threshold(diff, 0, 255,
				cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
			cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
				cv2.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours(cnts)

			for c in cnts:
				(x, y, w, h) = cv2.boundingRect(c)
				#cv2.rectangle(imagen1, (x, y), (x + w, y + h), (0, 0, 255), 2)
				cv2.rectangle(imagen2, (x, y), (x + w, y + h), (0, 0, 255), 2)
				

			cv2.imshow("Original", cv2.resize(imagen1,(600,720)))
			cv2.imshow("Muestra", cv2.resize(imagen2,(600,720)))
			cv2.imshow("Diff", cv2.resize(diff,(600,720)))
			cv2.imshow("Thresh", cv2.resize(thresh,(600,720)))
			cv2.waitKey(0)

			cv2.destroyAllWindows()
			cv2.imwrite("Resultados/temporal{}.jpg".format(ttl), diff)
			
		return("Done")
	except:
		return("Ha ocurrido un error, ¿Está bien el orden de los archivos?")