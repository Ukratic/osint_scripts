## Get EXIF data from image file
from PIL import Image
from PIL.ExifTags import TAGS
import tkinter as tk
from tkinter import filedialog

# read the image from dir
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
my_img = Image.open(file_path)
# extract exif data
exif_data = my_img.getexif()


# iterate over all exif data
for element_name in exif_data:
    # get tag name and data
    tag = TAGS.get(element_name)
    data = exif_data.get(element_name)
    # print tag name and data
    print(f"{tag}: {data}")