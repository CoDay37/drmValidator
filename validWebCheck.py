#This file will check if a website is valid or not
import http.client



filepath = 'output/formatWebsiteList.txt'
holder = ""
with open(filepath) as websiteList:
    for line in websiteList:
        if not line.strip():
            continue
        else:
            holder = line
            holder +=".com"
            holder.replace(" ","")
            print("TOGETHER = " + holder)







#checker = http.client.HTTPConnection(line)


#filepath = 'supportedsites.md'
#Opens file
#with open(filepath) as websiteList:
 #       for line in websiteList:
 #               for i in range(len(line) - 1, -1, -1):
 #                       if((line[i] == '*') and (line[i-1] == '*')):
 #                        outputFile.write(line[5:i-1] + '\n')
 #       line = line[5:]
 #       outputFile.write(line + '\n')
#outputFile.close()