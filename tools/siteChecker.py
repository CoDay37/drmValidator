import requests, urllib3, webbrowser, re
#import pC
from bs4 import SoupStrainer, BeautifulSoup


url1 = 'http://tmastream.tk/'
url2 = 'https://www.youtube.com/watch?v=12m1rG0Tj7U'
url3 = 'https://www.theverge.com'
url4 = 'http://www2.solarmoviesc.com/search/Infinity+Wars.html'

htmlSources = 0


userAgent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}

rp = requests.get(url4, headers = userAgent)
headInfo = rp.headers
contents = headInfo.get('content-type')
urlContent = rp.content

def getAllLinks(content):
    links = []
    numberofLinks = 0
    for link in BeautifulSoup(content, 'html.parser', parse_only=SoupStrainer('src')):
        if link.has_attr('href'):
            links.append(link['href'])
            print(link['href'])
            numberofLinks = numberofLinks + 1
    print("There are ", numberofLinks, " links on this site.")        
    htmlSources = 0
    for link in links:
        headerInfo = rp.headers
        contentType =headerInfo.get('content-type')
        if('text/html' in contentType):
            htmlSources+=1
    print('There are ', htmlSources, ' HTML sources.')
    return links


def getInfo(url):
    userAgent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
    r = requests.get(url, timeout = 1, headers = userAgent)
    urlContent = r.content
    soup = BeautifulSoup(urlContent, 'html.parser')
    links = []
    links = getAllLinks(urlContent)
    #return links

getInfo(url4)






#urls.update([a['href'] for a in soup.find_all('a', href=True)])
#print(urls)


#for link in soup.find_all('a'):
#    print(link.get('href'))

#holder = (link, '\n')
#print(holder)
    #urls.append(holder)

#print(samples)



#a_Tags = SoupStrainer('a')


#print(BeautifulSoup(url, 'html.parser', parse_only=a_Tags).prettify())

#print(a_Tags)

#auth = HTTPBasicAuth('fake@example.cm', 'password123')

#SoupStrainer = SoupStrainer(r.url)

#vidName = url2.split('/')[-1]

#print('HEADERS SENT:', r.request.headers)
#print(vidName)
#if(r.status_code == 200):
 #   print("GET succesful")

