#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import requests
from selenium import webdriver
import re
"""
driver = webdriver.Firefox()
driver.get("http://www2.solarmoviesc.com/")
elem = driver.find_element_by_class_name("form-control")
elem.clear()
elem.send_keys("Infinity Wars")
elem = driver.find_element_by_tag_name("button")
elem.send_keys(Keys.RETURN)
elem = driver.find_elements_by_class_name("m1-item")
#
#"""
headers = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.2526.73 Safari/537.36'
site = 'http://www.spectrumsportsnet.com/videos/2018/07/james-worthy-reacts-to-lebron-james-coming-to-lakers'




browser = webdriver.Chrome()
browser.get(site)
html = browser.page_source
print(type(html))
links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
for url in links:
    if ("ns11.ns.twc") in url:
        print(url)
#browser.close()
