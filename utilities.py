import requests
import csv
from bs4 import BeautifulSoup as Soup

def parse_xml(url):  
  resp = requests.get(str(url))
  soup = Soup(resp.text, "xml")
  tags = ([tag.name for tag in soup.find_all(True, text=True)])
  data = {}
  for tag in tags:
    data[tag] = soup.find(tag, text=True).text
  return data

def write_tsv(data):
  with open(data["cik"] + "_" + data["reportCalendarOrQuarter"] + "_13f.tsv", "wt") as report_file:
    tsv_writer = csv.writer(report_file, delimiter="\t")
    for each in data:
      tsv_writer.writerow([each, data[each]])

def xml_to_tsv(url):
  if url is None:
    print("\nError, cannot find 13F report for this CIK. Please try again.")
    return None
  data = parse_xml(url)
  write_tsv(data)
