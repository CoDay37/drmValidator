from selenium import webdriver


broswer = webdriver.PhantomJS()
broswer.get("http://www.spectrumsportsnet.com/videos/2018/07/derek-fisher-reacts-to-lebron-james-coming-to-lakers")

iframe  = broswer.find_element_by_tag_name("video")
broswer.switch_to.default_content()
broswer.switch_to.frame(iframe)
iframe_source = broswer.page_source
print(iframe_source)
print()
print(broswer.current_url)