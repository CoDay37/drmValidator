#pip install lxml
#pip install requests
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urljoin
import urllib3
import requests
import os
import re
from requests.exceptions import MissingSchema

websiteURL = 'https://www.theverge.com/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
payload = {'key': 'value1', 'key2': 'value2'}
#path = os.getcwd()

nonCheckedLinks = []
htmlCheckedList = []
photoLinkList = []
videoLinkList = []
missLinkList = []


def getSourceCode(string):
        r = requests.get(string,params=payload, headers={'User-Agent': USER_AGENT})
        pageText = r.text
        file = open("websiteSource.txt", "w")
        file.write(pageText)
        file.close

def getAllLinks(listy):
        for element in listy: 
                link = str(element)
                link = link[2:-2]
                #print( link)
                try:
                        r = requests.get(link,params=payload, headers={'User-Agent': USER_AGENT})
                except MissingSchema:
                        print('Non working link: ' + link)
                        print(type(link))
                        print(link)

def findLinks():
        halfParsed = []
        links = []
        lineNum = 1
        with open("websiteSource.txt") as sc:
                lines = (line.rstrip() for line in sc)
                lines = (line for line in lines if line)            
                for line in enumerate(sc):
                        line = sc.readline()
                        if(line.isspace() == True):
                                continue
                        else:
                                halfParsed.append(line)
        for element in halfParsed:
               foundLinks = re.search(r"https?", element)
               if(foundLinks):
                       links.append(element)
        for element in links:
                urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', element)
                nonCheckedLinks.append(urls)

def linkChecker():
        notUsed = []
        numberof = 0
        print("2")
        for element in reversed(nonCheckedLinks):
                holder = str(element)
                extensionCheck = (holder[-7:-2])
                print("***", element)
                if(("") in extensionCheck):
                        nonCheckedLinks.remove(element) 
                if((".jpg") in extensionCheck or ("png") in extensionCheck or ("svg") in extensionCheck or ("ico") in extensionCheck):
                        photoLinkList.append(element)
                        print("****************", element)
                        nonCheckedLinks.remove(element)
                if((".js") in extensionCheck or ("xml") in extensionCheck):
                        missLinkList.append(element)
                        nonCheckedLinks.remove(element)
                if((".mp4") in extensionCheck):
                        videoLinkList.append(element)
                        videoLinkList.remove(element)    

def controller(url):
        getSourceCode(url)
        findLinks()
        linkChecker()
        getAllLinks(nonCheckedLinks)
