#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
import requests
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

site = 'https://www.cbs.com'

r = requests.get(site)
data = r.text
soup = BeautifulSoup(data, "html.parser")
soup.prettify
for link in soup.findAll("a"):
    print(link.get('href'))
print()
print()
for link in soup.findAll("link"):
    print(link.get('href'))



listy = ['a','b','c','d','e']
tupy = ('apple','baby','collin','dog','eager')

#listy.append(tupy[3])
#listy.append(tupy[2])
#listy.append(tupy[4])
#listy.remove(tupy[2])

print(listy)
#for element in reversed(listy2):
    #print("The element is ", element)
    #print('b4', listy2)
    #listy2.remove(element)
    #print('after', listy2)
    #print("")
