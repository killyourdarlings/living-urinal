import requests
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
items = soup.findAll('div', { 'class': 'sh-dlr__content' })

results = []

# Iterate through the items.
for item in items:
    # All selectors were determined by inspection and will probably change.
    full_description_html = item.find('div', {'class': 'hBUZL'})
    title = item.find('h3').text
    price = item.find('span', {'aria-hidden': 'true'}).text
    merchant = full_description_html.find('a').text
    brief_description = item.findAll('div', {'class':'hBUZL'})[-1].text
    
    results.append(
        {
           'title': title,
           'price': price,
           'merchant': merchant,
           'brief_description': brief_description 
        }
    )


    