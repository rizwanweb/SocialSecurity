from bs4 import BeautifulSoup
from lxml import etree
import requests

URL = "https://socialsecuritynumerology.com/prefixes.php"

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")
#dom = etree.HTML(str(soup))
#print(dom.xpath('//*[@id="text"]/p[3]')[0].text)

list = soup.find('div', id="text")

# Get all links

# for a in soup.find_all('a', href=True):
#     print(a['href'])

states = []

for item in soup.find_all('p'):

    if item.text[0].isdigit():
        #a = item.find_all('a')
        #for link in a:
        #    print(link['href'])
        line = item.text.split('\n')

        for l in line:
            areaNumber = l[:11]
            s = l[14:]
            states.append(f"{s} - {areaNumber}")
#states = set(states)
#print(len(states))
for s in states:
    print(s)

        

            