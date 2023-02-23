import requests
from bs4 import BeautifulSoup
import re
url = 'https://www.daraz.com.np/catalog/?spm=a2a0e.11779170.search.1.58112d2bYOmFx7&q=food items&_keyori=ss&from=search_history&sugg=food items_0_1'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
script = soup.find("script", text=re.compile("window.pageData"))

filename = 'output.txt'
with open(filename, 'w') as f:
    f.write(script.string)
