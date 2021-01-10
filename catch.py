# Dependencies:
#   - beautifulsoup4
#   - requests

# Use the service of www.tunemymusic.com to import the song list shared from apple music
# This would print the results to the stdout as well as list.txt file.
from bs4 import BeautifulSoup
import requests

# url is the link of apple music list to be fetched
url = "your-apple-music-sharing-url"
r = requests.get(url)
soup = BeautifulSoup(r.text,features="html.parser")
parent = soup.find('div',class_="songs-list typography-caption")
i=1
with open('list.txt','w') as f:
    f.write("")

with open('list.txt','a',encoding='utf-8') as f:
    for row in parent.find_all("div",class_="row track web-preview song"):
        name = row.find("div",class_="song-name typography-label").contents[2]
        artist = row.find("div", class_="by-line typography-caption").span.a.contents[0]
        print(f'{artist} - {name}')
        f.write(f'{artist} - {name}\n')
