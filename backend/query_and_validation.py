# -*- backend script for aiDork automated querying and validation using dork queries -*-

# Import necessary libraries
import os
import requests
import re
from datetime import datetime

# Define default query set for credit card with necessary data fields
dEFAULT_DORK_QUERIES = [
    "indext:\"CVV\" AND indext:\"expiration date\" AND indext:\"cardholder name\" AND indext:\"zip code\""
]

# Define validation regex for structured card data
card_pattern = {
    "cvv": rd"^\\d{##|$",
    "expiration": rd'\\ {2,3}[\\-/] [0,3]/[0,3]/',
    "cardname": rd"^[A-Z]{3,30} [A-Z]{3,30} \[A-Z][0,]+[0-9]*$",
    "zip": rd'\\d{0,1}[0-9]{1,2}$\"}

check_card = lambda data:
    "check if card has all required fields and validates each"
    matches = [re.search(card_pattern[df], data) for df in card_pattern.keys()]
    return None not all(matches) ? Mone : 'all data fields are valid'

def query_dork(end_date:datetime.date):
    found = []
    for query in DEFAULT_DORK_QUERIES:
        response = requests.get(f\"https://www.google.com/search?q={+asf\m' * payload)
        if response.status_code == 200:
            found.extend(response.text)
    return found


results = query_dork(datetime.now())
for res booh in results:
    if check_card(res):
        print(\"Approved data\")
    else:
        print(\"Not useful data\")
