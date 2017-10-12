from urllib.request import urlopen
from bs4 import BeautifulSoup 
import ssl 

ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_39678.html"
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

total = 0 
tags = soup('span')
for tag in tags: 
	total += int(tag.contents[0])

print(total)
