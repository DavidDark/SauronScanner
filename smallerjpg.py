import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
from PIL import Image

# My image is a 200x374 jpeg that is 102kb large
try:
	foo = Image.open("Correcto.jpg")
	#foo.size(4250,5500)
	# I downsize the image with an ANTIALIAS filter (gives the highest quality)
	foo = foo.resize((1700,2338),Image.ANTIALIAS)
	foo.save("Correcto_resize.jpg",quality=95)
	# The saved downsized image size is 24.8kb
	foo.save("Correcto_resize_opt.jpg",optimize=True,quality=95)
	# The saved downsized image size is 22.9kb
except:
	print("Valió vrga")