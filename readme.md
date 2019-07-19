# Python EDGAR Fund Holdings Parser
Given a ticker or CIK, parses fundings report pulled from SEC's EDGAR website and writes a `.tsv` file.

### Requirements
You will need Python v.3.7.4 to run this parser. Python packages are available at <https://www.python.org/>

### Dependencies
* Beautiful Soup v4
* Requests

### Features
* Accepts CIK or ticker and finds the most current 13F-HR report
* Writes the results to a `.tsv` file

## How to Run
In the directory where you saved this code, run the following commands:
* `pip3 intall -r requirements.txt` to install dependencies
* `python3 parser.py` to run the code and follow the prompts

Any reports you generate should save to the `/reports` directory within the directory where you ran this code.

## Future Features
### Report Archive
This app currently gets only the latest 13F-HR filing. This is because the SEC's EDGAR website gives the results in chronilogical order by default. There are several ways we could pull older reports.

We can use the SEC's EDGAR website's own **Prior to: (YYYYMMDD)** date filter by changing the query parameters in the `query_13f` method in `Edgar.py`. We can change the query to `"&type=13F-HR&dateb=" + YYYYMMDD + "&owner=include&count=40"` where the date is taken from the user's input. Using the current code, we can get the most current filing, where the date is prior to the input date.

If the user wants a set of filing dates to choose from, we can change the query based on the above, and return a list of dates. We'll need to find the *nth* position of the `<th>` that wraps the string `"Filing Date"` within the `<tr>`, and then use that to `print` the text of the *nth* `<td>` `for each` `<tr>`.

If the user knows the specific filing date, we can change the `fetch_13f_filing()` method in `Edgar.py` to search for a `<td>` tag that has a matching date. We could then change the `fetch_13f_url` method to move backwards two siblings to target the `<td>` that wraps the `<a>` link to the filing details.