#Requests allows us to query an HTML page to be used for BeautifulSoup. The Pandas import allows us to display the information as a table. 
from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}

#the URL is the webpage we will be using to scrape for data. The header will be the same for MBB and WBB but the tr is limited to the first 3 tables on the page, with the [1] referring to the second table on the page.
#Source tells us where the data will come from and we are parsing this using lxml.
url = r"https://www.sports-reference.com/cbb/schools/cincinnati/men/2024-schedule.html"
source = requests.get(url, headers= headers)
soup = BeautifulSoup(source.content, 'lxml')

#This is telling the script to pull all the data in the td for every row in the table. This allows us to pull all the data into the output and is not limited by length and will pull all rows into the data. 
header = [th.getText() for th in soup.findAll('tr', limit=3)[2].findAll('th')]
header = header[1:]
rows = soup.findAll('tr')[1:]

game_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
stats = pd.DataFrame(game_stats, columns=header)
#This is how we get the table to display in the terminal. 
print(stats)

