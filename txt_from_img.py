import tkinter as tk
from tkinter import filedialog
from PIL import Image
from pytesseract import pytesseract

# tesseract path
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = tesseract_path

# read the image from dir
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
my_img = Image.open(file_path)

# extract text from image
# might need to specify parameter such as lang='eng' in some cases
text = pytesseract.image_to_string(my_img)
print(text)