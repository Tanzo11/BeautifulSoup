import requests
from bs4 import BeautifulSoup

data ={'title':[],'price':[],'image_url':[]}

n = int(input("Enter the no. of data you want : "))

url = "https://www.amazon.in/s?k=iphone"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


r= requests.get(url, headers=headers)

soup = BeautifulSoup(r.text,'html.parser')
#print(soup.prettify())

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price-whole")
images = soup.select("img.s-image")



count =0   # counter variable
for span in spans:
    #print(span.string)
    if count>= n:
        break
    data["title"].append(span.string)
    count+=1

count =0 #reset count to 0
for price in prices:
    #print(price.string)    
    if count>= n:
        break
    data['price'].append(price.string)
    count+=1

count = 0 #reset count to 0
for image in images:
    if count>=n:
        break
    data['image_url'].append(image['src'])

for i in range(len(data["title"])):
    print(f"{data['title'][i]}, ₹.{data['price'][i]} , Image URL: {data['image_url'][i]}")