import webbrowser
import requests
import sys
import urllib3
import certifi
import time

count = 0
http = urllib3.PoolManager(ca_certs=certifi.where())
url = 'https://python.org/'
search_url = 'https://duckduckgo.com/'
target = 'python.org'
redirects = ['redirect-to?url=/','redirect_to?url=/']
my_dorks = [f'site:{target}',
            f'site:{target} inurl:%3Dhttp:github.com',
            f'site:{target} inurl:redir site:github.com',
            f'site:{target} inurl:%3D%2F:github.com',
            f'site:{target}/?n=%3Dhttp:github.com']
firefox_path = r"/usr/bin/firefox"
webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))

for redirect in redirects:
    resp = http.request('GET', url+redirect, redirect=True)
    #req = requests.get(url+payload)
    if redirect not in resp:
        print(redirect,resp.status)
        #print(resp.geturl())
        #print(resp.info())
    else:
        print('Mot redirect')

for dork in my_dorks:
    resp = http.request('GET', search_url + dork, redirect=True)
    #req = requests.get(url+payload)
    if dork not in resp:
        print(dork,resp.status)
        #print(resp.geturl())
        #print(resp.info())
    else:
        print('Mot redirect')
for dork in my_dorks:
    webbrowser.get('firefox').open(search_url + dork)
