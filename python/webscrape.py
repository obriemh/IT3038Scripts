import requests, re 
from bs4 import BeautifulSoup 
 
data = requests.get("https://shop.gobearcats.com/Cincinnati-Bearcats-Alumni-Stickers-5700588?location=29&quantity=1&custcol_hardline_sizes=537").content
soup = BeautifulSoup(data, 'html.parser') 
span = soup.find("h1", {"id":"ProductNameHeader_Desktop"})
title = span.text
span = soup.find("span", {"class":"product-views-price-lead"}) 
price = span.text
print("The item with the name %s has a price of %s" % (title, price))

