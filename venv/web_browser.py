import webbrowser

# then make a url variable
url = "https://www.geeksforgeeks.org"

# getting path
chrome_path = r"/usr/bin/firefox"

# First registers the new browser
webbrowser.register('firefox', None,
                    webbrowser.BackgroundBrowser(chrome_path))

# after registering we can open it by getting its code.
webbrowser.get('firefox').open(url)