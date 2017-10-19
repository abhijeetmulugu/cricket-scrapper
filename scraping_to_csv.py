import csv
import sys
sys.path.append('C:/Users/ABHIJEET/Anaconda2/Lib/site-packages')
from bs4 import BeautifulSoup

import requests

r=requests.get("http://stats.espncricinfo.com/ci/engine/player/597806.html?class=9;template=results;type=batting;view=innings")

soup = BeautifulSoup(r.content)


table=soup.find_all('table', class_='engineTable')

list_of_rows = []
for row in table[3].findAll('tr',class_='headlinks'):
    list_of_cells = []
    for cell in row.findAll('th'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

    
for row in table[3].findAll('tr',class_='data1'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)



outfile = open("G:/cricket/smriti-all.csv", "w")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
outfile.flush() 
