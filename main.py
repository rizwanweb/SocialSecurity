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

ll = []

for item in soup.find_all('p'):

    if item.text[0].isdigit():
        line = item.text.split('\n')

        for l in line:
            state = l[14:]
            print(state)
    

    # if item.text[0].isdigit():
    #     link = item.find_all('a')
    #     print(link)

        

            