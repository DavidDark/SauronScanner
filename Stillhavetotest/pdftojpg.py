from pdf2image import convert_from_path

pages = convert_from_path('test1.pdf', 500)

for page in pages:
    page.save('temp_1.jpg', 'JPEG')