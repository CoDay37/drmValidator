#pip install lxml
#pip install requests
from bs4 import BeautifulSoup, SoupStrainer
import urllib3
import requests
import os
import re
import random
from requests.exceptions import MissingSchema

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
payload = {'key': 'value1', 'key2': 'value2'}
#path = os.getcwd()
unCheckedLinks = set()
parseHTML = set()
videoLinks = set()
randomLinks = set()
holdLinks = set()
placeHolder = set()
htmlLinks = 0
totalL = 0
post = False
base_URL = 'https://www.nbc.com'


payload = {#For Xfinity
    'user': 'nctatech',
    'passwd': 'TechLab!',
    'continue':'https://oauth.xfinity.com/oauth/authorize?response_type=code&redirect_uri=https://sp.auth.adobe.com/adobe-services/oauth2&state=CBxKlW&scope=openid%20profile%20https://login.comcast.net/pdp/tve&client_id=adobepass-hgtv&acr_values=urn:oasis:names:tc:SAML:2.0:ac:classes:InternetProtocol&response=1',
    'reqId':'1c24418a-4364-4eeb-a939-5d75dcd8787c'
}
payload2 = {#CHARTER
    'IDToken1':'Men254@charter.net',#emal
    'IDToken2':'Adam1041',#password
    'gotoOnFail':'',
    'goto':'L1NTT1BPU1QvbWV0YUFsaWFzL2NoYXJ0ZXIvaWRwP1JlcUlEPWE0MDk1MDM3aWZqMzFhODEzMmg5YWdkaDM1YWUyNGc=',
    'SunQueryParamsString':'cmVkaXI9dHJ1ZSZyZWFsbT0vY2hhcnRlciZmb3J3YXJkPXRydWUmU0FNTFJlcXVlc3Q9blZoSmw2cklFdDc3SytyWVMwOFZnNmpvdVZWOWtoa1ZCWm5FSFVNS0tKTU1Jdno2aDFybDg5NWJyMTkzTDF4a0VQSEZuQm5oano4dmNmUnlobmtScHNsN0gzdEQreTh3Y1ZNdlRQejN2cTV4cjJUL3o0L2VqOEtPSXp5Ymdhb01rZzA4VmJBb1gwQlJ3THpzNU9nMEthb1k1aXJNejZFTDljM3l2UitVWlZiTUVLVEkzdXhPNk0zMlVnZSt1V25jVVpBckdxSUNhZmtiUlArRjZhRER4QzV2OW55aGhGNEhVeGR2Ym1EbkpjemZFbGpPQ0dLSXBCbE03QmhSMWJXOFZqVWtocVVOb3RBdWtFL0dxMkQvaFV0ekY5NU1mKytYZVFYN0x5THozcmNKZERwQ2g1TndmeGhpTm9rTjhXQnErMTR3SE5rUUoveU9xWkR0b2dqUDhMMi90NlBpS2xZVUZSU1RvclNUOHIyUG94ajVpbzVmY1Z6RGhyUGhaRWFNM3NnSnV1dS95SGxhcG00YVVXRnlEMlNWSjdQVUxzSmkxcGtMaTFucHpxN3V6L0EzZE9iY21ZcVpvR255NjlXUC9vdnhsUkQ4bXBBdVJVa3h1NmZncjdHeVQ4WDlqM3ZHWmplTDgyZUV2d2F3dnhMUy8zaGtzSk42K3kyTlA1Qm5CUjgvdkdLbWhuNlh0eXFIbitxODRwN0FEcU91NjdkNitKYm1Qb0tqS0lxZ1U2VGo4WXJRLzZQL2tJV2VtT3pUMjVHMmt6UUpYVHNLMjFzbFNMQU1VdThGUkg2YWgyVVEvdzlnRE1IUUsvQXJ2TGl2TGtZa2YvU1JuMDM3bTBBL1daZ1g5bXNSMk5nbjFnYnVZZDcxQ0h6Uk4rSjcvNC8vVjBjM0lTMjNrMktmNW5IeDgvR2ZXUUtUTTR5Nm12ZGVpeStIUG8zNis0RGZ4d2o1M1VZbTlMdFcvRGNCZXdyV0hjU3dvd3ArcExzQ1Z6WGJQNFlOVFN6UnM2QTZHWWpWek5lazk1c0J6OHczd2lQVTkrTXZSZkpJNmwwQ0J1ZUJaL0Q3U3FhYll6aW5SM21tZ1dpMEVOVExoU0QxYUlwZGpvY1Ntd3RXT01mR2dyRTM5QTFXYjBhSXdNbEpHWHFzRDlKTHlwcGlRTFpPSlhPZVZDY3N1NE9LdUFkSU81cXNkM3ZXTEhiR0laZEdlRlVJSlIrUlVpazMyMUtXZ1ZLb1I0V1A1aFJKQTJITnlqdFR2TXhSalc5YzQ3Q1ZocXN5RU5iTFNWcWw1SkxmalhiZGJlY3N6dUZaazczV0dlekU5bERIWGpKV2FzWWNHUkVaUkZFd0xVTnRmTmF3cWlrdWxIa3NwNTRvMWRKNFdjQ3BOc0loVnB3T2FGUU5oNkZqWlZpTkdEN21taFRIQUg4eUlzbFZNVWl5clFUbkMzWGhiekRicEpzaHNaNm5ZYUNwTG1kN3lRVTRER2tmUlMrRHRlN2hHZFl5U1RPZzdmZzhEbU9mUXViSk5xSDJnek40ZjMrRS9pblcxL0F2WVBOSXhYYUVUaG03dEI4SCtucUw3THNPTHVHSEpJb2MwOUkwUUtBUGFwRUN2cWpJNjlPRlY4ZWJPWmR1aExqaWVKU29FQTJzS1A5NENvNGhQNjFScWdzcUJ4aHFJQ2xGVFNzV1l5Z0szMlBydWFHM3JDZFJCUTh3bmFVRFNkZUhVV21aSTNSblNyNkNUeHVYbnpiV2RwTTVPSEVSV3VCUi9zcWdRS0Z4MFdya21Gemw4Y1pCNURaTno5dXVVSkVkUlo3Z25kMjR1Q3hiVU42WkpXMyt6TXl1Q211N2FrVkc4blhjT0hqYmVTUnlxOGhOZHBFYlVveWlnckluc2k0cVVjU1cwVmhNWXR4bTFZSmFZcm9mbDE1cHhKMG10aXZ0aUsyTnRQWjN4d3ZkZ3ZsZG9kWFZxcUZKRzZsbU8xZDduYThpQXpMR01pL1pMcDQyVGh3RjBvYXRtZm9XQjRFQmdXYVpoSy9HMDNhbnNRZUpadS9oOEd0Yk1UZG5LOWI5TGl4dFozM1pjeHRxN3NTcnM1dFFuWnRjRnlmbDBpSFluM0dSV0l4cWJCT0xQRDRxZDUwcklrY0Y3bER5RGM1NmlwOGtjY2txNkRsbVhibERVRmxiQTdYcFViRGpwK0ZPSFIwY0hLMTludzBsZ1BLMGV1SlYwUmt5Q3R0bFVRZUFFQ21tQnRmdkM1QjJGYUF3L0s0UTg5N0M4cnUrdE1LeWdvby8wVGRuUWJpc3F3b0dwNjJ3d0JDRkRKQjBjRUtFb1JzdkhMK2VsakprWmQ2aWc3MGxtTEpKY25rQkhPSk16bjFxMFJQM08xMnc1alRjREp5alNUWVhlVHB5eVlCMG1md0M5OEZ4VHlOZ0gxMWsxOXBQMm1hK0pIbTVqY24xWGs4OGhOTFg0Y2JRMS95aW5sUU8yZlFHVktienlmQThyM2lqR3FBMEUzR2wzM1JKbWJRMllhOU5mYzg1U0NKMy9SdEgwNVdLbndRMnZBd3JFbGpMQWNjUTQvRmhEQ1JCZHpWaFpQV3c0Z3dTVTl1WmMvd0FzV09XRVU3Rnk1TUR3cFlES2RCejJpTWhNUm1xT0t3em50dFhTODdHU0QwZktuNXo0YzhTc3l4UHFSZVB0ZTJtb1hxbjhWVGhVVS9IK1pWNnFLdnpEZ1UxaDI5R0Vvdld5M0RxQUYraUFPQVB2cy9sWGV0UnV4WUUxd3dLRzVibEQ4RHlnMTFybVZpeFRGWjFieGx6bU1mN2xYV3ZtY3JDcDZVRWp0ZGE4dGhhb1NVQWFzYnZhbTZEZHBlY2dGeFRCM3l6VTRIZWVPYUtZa3FVd3ROMHdmZTZWSE5VTFZHVTcrZVV6M0tVNGpMZ1FOMjFxNEExRDVRbGNSWlB4WkJpQUV0MzN5U0psbTdDZDFtUjRnSXY5WVJOM1hQYjlMekVsYTdXdXViR3hadGxTM3hWdXkySW5oUjBJR0RIZndwOUt6T2MxNzJ1dS9aM0t5U1daNERwVTV1OUpVMkRJN2ZkQjZ5a2h6RTRGV2RqUEdVbGE5S0MvQjR2a3AweklKUm8yaGRPd0EyQzdHN1pPaVRQWFh2OG9tWFZMdU5WNHpEVTlzbTZMbHlicGNRZWE2RzJ4RVZ0VVpTaUN4TGdlUllQVUU4QTQ5NnltYlp1TTJxaGlSMTI5TDJONXY0ejg0TG40enZ6TTY4VjNuaHZobGpET1hwdHU5NXozOUgxdmUrQUF2TDV1TjdWaGtCNXRTZU9oY29ZbFM2cmpLV0d5QWd1UytkMEVtcUZSeGlhVEc0bUFwMkhDM3FhOVR3VFRnOGJFckhJZFo1ZENnWWxMbmc1UFZBamJLL0t5OGJCQi93Y2JRaUQyUXRueGZNRXh0WlJINWNyZStrYU1yVmJycXlWdDdRMlRxUVRZVy9ROVVrdEhZM0ZtTFNBUFZqemtLOXhZcVcxT2FFQmw4M29hQ2VxSnpBeTArRldDR05xeCsrNzY1cm5sQUE5N2hzdU1nb2JIQ1oybFRoazJkTjNJSzRYOFVEdVZvQnhPQzlHUzVIWmo4TTlSQ3hZY3V1Uk5kWG9tTkRiN01DbXBDcEZuR1U3cC9EVWxvSnhzYkVOUTQ1cGZGSjVtMHdORHoyOVRxZFpWRWNsdGF6Sm9uWnN3bDl2bWJMQ1hhdDdaK1JERTJxaWV5Z3J4MGpsYkR0Y0RNMVIyN1FyZWkyaTRlMXAvUFc1ZXhEdkR5THkvRlQrOUpSK2ZHMVY3S1dFeVhYZTd3WXZOd3BoVXM3Y05FbWdleDE5UmZsem5MNS91WS92bjF4aGNoM1hiaFB5ZllTSEQ2VCtCNDVPMy9EaEc0NmhiL2dQNUJ2Y2p4OXA1Tm96RDE2WE5xM0p2dWIySy9WVGplMUVNTEtkTzYzLzhUdHRocjFobndpdlpRY3h5OXdmeUMrdzN6aWxRdmUvZThJL2RleTJqSDNqMFIzMG9lMXVnQnpaNVcwdS9uZTZsbUZTWFI2NmZvYjh4cStuS1A1VFRYcHlUTkk2K2NhdmV3eVJiNHJsazdUcTFqaVJrZE1vZEp0dVVvL1NtczVoVjRwZjJ5NTMwL3JYaTkrVkVucXZkd05uNVhVVnVKclJmMUhsSzd4U2RidllQb1Q1MDJiLzdWNzRyN1pWNU9HSzZxWlp0d3cvenAvL05jQmNaRDRrelhoRTRabitJRDZFa1cvK3J2ajREdz09JlJlbGF5U3RhdGU9S1lUd1VnVmdKZ0VnMWdTd1BJTEFhUUdvRVlDS0NBeUF3bUFEWUJHQXRnTExLb0JDVkVBcWdFd0JLQURBSEpjQ1NDQWR3UUJOQU9vQVBBSGE4SUFld1FBdEFPSWtRdlNSd0IwbWdJSWtBRmtvQWNBRVNXU0Erb1Y0d0E1a2docE5GaUFHWUFoaUFBdUFOeVVBdllSZ0FOaE1LSDFjQVp5OFdZUzgwQ0E0dldRb0FCd0JqWGlRa0FCWmVBRmNRT2dCV0ppbzRkMkZnVVRKOGdGRlhPaGdkQUEwYzJRc1RBQ2NkT2hOZ2dYeDhpMVNZR0RCSTRJd0FGUUFGQUZvT1lDN0pPb28yZlE0U0V6QTJYbnd1MUxBTUh6cGtIUUVBTXhJQVpVakw0cHppakdDQU1TNUpLSG0wV1M0Nm5Va0xRd0FFNWVQb0xHQXZDQWZOTjBGd0FJNENHSFRVVEZBRHNFRm13Q1VTbG1NRXVrblNhSGhzalJSbUJYUndPVmVVRjRMVXVDbHMrVkVraFk4Tm1TRm0rREFhMktIRm1ZRkUraVEtVmVvalErakFJRVNISkF3RmhYaXdYRmsrVGdGQ2dIRWtJRkJYbHNyeHcwell3UXM0aklyM20xem9TZ1UrRnNSbUtWT0VPRXV3aVFjQzZGR0JkQkFYQXN4WG1KZ1VoSDhKaVF2Rm13VWtraDAtbndybm04elJZSDZKQjBPUW9MQVUwMzBQblNVQllYVEk4M2tKa2tvaTRkRnNhQmcrRlNOTHFDaU1VRmNPbFNMRlNMWHdDSEJyMTRKSDhFWnlYaU1WRmNOMzhDRWtoQ2dMV0JOeGEwMUF0bW13SzhIQVVaRkVZQTRXRG9GaHdWQmErZ0VybE1TaTRMRFh3SGgyQ2dEWTRFR3BKQTRKZ2VVRFFhSjArQ1lVQ29hQW9seWlDMDhMdUZ5a1FRT1lEVEZLa3JoUUdBNlQrSVE4S3ZHTWtTek1xdGh3Tk1GaE1ENENnZ1BxWGpBZ0lxU2RKRVRCWUJncmdnR3c3aFVGZ2xGMUhBY0NCSmNhRDRPNDFHekRvdkJRTUFWQ3pQRWJDcFBNRUNYREFHWktDQUlBVUs4MGFSQmdMQm9HQXhUK0dBc3lTSzh3anBGZytBc05NTFJvRW9PVDRFZytqQkRvT0RBaFFhQ1hEY2hENk1Vc3lrcTZraG9nb3JpdkN3UkkrR1FIQm9Dd0hBc0FHSUF0S0lMQXdPNFBpcFBDT0NlUlFrajBXQVNqaU1BaENYRndTanpBb1hBUURnZFJVQUlmSENOTVdCTUFnZFNwTUlYQ1hPa2FJSUJBOEpvRUtMUStQQ056aUpjWkRCR3dFQW1GQXhURks4SkR3RXc4SVVEb1dEVEY0RmhJRnBqNjhDQXBpeFN3T0F3RUsrZzNHaUxRM0RrcFljQzBaQ3BCd0pLdWtZaER6RG9WRG1jSWFCZEpFMHhHQ3dEWDVLa0pEaUZRa2hZR1FMVCtBb09nTW1RdkNhQzBKZ21FWUNDSG1BT0M4RlEzNEtCWTB6Q0IxcmhrQUlRQSZzcEVudGl0eUlEPWh0dHBzOi8vc2FtbC5zcC5hdXRoLmFkb2JlLmNvbQ==',
    'encoded':'true',
    'requestorID':'mtv',
    'referer':'null',
    'gx_charset':'UTF-8'
}


