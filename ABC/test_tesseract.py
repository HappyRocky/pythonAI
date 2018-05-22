# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image

# 二值化    
threshold = 140    
table = []    
for i in range(256):    
    if i < threshold:    
        table.append(0)    
    else:    
        table.append(1)  
        
pytesseract.pytesseract.tesseract_cmd = 'D:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
image = Image.open('4.jpg')
image = image.convert('L')  
#image = image.point(table,'1')   
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)
