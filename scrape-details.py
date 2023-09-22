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

print("Found Dates:")

dates = []
for label in date_labels:
    date = label.text.replace('\n', '')
    dates.append(date)
print(dates)

booked_out_dates = soup.find_all('s')

print("")
print("Booked out dates:")

out_dates = []
for booked_out_date in booked_out_dates:
    out_date = booked_out_date.text
    out_dates.append(out_date)
print(out_dates)

print("")
if date not in out_dates:
    print(f"{date} appears to be available")
else:
    print(f"{date} is booked out")