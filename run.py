#from pageParser import parse_videoHTML
from downloadTester import get_video_links, downloadVideo,formatOutput
from listFormater import format_List
from siteChecker import getInfo, getAllLinks

print("This Python program will take a list of websites in the format of: \n - **website.domain** ")
print("The program will take that list and search for all video sources on the website.")
print("In the output folder, there will be a list of websites with a true or false next to them to indicate if you can download videos from the website. ")
print("")

input = input("Enter a URL to be checked for video sources.")


(getInfo(input))

#format_List()