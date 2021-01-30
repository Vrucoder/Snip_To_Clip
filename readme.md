Pre-requisites: As of now, this hack works on windows computers. Python needs to be preinstalled.  

It happens that you find a bunch of text data in an image and you want to use it somewhere. Now, you may manually copy it, but it can be time consuming, if the data is large. 

So, here is the script which uses Google's Tesseract OCR to get the text out of that image and put it on your clipboard. 

Steps to use:

 1. Download and Install Tesseract OCR from [here](https://tesseract-ocr.github.io/tessdoc/Home.html). Copy and add the path to tesseract.exe in the python script here:
*pytesseract.pytesseract.tesseract_cmd = (r"**path\to\tesseract.exe**")*
 2. Install [pytesseract](https://pypi.org/project/pytesseract/), [pillow](https://pypi.org/project/Pillow/), [pyperclip](https://pypi.org/project/pyperclip/) using pip from command line.
 3. Make a designated folder where you will keep/save the images/snips from which the text has to be extracted. Edit the python file and add the path to this folder in the line having the *os.chdir(r"***here**
*")*** .
 4. Download the Edit the batch file to put the python file address in your system and keep the batch file in a folder which is set as path environment variable. 
 5. Press "Win+R", type the name of the batch file [SPACE] name of the desired image file with format. 

> Written with [StackEdit](https://stackedit.io/).