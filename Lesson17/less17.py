from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
bfup = BeautifulSoup(html.read(), 'html.parser')

name_list = bfup.find_all('span', {'class': 'green'})

for name in name_list:
    print(name.get_text())
