#pip install lxml
#pip install requests

import requests
#import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("https://play.hbogo.com/")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('div'))



#print(soup.find_all('p'))

