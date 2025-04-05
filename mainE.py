import time
import requests
from send_email import email1

import selectorlib # this library is used to extract data from a website

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


def send_email():
    print("Email was sent")

# Create a file, write and append 
def store(extracted):
    with open("data.txt", 'a') as file:
        file.write(extracted + '\n')

def read():
    with open("data.txt", 'r') as file:
        return file.read() 

def subject():
    con = 'Subject: Todays Event'
    return con

if __name__ == '__main__':
    while True:
        scrapped = scrape(URL)
        extracted = extract(scrapped)
        print(extracted)

        content = read()
        
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                subject_email = subject()
                message='Hey, new event was found!'
                join = f'{subject_email} "\n" {message}'
                email1(join)
            time.sleep(2)

    # you can run it constantly using a while loop but you  will have to keep your computer on always which is not okay for an organisation, or 
    # you can pay for a plan on the server on python how to keep running it for you , so the server keeps executing it

