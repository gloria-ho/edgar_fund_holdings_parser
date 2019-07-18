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