def getVideoSource(videoSet):
        vidSet = videoSet.copy()
        lent = (len(vidSet))
        for n in vidSet:
                print("Remaining: ", lent)
                lent-=1
                rq = requests.get(n, headers={'User-Agent': USER_AGENT})       
                data =rq.content
                souppy = BeautifulSoup(data, 'html.parser')
                souppy.pretiffy
        for ele in souppy.find_all('iframe', src=True):
                print("**",ele)
                if 'player.theplatform.com' in ele:
                        print("Found Source")
                        videoLinks.add(ele)


def findLinks(link):
        with requests.Session() as s:
                global post
                if post:
                        r = s.post(link, data=payload)
                        post = False
                elif not post:
                        r = requests.get(link, headers={'User-Agent': USER_AGENT})
                data = r.content
                soup = BeautifulSoup(data,'html.parser')
                soup.prettify
                global totalL
                totalL+=1
                #print("Total Number of Links Parsed: ", totalL)
                print("Status:", r.status_code)
                print("# of vid", len(videoLinks))
                for link in soup.findAll("a"):
                        sLink = link.get('href')
                        if(sLink == ''):
                                continue
                        elif (sLink is None):
                                continue
                        elif (sLink[0] == '/'):
                                combinedLink = (base_URL+sLink)
                                unCheckedLinks.add(combinedLink)
                        elif (base_URL not in sLink):
                                continue
                        elif (('https' in sLink) or ('http' in sLink)):
                                unCheckedLinks.add(sLink)                     
                        else:
                                continue

                for element in unCheckedLinks:
                        if '/video/' in element:
                                parseHTML.add(element)
                        
                unCheckedLinks.clear()
        """for element in unCheckedLinks:
                        holding = str(element)
                        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', holding)
                        link = str(url)
                        if not "http" in link or not "https" in link:
                                continue
                        else:
                                holdLinks.add(link)"""
                #TO_DO TOMORROW
                #ENSURE THAT PARSER STAYS ON WEBSITE


def linkChecker():
        for element in holdLinks:
                if 'player.theplatform.com' in element:
                        print("Found Source")
                        videoLinks.add(element)
                elif base_URL in element:
                        parseHTML.add(element)
                elif 'ico' in element or 'png' in element or 'jpg' in element or "woff2" in element or 'css' in element or 'js' in element or "xml" in element:
                        randomLinks.add(element)
                        print("Randomlink")
                elif '.mp4' in element or '.mpeg' in element or '.wmv' in element or '.mov' in element:
                        videoLinks.add(element)
                        print("Video Link")
                elif 'twitter' in element or 'facebook' in element or 'google.com' in element or 'instagram.com' in element:
                        print("radnom sht")
                        continue
                elif 'cbs' not in element:
                        continue
                else:
                        parseHTML.add(element)
        holdLinks.clear()

def controller(url):
        findLinks(url)
        holdSet = parseHTML.copy()
        for link in holdSet:
                findLinks(link)
        getVideoSource(parseHTML)
        print("CHECK", len(videoLinks))
        for element in videoLinks:
                print(element)


