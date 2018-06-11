#pip install lxml
#pip install requests
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urljoin
import urllib3
import requests
import os
import re
import random
from requests.exceptions import MissingSchema

websiteURL = 'https://www.theverge.com/'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'

payload = {'key': 'value1', 'key2': 'value2'}
#path = os.getcwd()

unCheckedLinks = set()
htmlChecked = set()
videoLinks = set()
randomLinks = set()

def getSourceCode(string):
        r = requests.get(string, headers={'User-Agent': USER_AGENT})
        data = r.text
        soup = BeautifulSoup(data,'html.parser')
        fData = str(soup.prettify)
        print("RESPONSE CODE", r.status_code)
        """file = open("websiteSource.txt", "w")
        file.write(fData)
        file.close"""
        #for link in soup.findAll("a")

def getAllLinks(listy):
        for element in listy: 
                link = str(element)
                link = link[2:-2]
                print(link)
                try:
                        r = requests.get(link,params=payload, headers={'User-Agent': USER_AGENT})
                        print("Response: ", r.status_code)
                        sourceText = r.text
                        file = open("websiteSource.txt", "w")
                        file.write(sourceText)
                        file.close()
                except MissingSchema:
                        print('Non working link: ' + link)
                        print(type(link))
                        print("***",link)

def findLinks():
        r = requests.get(websiteURL, headers={'User-Agent': USER_AGENT})
        print("Status: ", r.status_code)
        data = r.text
        soup = BeautifulSoup(data,'html.parser')
        fData = str(soup.prettify)
        for link in soup.findAll("a"):
                sLink = link.get('href')
                print("Link: ",sLink) 
                unCheckedLinks.add(sLink)
        for link in soup.findAll("link"):
                sLink2 = link.get('href')
                print("Link: ",sLink2) 
                unCheckedLinks.add(sLink2)


def linkChecker():
        notUsed = []
        numberof = 0
        for element in (unCheckedLinks):
                holder = str(element)
                extensionCheck = (holder[-7:-2])
                if(("") in extensionCheck):
                        unCheckedLinks.remove(element) 
                if(("jpg") in extensionCheck or ("png") in extensionCheck or ("svg") in extensionCheck or ("ico") in extensionCheck) or ("jpeg") in extensionCheck:
                        unCheckedLinks.remove(element)
                        randomLinks.add(element)
                if((".js") in extensionCheck or ("xml") in extensionCheck) or (".gif") in extensionCheck:
                        randomLinks.add(element)
                        unCheckedLinks.remove(element)
                if((".mp4") in extensionCheck):
                        videoLinks.add(element) 
                        unCheckedLinks.remove(element)
                else:
                        htmlChecked.add(element)
                        unCheckedLinks.remove(element)

def controller(url):
       # getSourceCode(url)
        findLinks()
       # linkChecker()
       # getAllLinks(htmlChecked)
        print("# of unchecked: ", len(unCheckedLinks))
        print("# of vid", len(videoLinks))
        print("# of random links", len(randomLinks))
        print("# of html", len(htmlChecked))
