from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www2.solarmoviesc.com/")
elem = driver.find_element_by_class_name("form-control")
elem.clear()
elem.send_keys("Infinity Wars")
elem = driver.find_element_by_tag_name("button")
elem.send_keys(Keys.RETURN)
elem = driver.find_elements_by_class_name("m1-item")
#elem.send_keys(Keys.RETURN)

i = 0
for line in elem:
    print(elem[i])
    i+=1
print(elem)

#driver.close()