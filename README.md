## Osint scripts
- exif_img_file.py : Extracts metadata from image
- fake_profile.py : Generates a fake profile info and picture, outputs txt file (with profile details) and image file with the name of the fake profile.
- txt_from_pdf.py : Extracts text from a pdf file (all pages)
- txt_from_img.py : Extracts text from image (requires Tesseract OCR)
- youtube_dl.py : Downloads youtube video from a link

Extracting scripts open a file dialog to select the file. For multiple files, simply replace "filedialog.askopenfilename()" with "filedialog.askdirectory()" and loop over the files.