#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
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
#3file_type = ['.png','jpg']
##string = "thisisfile.jpg"
#if((#string[-4:]) == '.jpg'):
    #print("SHE DO")
#else:
    #print(string[-4:])
#
##driver.close()


listy = ['a','b','c','d','e']

for element in reversed(listy):
    print("The element is ", element)
    print('b4', listy)
    listy.remove(element)
    print('after', listy)
    print("")
