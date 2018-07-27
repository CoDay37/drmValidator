from selenium.common.exceptions import TimeoutException, NoSuchElementException
from requests.exceptions import MissingSchema
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
import requests
import random
import os
import re

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.2526.73 Safari/537.36'
unCheckedLinks = set()
parseHTML = set()
videoLinks = set()
totalL = 1
post = False
base_URL = 'http://www.mtv.com'

ffProfile = webdriver.FirefoxProfile('/home/cday/.mozilla/firefox/kv4pspx2.cdayP')

def getVideoSource(site):
        driver = webdriver.Firefox(ffProfile)
        print("CHECKING VIDEO: ", site)
        try:
                driver.get(site)
        except selenium.common.exceptions.TimeoutException:
                print("Selenium Stuck")
        driver.implicitly_wait(30)
        html = driver.page_source
        try:
                vidLink = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/video").get_attribute('src')
        except selenium.common.exceptions.NoSuchElementException:
                print("Cannot find vid source")

        videoLinks.add(vidLink)
        driver.close()

def findLinks(link):
        with requests.Session() as s:
                global post
                if post:
                        r = s.post(link, data=payload2)
                        post = False
                elif not post:
                        r = requests.get(link, headers={'User-Agent': USER_AGENT})
                data = r.content #Get html content
                soup = BeautifulSoup(data,'html.parser')
                global totalL
                print("Total Number of Links Parsed: ", totalL)
                totalL+=1
                print("Status:", r.status_code)
                for link in soup.findAll("a"):
                        sLink = link.get('href')
                        if(sLink == ''):
                                continue
                        elif (sLink is None):
                                continue
                        elif (sLink[0] == '/'):
                                combinedLink = (base_URL+sLink)
                                #unCheckedLinks.add(combinedLink)
                        elif (base_URL not in sLink):
                                continue
                        elif (('https' in sLink) or ('http' in sLink)):
                                unCheckedLinks.add(sLink)                  
                        else:
                                continue

                holdSet = unCheckedLinks.copy()
                for element in holdSet:
                        findEpisodes(element)  
                for element in unCheckedLinks: # will have to adjust for links without video in URL
                        if ('/episodes/' in element):
                                parseHTML.add(element)        
                unCheckedLinks.clear()
def findEpisodes(url):
        if(('/shows/' in url) and ('/episode-guide') in url):
                print()
        elif('/shows/' in url):
                req = requests.get(url, headers={'User-Agent': USER_AGENT})
                dataContent = req.content
                soupy = BeautifulSoup(dataContent,'html.parser')
                for link in soupy.findAll('a'):
                        sourceLink = link.get('href')
                        unCheckedLinks.add(sourceLink)




def downloadVideo(url):
        r = requests.head(url)
        header = r.headers
        content_type = header.get('content-type')
        if 'text' in content_type.lower():
                return False
        elif 'html' in content_type.lower():
                return False
        else:
                return True

def controller(url):
        findLinks(url)
        linksChecked = set() ##Going to hold all links parsed and checked
        keepLooping = True
        while keepLooping:
                holdingLinks = parseHTML.copy()
                for link in holdingLinks:
                        linksChecked.add(link)
                        findLinks(link)
                        getVideoSource(link)
                for link in linksChecked:
                        parseHTML.discard(link)
                if(len(parseHTML) == 0):
                        keepLooping = False
        counter = 1
        for element in videoLinks:
                print(counter, ": ", element)
        