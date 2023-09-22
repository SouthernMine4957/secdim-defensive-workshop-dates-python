import requests
import argparse
from bs4 import BeautifulSoup

def scrape_details(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title tag and extract its text
    title = soup.find('title').get_text()

    # List of possible date values
    date_values = ['date1', 'date2', 'date3', 'date4', 'date5']

    for date_value in date_values:
        label_element = soup.find('label', {'for': date_value})
        if label_element:
            print(f"Found date: {label_element.text}")
        else:
            print(f"Date for {date_value} not found")

    for date_value in date_values:
        label_element = soup.find('s')
        print (label_element)

    return(title)

print(scrape_details('https://secdim.com/defensive-cloud-native-app/'))