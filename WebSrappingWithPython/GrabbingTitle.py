
import requests

result = requests.get('http://www.example.com')

print(type(result))# requests.models.Response
#print(result.text)#this will give me all html content, but it will be raw string, very messy
#
import bs4
#
# #create a bs4 variable/object
soup = bs4.BeautifulSoup(result.text, 'lxml')
#print(soup)# this soup object will also give me html content with a beautiful design, readable format
#
#print(soup.select('title'))# will give me full of html title as a single list element
#print(soup.select('title')[0].getText()) # Example Domain => will give me just text not other info
# print(soup.select('p'))# this will give me all p paragraph as a list
#
# site_paragraph = soup.select('p')#all p paragpraph
#
# #if we want to grab the first paragraph
# print(site_paragraph[0].getText())