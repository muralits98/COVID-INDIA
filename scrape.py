import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd

URL = 'https://www.mohfw.gov.in/'
page = requests.get(URL)

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

soup = BeautifulSoup(page.content, 'html.parser')
A = [tag.extract() for tag in soup.find_all("tr")]
for i in A:
    print(i.get_text())

sys.stdout = orig_stdout
f.close()

f = open('out.txt')
line = f.readline()
C = []
while line:
    if line != '\n':
        C.append(line.rstrip())
    line = f.readline()

ANS = []
i = 0
while i<len(C):
    ab = C[i:i+6]
    ANS.append(ab)
    # print(ab)
    i = i+6
df = pd.DataFrame(ANS[1:len(ANS)-1],columns=ANS[0])
print(df)
df.to_csv(r'\Dataset\19032020COVIDIND.csv')