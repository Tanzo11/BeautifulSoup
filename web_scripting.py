from bs4 import BeautifulSoup
import requests

with open("index.html","r") as f:
    doc = BeautifulSoup(f,"html.parser")

#print(doc.prettify())
    
tags = doc.title
#tag.string = "Hello"
print(tags.string)

#tags = doc.find("p")
tags=doc.find_all("a")

print(tags)

tags=doc.find_all("p")[0]
print(tags.find_all("b"))


