import requests, urllib3, webbrowser, re
from bs4 import SoupStrainer, BeautifulSoup


url1 = 'http://tmastream.tk/'
url2 = 'https://www.youtube.com/watch?v=12m1rG0Tj7U'
url3 = 'https://www.theverge.com'


def getInfo(url):
    userAgent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
    r = requests.get(url, timeout = 1, headers = userAgent)
    urlContent = r.content
    soup = BeautifulSoup(urlContent, 'html.parser')
    links = []
    links = getAllLinks(urlContent)
    return links




def getAllLinks(content):
    links = []
    numberofLinks = 0
    for link in BeautifulSoup(content, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            links.append(link['href'])
            numberofLinks+=1
    print("There are ", numberofLinks, "on that site.")        
    return links






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

