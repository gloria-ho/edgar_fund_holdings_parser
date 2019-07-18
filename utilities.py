import requests
import csv
from bs4 import BeautifulSoup as Soup


def parse_xml(source):
  
  return None


url = "https://www.sec.gov/Archives/edgar/data/1166559/000110465919029714/primary_doc.xml"
resp = requests.get(url)
soup = Soup(resp.text, "xml")

tags = ([tag.name for tag in soup.find_all(True, text=True)])
obj = {}

for tag in tags:
  obj[tag] = soup.find(tag, text=True).text

print(obj)

  
with open('report.tsv', 'wt') as report_file:
  tsv_writer = csv.writer(report_file, delimiter='\t')
  
  for each in obj:
    tsv_writer.writerow([each, obj[each]])
