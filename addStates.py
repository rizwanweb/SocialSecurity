from bs4 import BeautifulSoup

import requests
import sqlite3

URL = "https://socialsecuritynumerology.com/prefixes.php/"

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")
list = soup.find('div', id="text")




def Crud(conn, name, areaNumber):
    try:
        cursor = conn.cursor()
        query = """
                    INSERT INTO States (Name, AreaNumber)
                    VALUES
                    (?,?);
                """
        data = (name, areaNumber)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
    except sqlite3.Error as e:
        print("Failed to insert data", e)



for item in soup.find_all('p'):

    if item.text[0].isdigit():
        #a = item.find_all('a')
        #for link in a:
        #    print(link['href'])
        line = item.text.split('\n')

        
        try:
            conn = sqlite3.connect('data.db')
            if conn:
                print("Successfully Connected to Database")
            else:
                print("Failed to connect")
            for l in line:
                areaNumber = l[:11]
                s = l[14:]
                Crud(conn, s, areaNumber)
        except sqlite3.Error as e:
            print("Failed to insert data", e)
        finally:
            if conn:
                conn.close()
                print("Database Connection closed")
            # states.append(f"{s} - {areaNumber}")
#states = set(states)
#print(len(states))
# for s in states:
#     print(s)

        

            