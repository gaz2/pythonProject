import webbrowser

# then make a url variable
url = "https://duckduckgo.com/site:hrenvam.net/@google.com" # "inurl:%3Dhttp:github.com"

# getting path
firefox_path = r"/usr/bin/firefox"

# First registers the new browser
webbrowser.register('firefox', None,
                    webbrowser.BackgroundBrowser(firefox_path))

# after registering we can open it by getting its code.
webbrowser.get('firefox').open(url)