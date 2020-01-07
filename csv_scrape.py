import requests
from bs4 import BeautifulSoup
import csv 

url = 'https://www.crunchyroll.com/my-hero-academia/reviews/helpful/page1'

page = requests.get(url)
page.text

soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())

p = soup.find_all(class_='trunc')
# print(p)

for i in p:
    text = i.text
    print(text)

lines = []
for t in soup.find_all('div', {'class':'trunc'},{'class': 'more'}):
    text = t.text.replace("\t", "").replace("\r", "").replace('\n', '')
    lines.append(' '.join(text.split()[::]))

with open('myCSVfile.csv', 'w') as f:
    for line in lines:
        f.write(line + '\n')
    # writer = csv.writer(f, delimiter=',')
    # writer.writerow(lines)


