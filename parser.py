from Edgar import Edgar
# from utilities import xml_to_tsv
import utilities as util

def end_parser():
  prompt = input("\nDo you want to try again?  (y/n)  " )
  return prompt

def parser():
  stock = input("\nPlease enter a stock ticker or CIK.  ")
  output = Edgar(str(stock))
  util.xml_to_tsv(output.fetch_13f_url())
  return end_parser()

# start app
print("\nWelcome to the EDGAR Fund Holdings Parser.")
prompt = parser()
# ask if user wants to try again
while prompt == 'y':
  prompt = parser()
if prompt == 'n':
  print("\nThank you for trying the EDGAR Fund Holdings Parser. I hope you found it useful.")
else:
  print("\nSorry, I did not understand you. Thank you for trying the EDGAR Fund Holdings Parser. I hope you found it useful.")


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