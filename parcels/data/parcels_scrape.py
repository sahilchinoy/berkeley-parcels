import csv
import requests
from bs4 import BeautifulSoup

with open('scraped_parcels.csv', 'a') as outfile:
    fieldnames = ['location_id','APN','address','lot_size','building_size','owner','county_use']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    for location_id in range(55492, 73983):
        url = 'http://www.cityofberkeley.info/ppop/home/Summary/{}'.format(location_id)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        try:
            rows = soup.table.find_all('tr')
            out_row = {}
            out_row['location_id'] = location_id
            out_row['APN'] = rows[1].contents[1].string.strip()
            out_row['address'] = rows[2].contents[1].string.strip()
            out_row['lot_size'] = rows[3].contents[1].string.strip()
            out_row['building_size'] = rows[4].contents[1].string.strip()
            out_row['owner'] = rows[5].contents[1].string.strip()
            out_row['county_use'] = rows[6].contents[1].string.strip()
            writer.writerow(out_row)
            print location_id
            print out_row['owner']
        except AttributeError:
            pass
