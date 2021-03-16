from PIL import Image
import pytesseract as pyocr
import os
import glob

root_dir = r'path'
extensions = ('.jpg', '.jpeg', '.png')
destination_dir = r'path'
pyocr.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


tofile = []
file_name = []
for path, dirs, files in os.walk (root_dir):
    for file in files:
        if file.endswith(extensions):
            file_path = os.path.join(path, file)
            tofile = pyocr.image_to_string(Image.open(file_path))
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            destination_filepath = os.path.join(destination_dir, file_name + ".txt")
            d_file = open(destination_filepath, 'w', encoding="utf-8")
            d_file.write(tofile)
            d_file.close()


for filename in glob.glob(destination_dir + '/*.txt'):
    print (filename)
