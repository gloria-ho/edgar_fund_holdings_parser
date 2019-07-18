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

  def ticker_or_cik():
  # checks for valid stock ticker or CIK value
    return None

  def ticker_to_cik(self):
  # convert a stock ticker to CIK
    # find if a tag with CIK exists
    soup = self.fetch_query(self.query)
    try:
      cik_tag = soup("input", attrs={"name": "CIK"})[0]
    except IndexError:
      return "Error: invalid ticker, please check and try again."
    cik = cik_tag['value']
    return cik

  def cik_to_company(self):
  # convert a CIK to company name
    soup = self.fetch_query(self.query)
    # find tag with the class companyName
    company_tag = soup("span", attrs={"class": "companyName"})[0]
    company = company_tag.contents[0]
    return company

  def query_13f(self):
  # search for 13F report and return query results
    # narrow search params to 13F, parse response
    query_13f = self.query + "&type=13F-HR&dateb=&owner=include&count=40"
    query_13f_resp = requests.get(query_13f)
    query_13f_soup = Soup(query_13f_resp.text, "html.parser")
    return query_13f_soup

  def fetch_13f_filing(self, query_13f):
  # fetch the 13f filing details and return the result
    # find the documents button and parse the linked page
    try:
      button = query_13f("a", id="documentsbutton")[0]
    except IndexError:
      return None
    doc_url= self.url + button["href"]
    doc_filing_pg = requests.get(doc_url)
    doc_filing_soup = Soup(doc_filing_pg.text, "html.parser")
    return doc_filing_soup

  def fetch_13f_report(self, fetch_13f_filing):
  # fetch the report and return the result
    primary_doc = fetch_13f_filing.find("a", string="primary_doc.xml")
    doc_query = primary_doc["href"]
    doc_url = self.url + doc_query
    report_resp = requests.get(doc_url)
    report = Soup(report_resp.text, "html.parser")
    return report

  def report(self):
    query = self.query_13f()
    filing = self.fetch_13f_filing(query)
    if filing is None:
      return ("Error, cannot find 13F report for this CIK.")
    report = self.fetch_13f_report(filing)
    return report