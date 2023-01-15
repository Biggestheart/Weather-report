"""
    Author: AnietieLEssien
    Date: 14 Jan 2023
    Name: PyWeather || Python
    
    Hi guys! just made a very very very simple weather app using python.😅
    Python is a really cool & interesting programming language.🙌🙌
    
    
    ###JUST INPUT YOUR LOCATION###
**Maybe it will take some time to load**
    

"""

import os

import requests

val = input("")
url = 'https://wttr.in/{}'.format(val)

print()
print(""" <iframe style="border:none;" width="100%" height="700px" src='"""+url+"""'></iframe> """)

os.system("touch file.png")