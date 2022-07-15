from bs4 import BeautifulSoup
import urllib.request
import re
#import pyperclip

k = []
try:
   with urllib.request.urlopen('https://duckduckgo.com/site:python.org') as f:
      s = f.read().decode('utf-8')
      d = s.split()

except urllib.error.URLError as e:
   print(e.reason)

print(d)
req = 'https'
for word in d:
   if req in word:
      k.append(word)
print(k)