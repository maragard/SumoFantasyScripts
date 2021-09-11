import requests as req
import sys
from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer
from requests.exceptions import RequestException

def scrape_wrestler_data():
    data_url = "http://sumodb.sumogames.de/Banzuke.aspx?b=202109&heya=-1&shusshin=-1&w=on&spr=on&c=on"
    # Parse only tables with wrestler data
    onlytabl = SoupStrainer('table', class_='banzuke')

    resp = req.get(data_url)

    try:
        resp.raise_for_status()
    except RequestException as e:
        raise e
    else:
        soup = BS(resp.text, 'lxml', parse_only=onlytabl)
        #print(soup('table')[0].prettify())
        top_flight = soup('table')[0].find('tbody')('tr')
        print(top_flight)
        
        


if __name__ == '__main__':
    scrape_wrestler_data()
