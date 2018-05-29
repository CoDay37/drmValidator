#pip install lxml
#pip install requests
import requests
from bs4 import BeautifulSoup

def parse_videoHTML():
    header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
    sb_get = requests.get("https://www.youtube.com", headers = header)
    sb_get.content

    scrape_url="https://www.youtube.com"
    search_url="/results?search_query="
    search_hardcode = "game+of+thrones"
    website_url = scrape_url + search_url + search_hardcode
    sb_get = requests.get(website_url, headers = header)
    sb_get.content

    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")

    for x in yt_links:
        yt_href = x.get("href")
        yt_title = x.get("title")
        yt_final = scrape_url + yt_href
        print(yt_title + '\n' + yt_final + '\n')


















#page = requests.get("https://play.hbogo.com/")
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.find_all('div'))

#url = 'http://www.growingagreenerworld.com/episode125/'
#with requests.Session() as session:
  #  session.headers = headers

 #   response = session.get(url)

  #  soup = BeautifulSoup(response.content)

    # follow the iframe url
  #  response = session.get('http:' + soup.iframe['src'], headers={'Referer': url})
  #  soup = BeautifulSoup(response.content)

    # extract the video URL from the script tag
 #   print re.search(r'"url":"(.*?)"', soup.script.text).group(1)


#print(soup.find_all('p'))

