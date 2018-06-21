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
htmlLinks = 0
totalL = 0
base_URL = 'https://www.nbc.com'
payload = {#For Xfinity
    'user': 'nctatech',
    'passwd': 'TechLab!'
}
payload2 = {
    'IDToken1':'Men254@charter.net',
    'IDToken2':'Adam1041'
}


def getAllLinks(parseHTML):
        apple = parseHTML.copy()
        chc = (len(apple))
        for element in apple:
                chc-=1
                print("Remaining: ", chc)
                print(element)
                cleanLink = (element[2:-2])
                findLinks(cleanLink)
                parseHTML.remove(element)
        linkChecker()

        #for element in apple:
        #        hold = element[2:-2]
         #       findLinks(hold)

def findLinks(link):
        with requests.Session() as s:
                p = s.post(link, data=payload)
                #r = requests.get(link, headers={'User-Agent': USER_AGENT})
                data = p.content
                soup = BeautifulSoup(data,'html.parser')
                soup.prettify
                global totalL
                totalL+=1
                #print("Total Number of Links Parsed: ", totalL)

                print("Status:", p.status_code)
                links = soup.find_all('a',href=True)
                links2 = soup.find_all('link',href=True)
                for i in links2:
                        link = i.get('href')
                        unCheckedLinks.add(link)
                        #print("i", link)
                for link in soup.findAll("a"):
                        sLink = link.get('href')
                        #print("slink",sLink)
                        unCheckedLinks.add(sLink)
                for link in soup.findAll("link"):
                        sLink2 = link.get('href')
                        #print('slink2',sLink2)
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
                #TO_DO TOMORROW
                #ENSURE THAT PARSER STAYS ON WEBSITE


def linkChecker():
        for element in holdLinks:
                if 'ico' in element or 'png' in element or 'jpg' in element or "woff2" in element or 'css' in element or 'js' in element or "xml" in element:
                        randomLinks.add(element)
                elif 'mp4' in element or 'mpeg' in element or 'wmv' in element or '.mov' in element:
                        videoLinks.add(element)
                        print(element)
                elif 'twitter' in element or 'facebook' in element or 'google.com' in element or 'instagram.com' in element:
                        continue
                elif 'cbs' not in element:
                        continue
                else:
                        parseHTML.add(element)
                        print(element)
        print("Length of parseHTML", len(parseHTML))
        holdLinks.clear()

def controller(url):
        findLinks(url)
        linkChecker()
        print("### GETTING ALL LINKS")
        control = range(len(parseHTML))
        controlll = 2
        for i in control:
                getAllLinks(parseHTML)                
        print("# of unchecked: ", len(unCheckedLinks))
        print("# of vid", len(videoLinks))
        print("# of random links", len(randomLinks))

