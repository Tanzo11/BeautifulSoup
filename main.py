import requests
from bs4 import BeautifulSoup
def fetchAndSaveToFile(url, path):
    r= requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)    



url ="https://timesofindia.indiatimes.com/city/kolkata"

fetchAndSaveToFile(url, "data/times.html")

with open("sample.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')
#print(soup.prettify())
#print(soup.title.string, type(soup.title.string))
#pssrint(soup.div)
#print(soup.find_all("div")[1])

#the link presnt
#for link in soup.find_all("a"):
#    #print(link)
#    print(link.get("href"))
#    print(link.get_text())

#the path locations
#s=soup.find(id="link3")
#print(s.get("href"))

#print(soup.select("span#italics"))   #for id #
#print(soup.select("div.italics"))    #for calss .
#print(soup.span.get("class"))

#print(soup.find(id="italics").string)

#print(soup.find_all(class_="italics"))  #as class is a keyword in python

#for child in soup.find(class_="container").children:#
#    print(child)

#for parent in soup.find(class_="box").parents:
#    print(parent)

#cont = soup.find(class_="container")
#cont.name = "span"
#cont["class"]="myclass class2"
#cont.string = "I am a string"
#print(cont)


"""ulTag = soup.new_tag("ul")
liTag = soup.new_tag("li")
liTag.string = "Home"
ulTag.append(liTag)

liTag = soup.new_tag("li")
liTag.string = "About"
ulTag.append(liTag)

soup.html.body.insert(0, ulTag)
with open("modified.html","w") as f:
    f.write(str(soup))"""

#cont = soup.find(class_="container")
#print(cont.has_attr("contenteditable"))   #whether there is this attribute in the class container


def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_attr("content")

#results = soup.find_all(has_class_but_not_id)
results = soup.find_all(has_content)

for result in results:
    print(result,"\n\n")

