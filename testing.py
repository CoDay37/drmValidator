from requests.exceptions import MissingSchema
from selenium.webdriver import ActionChains, Firefox
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import requests
import random
import os
import re

site = 'http://www.spectrumsportsnet.com/videos/livetv/player'

site2 = 'http://watch.foodnetwork.com/live/?ic1=TVE_FN_Videos-textlink'
site2re = 'https://login.xfinity.com/login?r=comcast.net&s=oauth&continue=https%3A%2F%2Foauth.xfinity.com%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2Fsp.auth.adobe.com%2Fadobe-services%2Foauth2%26state%3DYR87VZ%26scope%3Dopenid%2520profile%2520https%3A%2F%2Flogin.comcast.net%2Fpdp%2Ftve%26client_id%3Dadobepass-foodnetwork%26acr_values%3Durn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Aac%3Aclasses%3AInternetProtocol%26response%3D1&ipAddrAuthn=1&client_id=adobepass-foodnetwork&reqId=36d603df-8ab0-4679-9ff1-d7e12752ce9b'

site3 = 'http://watch.hgtv.com/live/?ic1=TVE_HGTV_Shows-ChannelPage-RightRail'

site4 = 'http://www.dishanywhere.com/networks/tennis_channel_235'

site5 = 'https://idp.aws.spectrum.net/openam/SSOPOST/metaAlias/charter/idp?SAMLRequest=nVhJl6LYEt77K%2FLYS08mg6jgqcw%2BlxkVZVRhx3AFlEEZRPj1DzXTZ1Xl69fdCxY3iPhi5kbw489LEr%2BcYV5EWfrex97Q%2FgtMvcyP0uC9bxr8K9n%2F86P3o3CSGD9OQVWGqQZPFSzKF1AUMC87OSZLiyqBuQ7zc%2BRBU1u898OyPBZTBCmOb04n9Ob4mQvfvCzpKMgVDdGBvPgNov%2FCdtBR6pQ3e75QIr%2BDqYs3L3TyEuZvKSynBDFEsiNMnQTR9ZWy0g0kgaUD4sgpkE%2FGq2D%2Fhc9yD95Mf%2B%2BXeQX7LxL73ndG%2BC4c%2BuTYGe0oPyB8chcF6M51J74zDDueQnGKIjrD9%2F7OiYurVFFUUEqL0knL9z6OYuQrOnnFMAOjphg6Ram3IUXa%2FRclz8rMy2I6Su9xrPJ0mjlFVEw7a2ExLb3p1fsp%2FoZO3TtTMRUNQ3m9utF%2FWX%2FlA7%2Fmo8tQWkzvGfhrrOOn4v7HPWHTm8X5M8JfAzhf%2Beh%2FPBLYSb39lsUfyLOCjx9%2BMdWjoEtblcNPdX5xz1%2BHUdf1Wz18y%2FIAwVEURVAK6Xj8Igr%2B6D9koS%2Blu%2Bx2ZJw0SyPPiaP2VggyLMPMfwFxkOVRGSb%2FAxhDMPQK%2FAov3quHEekffeRn0%2F4m0E8W5oXzWoQO9omlwR3MuxaBL6Ymvff%2F%2BD9ldJMxcictdlmeFD8f%2F5khMD3DuKt4%2F7X48ufTpr8P%2BH2IkN9tZKOga8R%2FE6%2BnWN1B1k5cwY%2FcMRrmaNXsGhkN5qUEzaYhrbFejoj3mwHPzDfCI9L34y818sjpXSLBtaNe1FpSib5AqsVC1kdYdihjkAEVGbnbTAXbkhxGerNK7ePAHBzy%2BDyZbSOcPAhMap23zDi6bB0HkiNM1yZz4XLJ6QO%2FrvbWEnIFbQQNwvCLcmaSHk2cm1gfajYxbzA3OTWNKPNJ1n0ALXuhkYEdeRUx0DfnYp826dxa6sMjtVttlxnLs7oZKcOJvB8rrkbrBnQ52ccHjkEz27NGKc5y4e%2B3q4KxmgMDCfyQHpE5oyuGB0RFPA%2FGHij31gjZMpeTwMrcVq9n2dJmGarg0IFvT8a5yOFbvj1pdTC62Kgg81kmK3i8bgfylrKpIZftuSYYahGwLsranlUI3sQR15CsjSzS2PSzJbxcvBK8vz9C%2FxTra%2FjnsHmkYjtCKdYpnceBuX5Edl0Dl%2FBDliSebRkGIDAAtUSDQFKV1eki6GNtxmeamFS8gBIVYoAlHRxO4SESqBqlgVrwgKUHslrUjGqxa1UVelw9W5st58t0IQDM5JhQNs1hXFqbEWpv5EDFqcYTqMbaakcXJy5iC3w6WK5pUBh8vBy5G77yhfVe4rWm52%2BXqMSNYl%2F0z15SXBYtKO%2FMsjF7ZuaWhbVdthIrBya%2B3vvbWSzxy9hL7diLaFbVQdmTOA%2BVaWLLGhwms16zbEEts93DZ1cacadJ7dI4YKt1Vgf24cK0YHZXaBkgXhuyJtdc52qv81ViwZG1NpejnVCNm8ShrHE1W9%2FiILIgNKwNEegJ1doGt5cZ7h6OoHbUjXa2EjPowtJ21pc9r6FnbrI8eynducl3cVIvHYLzGReZw%2BjG2WCxL8Sl3bki8XToDeVgzVtP8ZNlPl2GPXdTV94QVNZ2jTrMKLQFKrL10d7F0ToIuEgGqMDoJ0GX3CGrcl0WTQAIiWZrcH0%2FB1lXASor2IWU9%2BZWEFOYFZUVVIOJqZ1F8bKqKhietuIcQ1QyRLLBCRGHXjJ3g5oqFcgpgsWEO0vcKBuSzwvgEmdyFtDznrSzTdGaMVAbuIcN2VwUauSRIemx%2BQXuwsOOQcAuviietZu0zWxBCkqbkKudmfoIba4ibW2uhHk9qVyy6Q3ooymkw%2FOsEtbVAGXYmC%2BDpkvKpHUIZ7Uxd7yLpIrit0lMLXX8JHLRZViRwFoMeJYYj%2FdjIIumZ4gjq4cVZ5BuDHszw%2FcQOxyPhFsJymSPcOVADs2c8UlITIY6DuujwO%2BqBe9gpJkP1aC5CGeZXZSnzE%2FGxlZr6N5pTKkC6pu4sNT3dXW2UVDzuDaSObReRJQLApkGQNgHAZ93rUfbLQivGRQ1jhP2wApCu7U2WLFIl3VvkfCYLwSVda%2BZysKpUgaHay35XK0yMgA1G3Q1p6EKUEXkmjoQbDoV6I1npqobmVYFhimEXpdqnq5lmg6CnA44nlY9Fuzpu3YdcJs9bcm8JdAJpFnAMd07WWbkm%2FBdVqL50M98Uat7XpudF7ja1VrX3Lh0s2yBL2uvBfGTgg4E2MKn0Lcyw1nd67prd7dC5gQWbAJa21kyFR747S7kZDNKwKk4r8cUJ1uTFuT3eJHcjAWRzDCBeAJeGB7vlq0i8ty1xy9alu0iWTYuS2%2BfrOvCpS1k7lCLtSXNa4umVVOUgSBweIj6Ihj3Fg3Ves2ohRtsbzP3NpoFz8xzQUjuzM%2B8VnTjvRliDWfote16z33H1Pe%2BAyrIZ%2BPartci7de%2BNBar9aj0OHUsN8SR4I%2FZjEkjo%2FCJtaGQ2kRk8mjOUMeev4HUXiMRi1zlx0vBosQFL6k9PcJ2urJoXHwgzNCGWLM78az6vsg6JhrgSuUsvLVC24ultfQXlubGJhH1Bl2f1PJhPR%2BTFnAGKwEKNU4sjTYnDOBxRya2Jf0ERptsuBWjhLaFXfe5Fng1RA%2B7ho%2FXhQP2E6dKXbLsmTZI6nkyULoFYBzNitFCYnfjaAcRC5b8amRRBpMQZnvccxmpyzFvOe4pOrWluL44mMaSYwafVH43LkT7nlln1DGu45Je1GRRuw4RrLZsWeGe1d0zyr6JDMnbl5W7zpTjdjgfbkZt0y6ZlYRGt6vx1%2BvuQbxfiMjzVfnTVfrxtVNxlxKm13G%2FG7y8OIJpOfWyNIXedfKVlM9p%2Bv7mPr1%2FckXpdVy7Dcj3CR4%2BkPofeLeN4MM3HEPf8B%2FIN7gfP7LYc6Y%2BvK5sRnP8Gtuv1E81jhvD2HHvtP7H77Qp9oZ9IryWHcT06P1AfoH9xikdev9dE%2F6pY7dd7BuP7qAPbXcDlNgpb3Pxv9O16XazrC4e2n4G%2Fcazpzj%2BU11mekizOv3Gs3sUkW%2FK5ZO07PY4iVWyOPKablaPs5rJYVeMX9suf9P615vflRL5r3cDp%2BV1Gbia0X%2FRlSu8WnXL2C6C%2BdNm%2F%2B1i%2BK%2FWVeThiu5lx24bfpw%2F%2FzXAXGI%2FjE03Ba80Q19yxiMczwwP4gMF%2Bea%2Fxcd%2FAA%3D%3D&RelayState=KYTwUgVgJgEg1gSwPILAaQGoEYCKCAyAwmADYBGAtgLLKoBCVEAqgEwBKADAHJcCSCAdwQBNAOoAPAHa8IAewQAtAOIkQvSRwB0mgLR0AghBISAbIQoIALABUAGmwBumkBQDKYAKIAzDB9FYdUQBmAFZ9AFcsAC8uVyiEAAsQABEMDAgvYEJksBNJAXCSJQBnEAxZFgRiy3EcMlFJOmKAY2EmLwAHEgETEA5LAH0AFx0OqjgKfQBOUWFkyw6EhS4WfQ8kChMOcKUWAEMEqcsQAA4vMFs0VwEBADEPJT2ABTISVw4YW73knR0BtnEmDcOCgLCo4Qoe3CACcqGQOjAcMUBmBiqI4AJXMJbq5krYvCcAOYQMhMXg4KLAVzWBJkrjhcJQVx7DjJJCuMggJgnGCSHQQawQQiyYT6BwDLgIKYUQgIKjAWTJdRBACOligXDQ-nCokI0K4OBOyX0XlukjQHUsbAehIoHRAQUIMGhMCmIAQdBArmACgG4gEOAGJzQaC4AiexUWej2AnElh01nEwg41jIDmalg8DmAFBV4johS8ZAN7hwdAokgSCTI1i4zSiFHSvDubCwaVs0KQHSGLAMGC8ISGXhgLCCMBOWBgAHZeEhbGAVXAgs1odCBjhBjswHQp1hwg5oSwkFM9oSvAI6AIHFBbBAEoQ0M0KAopgMpmhbAxgLxeAokDB3SgNgMAcUQFFEUQQHEaElC8ZoqCnLgOl4J4TBCIIBF7QlJBIKZXCeBYqEIUQTg8HASH0MA4D2FEOigMAmA4YRrAEWBblEDoohsKZkiiDAKCmQkpiUYB9CGKAGTIKYvDgQg2BVac6gSXgdCQFUKGKEw6FsJgIGAJgpjgDoKDgfQThALSPEJDAuNufRRDlLApLQZJZCYRQomqaw0EsZJwm9BJbg4fQFAEE5LBOIY2D0tAlCgYRbDgBQPCYZJrCiawVToNBZCgKIpnwZIPGsfQBBIZo2CiFhmhVLwoBILhoVuBIHDYIJvRgJ5RAoXgmC4EzJCJaF8BAEIpw8EBJFcLx9F%2BZpmjIJRCSnHQlGrOsPBOfA4HEJQMAGeMcBofQKrgJ5hA0ug6AGAYOluWxbA8SqWAcKIOlkCAuQccKsAo6wnWKHATCGNwyCgfQ0BIOgHCUKZJCefR8BCAQQj6p5xFcE4mFPDxhAUFU9n0EIdBVIIHEIARoR0ChZHCbdqQSfAPxCNhmqQLAIA4KAcB8phCCGAZ9EIfKojALg6BIHA4EsWGOGmhJmmKJAQgcAQsF%2BlgOASOsoGaDIXqmJ58DoDxNAgUQxY8LAVXCPM0RNqBWuhHDCX0IA&redir=true'

