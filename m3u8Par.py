import re
from urllib.parse import urljoin
import validators
import requests
from requests.exceptions import ConnectionError, ReadTimeout, TooManyRedirects, ChunkedEncodingError

m3u_regex = r'(\.m3u8?)|(&?type=m3u8?)'
whitespace = r'^\s*$'
streams = set()

def parse_m3u(url):
   print('Parsing %s' % url)
   try:
       request = requests.get(url)
   except (ConnectionError, ReadTimeout, TooManyRedirects, ChunkedEncodingError):
       print('Cannot make a request to %s' % url)
   else:
       splitext = request.text.split('\n')
       splitext = list(filter(lambda x: not re.match(whitespace, x), splitext))
       splitext_iter = iter(splitext)
       if splitext_iter:
           curr = next(splitext_iter).strip()
           try:
               while True:
                   ext_above = False
                   while re.search(r'#EXT', curr):
                       curr = next(splitext_iter).strip()
                       ext_above = True
                   if ext_above and not validators.url(curr):
                       curr = urljoin(url, curr)
                   if ext_above and re.search(m3u_regex, curr):
                       parse_m3u(curr)
                   elif ext_above:
                       print('Adding %s to streams' % curr)
                       streams.add(curr)
                   curr = next(splitext_iter).strip()
           except StopIteration:
               pass

