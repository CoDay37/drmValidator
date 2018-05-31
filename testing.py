import urllib
from bs4 import BeautifulSoup as BS

url = 'https://www.youtube.com/watch?v=I9CT0ZLX4Wo'
#open and read page
page = urllib.request.urlopen(url)
html = page.read()
#create BeautifulSoup parse-able "soup"
soup = BS(html, "html.parser")
#get the src attribute from the video tag
video = soup.find_all('player', id='player')
print(video)