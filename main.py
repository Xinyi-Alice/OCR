#Environment python2.7
import sys
import base64
import requests
import json
from PIL import  Image,ImageDraw,ImageFont
import textwrap
# Put desired file path here
file_path ="images/algebra.jpg"

#Check file size
def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size
file = open(file_path, 'rb')
print 'The size of the file is:'
print getSize(file)

#Send request to Mathpix server
image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read())
r = requests.post("https://api.mathpix.com/v3/latex",
    data=json.dumps({"src": image_uri},{"ocr":["math", "text"]}),
    headers={"app_id": "xyzhang1228_163_com", "app_key": "a75fe1e5eee21d2c5820",
            "Content-type": "application/json"})

#Receiving results from Mathpix server, and extract the Latex information
LatexResults=str(r.text).split(',')[0].split('"')[3]
print 'LaTex:\n'+LatexResults

#Print output image-draw a blank canvas
im = Image.new("RGB",(600,400),"white")
fnt = ImageFont.truetype("arial.ttf",32)

#Print text to canvas
imageoutput='\n'.join(textwrap.wrap(LatexResults, 40))
ImageDraw.Draw(im).text((im.size[0]/10,im.size[1]/10),"Recogized LaTex Output:",fill='black',font=fnt)
ImageDraw.Draw(im).text((im.size[0]/10,im.size[1]/4),imageoutput,fill='black',font=fnt)


#Show and save image
im.show()
im.save("1.jpg")
