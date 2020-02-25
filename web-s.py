from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

driver = webdriver.Chrome("C:\\Users\\kpraf\\Downloads\\chromedriver_win32\\chromedriver.exe")

products=[]
prices=[]
#ratings=[]
driver.get('https://www.mysmartprice.com/mobile/pricelist/samsung-mobile-price-list-in-india.html')

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

list_containers = soup.findAll('div', attrs={"class":"prdct-item__dtls"})
#print(type(list_containers))
#print(len(list_containers))

for div in list_containers:
    name=div.find('a', attrs={'class':'prdct-item__name'})
    #print(name)
    price=div.find('span', attrs={'class':'prdct-item__prc-val'})
    #print(price)

    if name:
        products.append(name.text)
    else:
        products.append(np.nan)
    if price:
        prices.append(price.text)
    else:
        prices.append(np.nan)
next_btn = soup.find('a', attrs={'data-pgno':'2'})

print(next_btn)


df = pd.DataFrame({'Product Name':products,'Price':prices,}) 
df.to_csv('Prafful_PyScrape.csv', index=False, encoding='utf-8')