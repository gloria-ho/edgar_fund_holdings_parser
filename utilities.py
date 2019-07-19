import requests
import csv
from bs4 import BeautifulSoup as Soup
import os

def parse_xml(url):  
  resp = requests.get(str(url))
  soup = Soup(resp.text, "xml")
  tags = ([tag.name for tag in soup.find_all(True, text=True)])
  # find all tags that wrap text and save as a key value pair
  data = {}
  for tag in tags:
    data[tag] = soup.find(tag, text=True).text
  return data

def write_tsv(data):
  # check if reports/ path exists, or create one
  if not os.path.exists("reports/"):
    os.mkdir("reports/")
  file_name = "reports/" + data["cik"] + "_" + data["reportCalendarOrQuarter"] + "_13f.tsv"
  # write and save a tsv with a new row per set of key value pairs
  with open(file_name, "wt") as report_file:
    tsv_writer = csv.writer(report_file, delimiter="\t")
    for each in data:
      tsv_writer.writerow([each, data[each]])
  print("\nReport has been saved as " + file_name)

def xml_to_tsv(url):
  if url is None:
    print("\nError, cannot find 13F report for this CIK. Please try again.")
    return None
  data = parse_xml(url)
  write_tsv(data)
