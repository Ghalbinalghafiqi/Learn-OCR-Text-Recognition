import pytesseract as pyt

import cv2

img = cv2.imread("text_img.png")

pyt.pytesseract.tesseract_cmd = "C:\\Users\\HP\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

text = pyt.image_to_string(img)

print(text)

with open("text_file.txt", "w+") as f:
    f.write(text)