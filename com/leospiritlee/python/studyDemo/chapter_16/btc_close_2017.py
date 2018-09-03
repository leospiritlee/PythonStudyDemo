from __future__ import (absolute_import, division, print_function, unicode_literals)
from urllib.request import urlopen
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

response = urlopen(json_url)

req = response.read()

with open('btc_close_2017_urllib.json','wb') as f:
    f.write(req)

file_urllib = json.loads(req)
print(file_urllib)