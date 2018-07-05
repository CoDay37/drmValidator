#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
import requests
from selenium import webdriver
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

#browser.quit()
"""print("site:", type(site))
print("headers:", type(headers))

r = requests.get(site, headers={'User-Agent': headers})

soup = BeautifulSoup(r.text, "html.parser")
soup.prettify
print()
for link in soup.findAll("video"):
    print(link.get('src'))

print(soup)
"""


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
