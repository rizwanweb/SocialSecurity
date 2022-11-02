from bs4 import BeautifulSoup
import requests
import sqlite3


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

# SELECT QUERY
def SelectFromDatabase(conn):
    try:
        cursor = conn.cursor()
        query = """
                    SELECT StateID, AreaNumber FROM States;
                """
        
        cursor.execute(query)
        records = cursor.fetchall()
        conn.commit()
        cursor.close()
        return records
    except sqlite3.Error as e:
        print("Failed to read data", e)

# INSERT QUERY FOR GROUPS
def InsertToGroups(conn, ID, groupNumber):
    try:
        cursor = conn.cursor()
        query = """
                    INSERT INTO Groups (StateID, GroupNumber)
                    VALUES
                    (?,?);
                """
        data = (ID, groupNumber)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
    except sqlite3.Error as e:
        print("Failed to insert data", e)

# INSERT QUERY FOR SSN
def InsertToSSNumbers(conn, SSNumber, StateID):
    try:
        cursor = conn.cursor()
        query = """
                    INSERT INTO SSNumbers (SSNumber, StateID)
                    VALUES
                    (?,?);
                """
        data = (StateID, SSNumber)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
    except sqlite3.Error as e:
        print("Failed to insert data", e)

try:
    conn = sqlite3.connect('data.db')
    if conn:
        print("Successfully Connected to Database")
        records = SelectFromDatabase(conn)
    else:
        print("Failed to connect")

except sqlite3.Error as e:
    print("Failed to insert data", e)
finally:
    if conn:
        conn.close()
        print("Database Connection closed")


for row in records:
    StateID = row[0]
    areaNumber = row[1]
    prefix = areaNumber[0:3]
    #print(f"{ID}---{prefix}")
    URL = f"https://socialsecuritynumerology.com/prefixes.php/{prefix}"
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")

    try:
        conn = sqlite3.connect('data copy.db')
        if conn:
            print("Successfully Connected to Database")
            try:
                for item in soup.find_all('p'):
                    a = item.find_all('a')
                    for link in a:
                        if link.text[0].isdigit():            
                            groupNumber = link.text
                            #InsertToGroups(conn, StateID, groupNumber)
                            print(f"{groupNumber} inserted to Group Table")
                            group_prefix = link['href']
                            #print(group_prefix)
                            grp_url = f"https://socialsecuritynumerology.com{group_prefix}"
                            page = requests.get(grp_url, headers=HEADERS)
                            soup1 = BeautifulSoup(page.content, "html.parser")

                            for i in soup1.find_all('p'):
                                a = i.find_all('a')
                                for li in a:
                                    if li.text[0].isdigit() and '-' in li.text:
                                        #print(li.text)
                                        SSNumber = li.text
                                        #InsertToSSNumbers(conn, StateID, SSNumber)
                                        print(f"{SSNumber} inserted to Social Security Table")

            except sqlite3.Error as e:
                print("Failed to insert data", e)
        else:
            print("Failed to connect")
    finally:
        if conn:
            conn.close()
            print("Database Connection closed")