import requests
from bs4 import BeautifulSoup
import logging
import argparse
from urllib.parse import quote
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')

# create the arguments
my_parser = argparse.ArgumentParser(description='Yellow Pages Scraper', 
                                    epilog='Enjoy the program! :)',
                                    allow_abbrev=False)

my_parser.add_argument('-q',
                        '--query',
                        action='store', 
                        type=str, 
                        nargs=1,
                        required=True,
                        help='the search text (Example : Coffee Shops)')

my_parser.add_argument('-g',
                        '--geo',
                        action='store', 
                        type=str, 
                        nargs=1,
                        required=True,
                        help='the Geolocation (Example : Chicago)')

my_parser.add_argument('-l',
                        '--limit',
                        action='store', 
                        type=int, 
                        nargs=1,
                        required=True,
                        help='the max scraped places (zero to extract all)')

my_parser.add_argument('-f',
                        '--file',
                        action='store', 
                        type=str, 
                        nargs=1,
                        required=True,
                        help='file to store data (Example: output.csv)')



args = my_parser.parse_args()

query = args.query[0]
geo = args.geo[0]
limit = args.limit[0]
file = args.file[0]



# start scraping
logging.info('start searching places ...')
query = quote(query)
geo = quote(geo)
page = 0 
data = []
while True:
    url = "https://www.yellowpages.com/search?search_terms="+str(query)+"&geo_location_terms="+str(geo)+"&page="+str(page)+""
    response = requests.get(url)
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text,"lxml")
    results = soup.find('div',attrs={'class':'scrollable-pane'}).find_all('div',attrs={'class':'result'})
    for result in results:
        try:
            name = result.find('h2',attrs={'class':'n'}).find('a').get_text()
        except:
            name = None

        try:
            phone = result.find('div',attrs={'class':'phone'}).get_text()
        except:
            phone = None

        adresse = ""
        try:
            street = result.find('div',attrs={'class':'street-address'}).get_text()
            adresse = adresse + street
        except:
            street = None
        try:
            locality = result.find('div',attrs={'class':'locality'}).get_text()
            adresse = adresse + ' ' + locality
        except:
            locality = None
        
        try:
            website = result.find('a',attrs={'class':'track-visit-website'})['href']
        except:
            website = None

        data.append({
            'name' : name,
            'phone' : phone,
            'adresse' : adresse,
            'website' : website
        })

    page = page + 1
    if limit != 0:
        if page*30 >= limit:
            break

# save to outputfile
df = pd.DataFrame(data)
df.to_csv(file)