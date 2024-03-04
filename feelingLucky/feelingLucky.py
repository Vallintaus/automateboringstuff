import requests, sys, webbrowser, bs4

print("Googling...")
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result link
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open browser tab for each result
linkElems = soup.select('div#main > div > div > div > a')
numOpen = min(2, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))