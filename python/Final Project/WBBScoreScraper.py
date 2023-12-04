from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}

url = r"https://www.sports-reference.com/cbb/schools/cincinnati/women/2024-schedule.html"
source = requests.get(url, headers= headers)
soup = BeautifulSoup(source.content, 'lxml')

header = [th.getText() for th in soup.findAll('tr', limit=3)[2].findAll('th')]
header = header[1:]
rows = soup.findAll('tr')[1:]

game_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
stats = pd.DataFrame(game_stats, columns=header)
print(stats)