site6 = 'https://www.discovery.com/watch/discovery'

site7 = 'https://www.epix.com/series/deep-state/season/1/episode/1/old-habits?play=true'

site8 = 'http://www.mtv.com/episodes/y7pn7w/jersey-shore-family-vacation-meatball-training-day-season-1-ep-110'

site9 = 'https://www.foxsportsgo.com/channel/49070/fox-sports-1'

site10 = 'http://www.foxnews.com'

headers = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.2526.73 Safari/537.36'


ffProfile = webdriver.FirefoxProfile('/home/cday/.mozilla/firefox/kv4pspx2.cdayP')
driver = webdriver.Firefox(ffProfile)
#links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
driver.get(site8)
driver.implicitly_wait(100)
linky = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/video").get_attribute('src')
driver.execute_script('console.log("hello")')

driver.execute_script="document.getElementsByName()"
actualTag = driver.page_source
print("SOURCE: ", actualTag)
print("Length: ", len(linky))
print("Type: ", type(linky))                 
print(driver.current_url)
print("link: ", linky)

"""usrName = driver.find_element_by_name('username').send_keys('Mtooley@aol.com')
pWord = driver.find_element_by_name('password').send_keys('tur44tle')
clickLogin = driver.find_element_by_id('login').click()"""
#blob:http://www.mtv.com/c9f4700e-6f44-4822-88fb-ccab7373b3041212

