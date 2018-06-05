#pip install lxml
#pip install requests
from bs4 import BeautifulSoup, SoupStrainer
import urllib3
import requests
import os
import re

websiteURL = 'https://www.theverge.com/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
path = os.getcwd()

def getSourceCode(string):
        payload = {'key': 'value1', 'key2': 'value2'}
        r = requests.get(string,params=payload, headers={'User-Agent': USER_AGENT})
        pageText = r.text
        file = open("websiteSource.txt", "w")
        file.write(pageText)
        file.close
        findLinks()

def getAllLinks(content):
    links = []
    numberofLinks = 0
    with open("findLinks.txt", "a") as wk:
        for line in BeautifulSoup(content, 'html.parser'):
                print("YOLO",line)
                """if "src" or "link" or "<a" or "href":
                        print(line)
                        wk.write(line)
                        links.append(line)
                        numberofLinks = numberofLinks + 1"""
        print("There are ", numberofLinks, " links on this site.")           
        #print(links)

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
               m = re.search(r"https?", element)
               if(m):
                       links.append(element)
                       print(element)
