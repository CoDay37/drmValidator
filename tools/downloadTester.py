import requests 
from bs4 import BeautifulSoup

input_link = "http://www-personal.umich.edu/~csev/books/py4inf/media/"
header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}

def get_video_links(link): 
    # create response object
    r = requests.get(input_link)
    # create beautiful-soup object
    soup = BeautifulSoup(r.content,'html5lib')
    # find all links on web-page
    links = soup.findAll('a')
    # filter the link sending with .mp4
    video_links = [input_link + link['href'] for link in links if link['href'].endswith('mp4')]
    return video_links

def downloadVideo(link):
    url_get = requests.get(link, header)
    soupData = BeautifulSoup(url_get.content,'html.parser')
    videoLinks = soupData.find_all("a")
    for x in videoLinks:
        href = x.get("href")
        title = x.get("title")
    print("Link: " + link + "\n")
    print(title)
    #print("Title: " + title + "\n")

    #links = soup.findAll("a")
    #video_links = [link + link['href'] for link in links if link['href'].endswith('mp4')]
    print(videoLinks)
    #print(r.content)

def download_videos(video_links):
     for link in video_links:
        # obtain filename by splitting url and getting 
        # last string
        file_name = link.split('/')[-1]   
        print ("Downloading file: " +file_name)
        # create response object
        r = requests.get(link, stream = True)
        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
        print ("%s downloaded!\n" + file_name)
        print ("All videos downloaded!")
        return

def formatOutput(videoList):
    for line in videoList:
        holder = videoList
        holder.replace("</a>", "/n")