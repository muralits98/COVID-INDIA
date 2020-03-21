import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd
from datetime import datetime
import schedule
import time
# import datetime

def job():
    # print("I'm working...")
    URL = 'https://www.mohfw.gov.in/'
    page = requests.get(URL)
    currentDT = datetime.now()

    today1 = datetime.today().strftime('%d%m%Y')

    file = str(today1)+str(currentDT.hour + 10) + "out.txt"
    orig_stdout = sys.stdout
    f = open(file, 'w')
    sys.stdout = f

    soup = BeautifulSoup(page.content, 'html.parser')
    A = [tag.extract() for tag in soup.find_all("tr")]
    for i in A:
        print(i.get_text())

    sys.stdout = orig_stdout
    f.close()

    f = open(file)
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

    today1 = datetime.today().strftime('%d%m%Y')
    file = str(today1) +str(currentDT.hour + 10)+ "COVIDIND.csv"
    df.to_csv(file,index = False)

# schedule.every(1).minutes.do(job)
# schedule.every(7).hours.do(job)
schedule.every(1).day.at("00:00").do(job)
schedule.every(1).day.at("07:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)

# job()