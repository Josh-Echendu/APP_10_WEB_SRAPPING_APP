import time
import requests
from send_email import email1
import selectorlib # this library is used to extract data from a website
import sqlite3

# Establish a connection object instance
connection = sqlite3.connect("data.db")

# We want to extract data from this url
URL = 'https://programmer100.pythonanywhere.com/tours/'

# THIS header tells the webserver that the script is actually a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')

    # This returns a dictionary which has a key called 'tours'
    value = extractor.extract(source)['tours']
    return value

def store(extracted):
    row = extracted.split(",")
    print(row)

    # Stripping the spaces in each item
    row = [item.strip() for item in row]
    print(row)

    # Establish a cursor object
    cursor = connection.cursor()

    # INSERT new rows
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()

def read(extracted):
    row = extracted.split(",")
    print(row)

    # Stripping the spaces in each item
    row = [item.strip() for item in row]
    print(row)
    band, city, date = row

    # Establish a cursor object
    cursor = connection.cursor()

    # Query certain columns based on conditions
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date)) # i can use to row column which is a list or the, 'band, city, date' column
    rows = cursor.fetchall() # This returns a list with the 'execute()' method, but returns a list of tuples when you use the 'executemany()' method
    print(rows)
    return rows

def subject():
    con = 'Subject: Todays Event'
    return con

if __name__ == '__main__':
    while True:
        scrapped = scrape(URL)
        extracted = extract(scrapped)
        print(extracted)
        
        if extracted != "No upcoming tours":
            rows = read(extracted) # This is a list
            print(type(rows))
            if not rows:
                store(extracted)

                # Created an email subject
                subject_email = subject()
                message='Hey, new event was found!'
                join = f'{subject_email} "\n" {message}'
                email1(join)
            time.sleep(2)

#>>> row = ['feng suave', 'minimalia city', '5.5.2089']
#>>> band, city, date = row                                                           key', 'Monkey city', '2088.10.15'), ('Cats', 'Cat city', '2088.10.17'), ('Hens', 'Hen city', '208
#>>> band
#'feng suave'
#>>> city
#'minimalia city'
#>>> date
#'5.5.2089'
    

