#Python Library 'Requests' (HTTP/1.1)
import requests

import os
from PIL import Image
from IPython.display import IFrame
from requests.api import request

#Make a GET request via method get to url:
url='https://www.ibm.com/'
r=requests.get(url)

#View status code:
r.status_code

#View the request headers:
print(r.request.headers)

#View request body:
print('request body:', r.request.body)

#View the HTTP response header:
header=r.headers
print(r.headers)

#Obtain the request date:
header['date']

#Obtain the type of data:
header['Content-type']

#Check encoding:
r.encoding

#Review characters of the HTML's body:
r.text[0:100]

#Loading other types of data for non-text requests, like images:
# Use single quotation marks for defining string
url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'

#Get request:
r=requests.get(url)
print(r.headers)

#Content type:
r.headers['Content-Type']

#Specify the file path and name
path=os.path.join(os.getcwd(), 'image.png')
path

#access the body of the response:
with open(path,'wb') as f:
    f.write(r.content)
    
#View image:
Image.open(path)
