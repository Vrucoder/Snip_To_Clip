'''
Using PILLOW for Image sharpening better accurates the tesseract OCR.
Web refs:
    The clipboard types in windows: https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa359736(v=vs.85)
    Image Sharpening: https://pythonexamples.org/python-pillow-adjust-image-sharpness/
    Pillow ImageEnhance docs: https://pillow.readthedocs.io/en/3.0.x/reference/ImageEnhance.html
'''
import sys
import pytesseract
from PIL import Image
import time
import os
import pyperclip
from PIL import ImageEnhance
from time import strftime

# Edit this.
pytesseract.pytesseract.tesseract_cmd = (
    r"path\to\tesseract.exe"
)

# Edit this.
os.chdir(r"path\to\designated_snip_folder")

image = Image.open(sys.argv[1])
enhancer = ImageEnhance.Sharpness(image)

#  a factor of 2.0 gives a sharpened image
sharp = enhancer.enhance(2.0)

filename = 'img ' + strftime("%Y_%m_%d %H-%M-%S") + '.png'
sharp.save(filename)

text = pytesseract.image_to_string(Image.open(filename))

print(text)

option1 = str(input("Do you want to copy it?"))

yes = ["y", "Y", "Yes", "YES"]

if option1 in yes:
    pyperclip.copy(text)
    print("copied that.")
else:
    print("didn't copy that.")

option2 = str(input("Do you want to delete sharpened image replica? "))

if option2 in yes:
    os.remove(filename)
    print(filename + " deleted from " + str(os.getcwd()))
else:
    pass

