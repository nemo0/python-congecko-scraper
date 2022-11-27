# Scraping Coingecko crypto prices and store into a csv file
# Author: @Ami_Subha

from bs4 import BeautifulSoup
import requests
import json

r = requests.get('https://www.coingecko.com/en/coins/ethereum/historical_data#panel')

soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find('table', attrs={'class': 'table table-striped text-sm text-lg-normal'})

table_data = table.find_all('tr')

table_headings = []

for th in table_data[0].find_all('th'):
    table_headings.append(th.text)

table_details = []

for tr in table_data:
    th = tr.find_all('th')
    td = tr.find_all('td')

    data = {}

    for i in range(len(td)):
        data.update({table_headings[0]: th[0].text})
        data.update({table_headings[i+1]: td[i].text.replace('\n', '')})

    if data.__len__() > 0:
        table_details.append(data)

with open('table.json', 'w') as f:
    json.dump(table_details, f, indent=2)
    print('Data saved to json file...')
    