from Edgar import Edgar
from utilities import parse_xml

def parser():
  print("Welcome to the EDGAR Fund Holdings parser.")
  x = input("Please enter a stock ticker or CIK.  ")
  a = Edgar(str(x))
  print(a.report())

def end_parser():
  prompt = input("Do you want to try again?  (y/n)  " )
  return prompt

parser()
while end_parser() == 'y':
  parser()


# # testing
# g = Edgar("goog")
# b = Edgar("0001166559")
# # test ticker_to_cik function
# print(g.ticker_to_cik()) #0001652044
# # test cik_to_company function
# print(g.cik_to_company()) # Alphabet Inc.
# print(b.cik_to_company()) # Bill & Melinda Gates Foundation Trust
# # test 13f
# print(g.report()) # Error, cannot find 13F report for this CIK.
# print(b.report()) #