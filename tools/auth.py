from requests import Request, Session
from bs4 import BeautifulSoup, SoupStrainer
import requests

url = 'https://login.xfinity.com/login?r=comcast.net&s=oauth&continue=https%3A%2F%2Foauth.xfinity.com%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2Fsp.auth.adobe.com%2Fadobe-services%2Foauth2%26state%3DkP5Bzd%26scope%3Dopenid%2520profile%2520https%3A%2F%2Flogin.comcast.net%2Fpdp%2Ftve%26client_id%3Dadobepass-espn%26acr_values%3Durn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Aac%3Aclasses%3AInternetProtocol%26response%3D1&ipAddrAuthn=1&client_id=adobepass-espn&reqId=3620d577-2996-458f-a31a-ea88c5858118'
url2 = 'https://www.espn.com/watch/?id=3345739'

#req = Request('POST', url, data=data, headers=headers)
#prepped = req.prepare_request()

payload = {
    'user': 'nctatech',
    'passwd': 'TechLab!'
}
with requests.Session() as s:
    p = s.post(url2,data=payload)
    data = p.content
    soup = BeautifulSoup(data,'html.parser')
    soup.prettify
    print(soup)
