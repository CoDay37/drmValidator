#pip install lxml
#pip install requests
from bs4 import BeautifulSoup, SoupStrainer
import urllib3
import requests
import os
import re
import random
from requests.exceptions import MissingSchema

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
payload = {'key': 'value1', 'key2': 'value2'}
#path = os.getcwd()
unCheckedLinks = set()
parseHTML = set()
videoLinks = set()
randomLinks = set()
holdLinks = set()
lengthOf = len(parseHTML)


def getAllLinks(parseHTML):
        apple = parseHTML.copy()
        print("Length of parseHTML: ", len(parseHTML))
        for element in apple:
                hold = element[2:-2]
                print("*******", element)
                findLinks(hold)

def findLinks(link):
        aLink = 'http'
        bLink = 'https'
        r = requests.get(link, headers={'User-Agent': USER_AGENT})
        print("Status: ", r.status_code)
        data = r.text
        soup = BeautifulSoup(data,'html.parser')
        for link in soup.findAll("a"):
                sLink = link.get('href') 
                unCheckedLinks.add(sLink)
        for link in soup.findAll("link"):
                sLink2 = link.get('href')
                unCheckedLinks.add(sLink2)
        for element in unCheckedLinks:
                holding = str(element)
                url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', holding)
                link = str(url)
                if not "http" in link or not "https" in link:
                        continue
                else:
                        holdLinks.add(link)
        unCheckedLinks.clear()
        linkChecker()
        #TO_DO TOMORROW
        #duplicate set and use to control recurisive loop
        #USE request.sessions to login with username/pW

def linkChecker():
        print("Length of HoldLinks: ", len(holdLinks))
        for element in (holdLinks):
                if 'ico' in element or 'png' in element or 'jpg' in element or "woff2" in element or 'css' in element or 'js' in element or "xml" in element:
                        randomLinks.add(element)
                elif 'mp4' in element or 'mpeg' in element or 'wmv' in element or 'mov' in element:
                        videoLinks.add(element)
                if not element:
                        continue
                else: 
                        parseHTML.add(element)
        holdLinks.clear()
                
                        
def controller(url):
        findLinks(url)
        #linkChecker()
        getAllLinks(parseHTML)
        print("# of unchecked: ", len(unCheckedLinks))
        print("# of vid", len(videoLinks))
        print("# of random links", len(randomLinks))

        for elemet in randomLinks:
                print("**", elemet)

        for element in videoLinks:
                print(element)

