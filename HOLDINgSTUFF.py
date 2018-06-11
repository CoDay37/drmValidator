#from pageParser
'''
lines = []
with open('output111.txt', 'rt') as in_file:
        for line in in_file:
                lines.append(line.rstrip('\n'))
        counter = (len(lines))
        holder = 0
        for element in range(0, counter):
                if(lines[holder].find('a') == -1):
                        print("No A is found")
                        lines.remove(lines[holder])
                        holder+=1
                print('holder: ', holder)
                print('counter: ', counter)
                print('Line of code', lines[holder])
                print(lines[holder].find('a'))
                holder+=1
                
                if(holder > counter):
                        break

       
#print(len(soup_string))
#for i in soup_string:
#        if soup_string[i] == "<" and soup_string[i+1] == "a":

#print(soup.find_alloutput1

#outputFile = open('output1
        ##Opens fileoutput1
        #with soup as websiteList:
                #for line in websiteList:
                        #for i in range(len(line) - 1, -1, -1):
                                #if((line[i] == '*') and (line[i-1] == '*')):
                                        #outputFile.write(line[5:i-1] + '\n')
                #line = line[5:]
                #outputFile.write(line)
        #outputFile.close()


#    header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
#    sb_get = requests.get("https://www.youtube.com", headers = header)
#    sb_get.content

 #   scrape_url="https://www.youtube.com"
###    search_url="/results?search_query="
#    search_hardcode = "game+of+thrones"
 #   website_url = scrape_url + search_url + search_hardcode
#    sb_get = requests.get(website_url, headers = header)
  #  sb_get.content

 #   soupeddata = BeautifulSoup(sb_get.content, "html.parser")
 #   yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
#
 #   for x in yt_links:
 #       yt_href = x.get("href")
 #       yt_title = x.get("title")
 #       yt_final = scrape_url + yt_href
 #       print(yt_title + '\n' + yt_final + '\n')


#page = requests.get("https://play.hbogo.com/")
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.find_all('div'))

#url = 'http://www.growingagreenerworld.com/episode125/'
#with requests.Session() as session:
        #session.headers = headers
        #response = session.get(url)
        #soup = BeautifulSoup(response.content)
        #follow the iframe url
        #response = session.get('http:' + soup.iframe['src'], headers={'Referer': url})
        #soup = BeautifulSoup(response.content)

    # extract the video URL from the script tag
 #  print re.search(r'"url":"(.*?)"', soup.script.text).group(1)
#print(soup.find_all('p'))
'''

"""def findLinks():
        halfParsed = []
        links = []
        lineNum = 1
        with open("websiteSource.txt", "r") as sc:
                lines = (line.rstrip() for line in sc)
                lines = (line for line in lines if line)            
                for line in enumerate(sc):
                        line = sc.readline()
                        if(line.isspace() == True):
                                continue
                        else:
                                halfParsed.append(line)
        for element in halfParsed:
               foundLinks = re.search(r"https?", element)
               if(foundLinks):
                       links.append(element)
        for element in links:
                urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', element)
                print("********", type(urls))
                #for x in urls
                goingIn = str(urls)
                htmlChecked.add(goingIn)
                print(goingIn)"""