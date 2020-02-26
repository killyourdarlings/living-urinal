import requests
import csv
from bs4 import BeautifulSoup

# Establish a session.
session = requests.Session()

# Set up important headers.
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:72.0) Gecko/20100101 Firefox/72.0'
})

# Establish a base URL
url = 'https://www.google.com/search?q=urinal&tbm=shop'
response = session.get(url)

# Parse the results.
soup = BeautifulSoup(response.content, 'lxml')

# Extract the items. The class name was determined by inspecting the HTML.
items = soup.findAll('div', {'class': 'sh-dlr__content'})

results = []

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(
        employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(["TITLE", "PRICE", "MERCHANT", "DESCRIPTION"])
    # Iterate through the items.
    for item in items:
        # All selectors were determined by inspection and will probably change.
        try:
            full_description_html = item.find('div', {'class': 'hBUZL'})
        except:
            full_description_html = "NONE"

        try:
            title = item.find('h3').text
        except:
            title = "NONE"
            print("No Title")

        try:
            price = item.find('span', {'aria-hidden': 'true'}).text
        except:
            price = "NONE"
            print("No Price")

        try:
            merchant = full_description_html.find('a').text
        except:
            merchant = "NONE"
            print("No Merchant")

        try:
            brief_description = item.findAll('div', {'class': 'hBUZL'})[-1].text
        except:
            brief_description="NONE"
            print("No Brief Description")

        employee_writer.writerow([title, price, merchant, brief_description])

        results.append(
            {
                'title': title,
                'price': price,
                'merchant': merchant,
                'brief_description': brief_description
            }
        )
        

print("Ok!")
