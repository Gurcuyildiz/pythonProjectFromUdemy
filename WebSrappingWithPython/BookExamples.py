
import requests
import bs4

#here is the link of book and there are many pages, the below one is page 3
#http://books.toscrape.com/catalogue/page-2.html

#if we want to go to the pahe 20 or 12, delete the number and put curly braces, then insert format method
bas_url = 'http://books.toscrape.com/catalogue/page-{}.html'

page_num = 12
print(bas_url.format(page_num))# will go to page 12


#create another request
res = requests.get(bas_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
print(len(soup.select('.product_pod')))#20

