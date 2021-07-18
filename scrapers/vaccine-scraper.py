import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/COVID-19_vaccine"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="mw-customcollapsible-myDivision").find("tbody").find_all("tr")
del results[0]

data = []
for tr in results:
    data.append([tr.find("b").text, tr.find_all("td")[1].text.split(',')[0].strip(), tr.find_all("td")[2].find_all('a')[0].text.strip()])

pd.DataFrame(data).to_excel('human_vac.xlsx', index=False)

# results = soup.find_all("table")[1].find("tbody").find_all("tr")
# del results[0]
#
# data = []
# for tr in results:
#     data.append([tr.find_all("td")[0].find("b").text, tr.find_all("td")[1].text.split(',')[0].strip(), tr.find_all("td")[2].find_all('a')[0].text.strip()])
#
# pd.DataFrame(data).to_excel('vac.xlsx', index=False)