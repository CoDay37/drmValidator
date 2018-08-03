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


base_URL = 'http://mtv.com'

ffProfile = webdriver.FirefoxProfile('/home/cday/.mozilla/firefox/kv4pspx2.cdayP')

def getVideoSource(site):
        global totalL
        totalL+=1
        print('Video Number: ', totalL)
        print("Link: ", site)
        driver = webdriver.Firefox(ffProfile)
        try:
                driver.get(site)
                driver.implicitly_wait(45)
        except selenium.common.exceptions.TimeoutException:
                raise print("Selenium got stuck")
        html = driver.page_source    
                #MTV
                #vidLink = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/video").get_attribute('src')
                #HGTV
        #vidLink = driver.find_element_by_xpath("//*[@id='player_193-video-content]")
        """iframe= driver.find_element_by_id('player_139')
        driver.switch_to_frame(iframe)
        vidLink = driver.find_element_by_class_name('any-video-content')"""
        driver.execute_script("url = document.getElementsByTagName('video');var a = document.createElement('a');document.body.appendChild(a);a.style = 'display: none';a.href = url;a.setAttribute('download','Aname');a.click();window.URL.revokeObjectURL(url);")
        videoLinks.add(vidLink)
        print(vidLink)
        driver.close()

def findLinks(link):
        print(link)
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
                elif (('https' in sLink) or ('http' in sLink)):
                        unCheckedLinks.add(sLink)                  
                else:
                        continue
        holdSet = unCheckedLinks.copy()
        for element in holdSet:
                findEpisodes(element)  
        for element in unCheckedLinks: # will have to adjust for links without video in URL
                parseHTML.add(element)
        unCheckedLinks.clear()

def findEpisodes(url):
        if(('/shows/' in url) and ('/episode-guide') in url):
                print("Check findEpisodes Method")
        elif('/shows/' in url) or ('/show/' in url):
                req = requests.get(url, headers={'User-Agent': USER_AGENT})
                dataContent = req.content
                soupy = BeautifulSoup(dataContent,'html.parser')
                for link in soupy.findAll('a'):
                        if(base_URL not in link):
                                continue
                        else:
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
                        