#Scanner.py
import cv2
import numpy as np

img =cv2.imread("Correcto.jpg")
height, width = img.shape[:2]

#Coordinates
start_row, start_col = int(height*.5), int(width*.5)

end_row, end_col = int(height*.95), int(width*.95)

crop = img[start_row:end_row, start_col:end_col]

cv2.imshow('Crop', crop)
cv2.waitKey(0)