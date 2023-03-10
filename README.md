## Osint scripts
- exif_img_file.py : Extract metadata from image
- fake_profile.py : Generate fake profile info from randomized EU locale
- txt_from_pdf.py : Extract text from a pdf file (all pages)
- txt_from_img.py : Extract text from image (requires Tesseract OCR)
- youtube_dl.py : Download youtube video

Most scripts open a file dialog to select the file. For multiple files, simply replace "filedialog.askopenfilename()" with "filedialog.askdirectory()" and loop over the files.