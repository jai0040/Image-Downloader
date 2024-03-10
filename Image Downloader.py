#Image Downloader
import urllib.request 
from PIL import Image 

# Corrected URL without backslashes
#url = "https://media.geeksforgeeks.org/wp-content/uploads/20210224040124/JSBinCollaborativeJavaScriptDebugging6-300x160.png" 
#urllib.request.urlretrieve(url, "geeksforgeeks.png") 

img = Image.open("Scenery.jpg") 

# Opening the image and displaying it
img = Image.open("geeksforgeeks.png") 
img.show()
