import pytesseract as pyt
import cv2
import os 

#? mencari file gambar di directory yang sama dengan script
current_directory = os.getcwd()
image_files = [f for f in os.listdir(current_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not image_files:
    print("Tidak ada file gambar (PNG atau JPG) di direktori ini.")
else:
    for image_file in image_files:
        print(f"Memproses file gambar: {image_file}")
        
        # Membaca gambar
        img = cv2.imread(image_file)

        # Path ke executable Tesseract
        pyt.pytesseract.tesseract_cmd = "C:\\Users\\HP\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

        # Ekstraksi teks dari gambar
        text = pyt.image_to_string(img)

        print(f"Teks yang diekstrak dari {image_file}:")
        print(text)

        # Menyimpan hasil ekstraksi ke file teks
        output_file = os.path.splitext(image_file)[0] + "_output.txt"
        with open(output_file, "w+") as f:
            f.write(text)

        print(f"Teks dari {image_file} telah disimpan di file: {output_file}")