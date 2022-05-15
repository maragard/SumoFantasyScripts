import pandas as pd
import requests as req
import sys
from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer
from requests.exceptions import RequestException

def scrape_wrestler_data():
    # TODO: generalize the date to pull a variable date
    data_url = "http://sumodb.sumogames.de/Banzuke.aspx?b=202111&heya=-1&shusshin=-1&w=on&sps=on&spr=on&c=on"
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
        # cleaned_rows = [
            # {
              # 'Wrestler Rank': row('td')[0].string.encode('ascii', 'ignore').decode().strip(),
              # 'Rikishi': row('td')[1].string,
              # 'Height': ' '.join(row('td')[2].string.split(' ')[:2]),
              # 'Weight': ' '.join(row('td')[2].string.split(' ')[2:]),
              # 'Previous Rank': row('td')[3].string,
              # 'Prev. Tournament': row('td')[4].string.encode('ascii', 'ignore').decode().strip()
            # }
        # for row in top_flight]
        for row in top_flight:
            
            
            # data_template = {col: "" for col in ["Wrestler Rank", "Rikishi", "Height", "Weight", "Previous Rank", "Prev. Tournament"]}
            
        #print(cleaned_rows)
        prepped_data = pd.DataFrame(cleaned_rows)
        #print(prepped_data)

        prepped_data.to_csv("./roster.csv", index=False)


if __name__ == '__main__':
    scrape_wrestler_data()
