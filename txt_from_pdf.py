import pdfplumber
import tkinter as tk
from tkinter import filedialog

# read the image from dir
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

# extract text from pdf and print out all pages
with pdfplumber.open(file_path) as pdf:
    for page in pdf.pages:
        print(page.extract_text())