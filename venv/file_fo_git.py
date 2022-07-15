import requests
import sys
import urllib3
import certifi

http = urllib3.PoolManager(ca_certs=certifi.where())
url = 'https://httpbin.org/'
payloads = ['redirect-to?url=/','redirect_to?url=/']
for payload in payloads:
    resp = http.request('GET', url+payload, redirect=True)
    #req = requests.get(url+payload)
    if payload not in resp:
        print(payload,resp.status)
        #print(resp.geturl())
        #print(resp.info())
    else:
        print('Mot redirect')