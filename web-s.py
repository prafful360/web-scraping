from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:\\Users\\kpraf\\Downloads\\chromedriver_win32\\chromedriver.exe")

products=[]
prices=[]
#ratings=[]
driver.get('https://www.flipkart.com/computers/laptops/pr?sid=6bo,b5g&q=laptops&otracker=categorytree')

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    #rating=a.find('div', attrs={'class':'hGSR34'})
    products.append(name.text)
    prices.append(price.text)
    #ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,}) 
df.to_csv('products.csv', index=False, encoding='utf-8')