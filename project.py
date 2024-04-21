import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.fotor.com/features/old-filter/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.text, 'html.parser')

# Print out the HTML content of the webpage
print(soup.prettify())

# Find the title of the photo filter
title_element = soup.find('h1', class_='feature-title')
title = title_element.text.strip() if title_element else "Title not found"

# Find the description of the photo filter
description_element = soup.find('div', class_='feature-description')
description = description_element.text.strip() if description_element else "Description not found"

# Find the download link (if available)
download_link_element = soup.find('a', class_='download-button')
download_link = download_link_element['href'] if download_link_element else None

# Print the extracted information
print(f"Title: {title}")
print(f"Description: {description}")
if download_link:
    print(f"Download Link: {download_link}")
else:
    print("Download link not available.")
