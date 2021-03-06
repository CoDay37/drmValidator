from selenium.common.exceptions import TimeoutException, NoSuchElementException
from requests.exceptions import MissingSchema
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
"""import org.openqa.selenium.JavascriptExecutor"""
import requests
import random
import os
import re

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.2526.73 Safari/537.36'
unCheckedLinks = set()
parseHTML = set()
videoLinks = set()
totalL = 0


base_URL = 'http://www.nbc.com'

ffProfile = webdriver.FirefoxProfile('/home/cday/.mozilla/firefox/kv4pspx2.cdayP')

def getVideoSource(site):
        global totalL
        totalL+=1
        print('Video Number: ', totalL)
        print("Link: ", site)
        driver = webdriver.Firefox(ffProfile)
        """r = requests.get(site, headers={'User-Agent': USER_AGENT})
        data = r.content #Get html content
        soup = BeautifulSoup(data,'html.parser')
        for link in soup.findAll("a"):"""

        try:
                driver.get(site)
                driver.implicitly_wait(45)
        except selenium.common.exceptions.TimeoutException:
                raise print("Selenium got stuck")     
        driver.switch_to_frame('player')
        driver.find_element_by_class_name('tpPlayOverlay').click()
        vidLink = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/video[1]').get_attribute('src')


#        driver.execute_script("url = document.getElementsByTagName('video');var a = document.createElement('a');document.body.appendChild(a);a.style = 'display: none';a.href = url;a.setAttribute('download','Aname');a.click();window.URL.revokeObjectURL(url);")
        videoLinks.add(vidLink)
        print(vidLink)
        print()
        driver.close()

def findLinks(link):
        r = requests.get(link, headers={'User-Agent': USER_AGENT})
        print(r.status_code)
        data = r.content #Get html content
        soup = BeautifulSoup(data,'html.parser')
        for link in soup.findAll("a"):
                sLink = link.get('href')
                if(sLink == ''):
                        continue
                elif (sLink is None):
                        continue
                elif (sLink[0] == '/'):
                        combinedLink = (base_URL+sLink)
                        unCheckedLinks.add(combinedLink)
                elif (base_URL not in sLink):
                        continue             
                else:
                        continue
        holdSet = unCheckedLinks.copy()
        unCheckedLinks.clear()
        for element in holdSet:
                findEpisodes(element)  
        for element in unCheckedLinks: # will have to adjust for links without video in URL
                parseHTML.add(element)
        unCheckedLinks.clear()

def findEpisodes(url):
        req = requests.get(url, headers={'User-Agent': USER_AGENT})
        dataContent = req.content
        soupy = BeautifulSoup(dataContent,'html.parser')
        print(soupy.prettify())
        for link in soupy.findAll('a'):

                if('/video/' in link):
                        sourceLink = link.get('href')
                        fullLink = (base_URL+sourceLink)
                        unCheckedLinks.add(fullLink)

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
                        