print("Url: ", driver.current_url)
"""
driver.forward()
print("Status: ", driver.page_source)
print("Url: ", driver.current_url)
xFinityLogin = {'user': 'nctatech', 'passwd': 'TechLab!',}"""

"""//*[@id="primaryListWrapper"]/ul/li[5]/a"""






"""
python_button = driver.find_element_by_id('') #FHSU
python_button.click() #click fhsu link

soup_level1=BeautifulSoup(driver.page_source, 'html.parser')

"""





















"""datalist = []
x = 0 

#Beautiful Soup finds all Job Title links on the agency page and the loop begins
for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
    
    python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
    python_button.click()
    
    soup_level2=BeautifulSoup(driver.page_source, 'lxml')
    
    driver.execute_script("window.history.go(-1)") 

#end the Selenium browser session
driver.quit()

#get current working directory
path = os.getcwd()

#open, write, and close the file
f = open(path + "\\fhsu_payroll_data.json","w") #FHSU
f.write(json_records)
f.close()"""




"""
#storing the cookies generated by the browser
request_cookies_browser = driver.get_cookies()
#making a persistent connection using the requests library
params = {'IDToken1':'TamADAGZ', 'IDToken2':'TDMteam01'}
s = requests.Session()
#passing the cookies generated from the browser to the session
c = [s.cookies.set(c['name'], c['value']) for c in request_cookies_browser]
resp = s.post(site5, params) #I get a 200 status_code
#passing the cookie of the response to the browser
dict_resp_cookies = resp.cookies.get_dict()
response_cookies_browser = [{'name':name, 'value':value} for name, value in dict_resp_cookies.items()]
c = [driver.add_cookie(c) for c in response_cookies_browser]
print("CCCCC: ", c)
#the browser now contains the cookies generated from the authentication    
#driver.get(url)"""


"""links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
for url in links:
    if ("ns11.ns.twc") in url:
        print(url)
#browser.close()"""
