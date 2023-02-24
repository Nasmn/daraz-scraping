import requests
from bs4 import BeautifulSoup
import re
import csv
import json

url = 'https://www.daraz.com.np/catalog/?spm=a2a0e.11779170.search.1.58112d2bYOmFx7&q=food items&_keyori=ss&from=search_history&sugg=food items_0_1'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
script = soup.find("script", text=re.compile("window.pageData"))
data = json.loads(script.string[16:])

columns = ['item', 'unit', 'amount']
with open ('items.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    for items in data['mods']['filter']['filterItems']:
        if 'options' in items:
            for a in items['options']:
                writer.writerow([a['title'], '', ''])
