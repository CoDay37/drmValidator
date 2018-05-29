#This file inputs a website list and formats it to be feed into a program

#Prompt
print('Website list must follow below format:')
print('- **website.domain**')

#File being written
outputFile = open('output/formatWebsiteList.txt','w+')
#Source file of websites
filepath = 'supportedsites.md'
#Opens file
with open(filepath) as websiteList:
        for line in websiteList:
                for i in range(len(line) - 1, -1, -1):
                        if((line[i] == '*') and (line[i-1] == '*')):
                         outputFile.write(line[5:i-1] + '\n')
        line = line[5:]
        outputFile.write(line)
outputFile.close()