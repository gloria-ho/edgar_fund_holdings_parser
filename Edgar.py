import requests
from bs4 import BeautifulSoup as Soup

class Edgar:

  def __init__(self, input):
    self.input = input
    self.url = "https://www.sec.gov/"
    self.query_url = self.url + "cgi-bin/browse-edgar?action=getcompany&CIK="
    self.query = self.query_url + input

  def fetch_query(self, query):
    resp = requests.get(query)
    soup = Soup(resp.text, "html.parser")
    return soup

  def query_13f(self):
  # narrow query paras to '13F-HR' type and return results
    query_13f = self.query + "&type=13F-HR&dateb=&owner=include&count=40"
    query_13f_resp = requests.get(query_13f)
    query_13f_soup = Soup(query_13f_resp.text, "html.parser")
    return query_13f_soup

  def fetch_13f_filing(self):
  # fetch the 13f filing details and return the result
    query_13f = self.query_13f()
    # find the documents button and parse the details page
    try:
      button = query_13f("a", id="documentsbutton")[0]
    except IndexError:
      return None
    doc_url= self.url + button["href"]
    doc_filing_pg = requests.get(doc_url)
    doc_filing_soup = Soup(doc_filing_pg.text, "html.parser")
    return doc_filing_soup

  def fetch_13f_url(self):
  # fetch and return the xml link
    filing = self.fetch_13f_filing()
    if filing is None:
      return None
    primary_doc = filing.find("a", string="primary_doc.xml")
    doc_query = primary_doc["href"]
    doc_url = self.url + doc_query
    return doc_url