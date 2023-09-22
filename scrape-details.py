import requests
import argparse
from bs4 import BeautifulSoup

url = 'https://secdim.com/defensive-cloud-native-app/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the title tag and extract its text
title = soup.find('title').get_text()

print(f"Title: {title}")
print("")

# Find all label elements whose 'for' attribute starts with 'date'
date_labels = soup.select('label[for^="date"]')

for label in date_labels:
    print(f"Found date: {label.text}")

booked_out_dates = soup.find_all('s')

for booked_out_date in booked_out_dates:
    print(f"Booked out date: {booked_out_date.text}")
    print("")