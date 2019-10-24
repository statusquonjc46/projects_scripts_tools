import bs4 as bs
import urllib.request
import csv

# webpage data scraper for table data based on table class that outputs to a csv
url = urllib.request.urlopen('https://clinicaltrials.gov/ct2/results?cond=&term=&cntry=&state=&city=&dist=').read()
urlSoup = bs.BeautifulSoup(url, 'lxml')
urlList = []
urlString = ''
for table in urlSoup.find_all('td'):
    urlString = table.text

for string in urlString.splitlines():
    urlList.append(string)

csvFile = open('clintrials', 'w')
writer = csv.writer(csvFile)
for item in urlList:
    writer.writerow([item])
csvFile.close()
