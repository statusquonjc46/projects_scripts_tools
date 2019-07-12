import bs4 as bs
import urllib.request
import csv

# webpage data scraper for table data based on table class that outputs to a csv
url = urllib.request.urlopen('<your url to scrape here>').read()
urlSoup = bs.BeautifulSoup(url, 'lxml')
urlList = []
for table in urlSoup.find_all('table', class_='<table class>'):
    urlString = table.text

for string in urlString.splitlines():
    urlList.append(string)

csvFile = open('<csv file name>', 'w')
writer = csv.writer(csvFile)
for item in urlList:
    writer.writerow([item])
csvFile.close()
