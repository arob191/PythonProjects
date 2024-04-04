
import requests
from scrapingbee import ScrapingBeeClient
import csv
import os
from bs4 import BeautifulSoup
# 'F2XZ1PAL0AWHY16ALCKL94RZ8A74O8IF5EEQM1962VHDOE5XTLXU5S1EFG686HVSH2A4OHEBAF6XX575'

# Function to scrape a single page and return the table rows
def scrape_page(page_url):
    # ScrapingBee API endpoint
    scrapingbee_endpoint = 'https://app.scrapingbee.com/api/v1/'
    
    # Parameters for ScrapingBee API
    params = {
        'api_key': 'F2XZ1PAL0AWHY16ALCKL94RZ8A74O8IF5EEQM1962VHDOE5XTLXU5S1EFG686HVSH2A4OHEBAF6XX575',
        'url': page_url,
        'render_js': 'false',
    }
    
    # Send a GET request to ScrapingBee API
    response = requests.get(scrapingbee_endpoint, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table you're interested in scraping
        # You'll need to inspect the HTML structure to find the correct table or class name
        table = soup.find('table', {'id': 'coleccion'})
        if table:
            # Extract the text from each table data <td> tag
            return [[td.text.strip() for td in row.find_all('td')] for row in table.find_all('tr', {'class': ['odd', 'even']})]
        else:
            print('Table not found. Please check the ID and ensure the table exists.')
            return None
    else:
        print(f'Failed to retrieve the webpage. Status Code: {response.status_code}')
        return None

# Function to save data to CSV
def save_to_csv(data, filename, headers):
    # Check if the file exists
    file_exists = os.path.isfile(filename)
    # Open the file in append mode, or create it if it doesn't exist
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Write headers only if the file is being created
        if not file_exists:
            writer.writerow(headers)
        writer.writerows(data)

# Main script
if __name__ == '__main__':
    base_url = 'https://pares.mcu.es/MovimientosMigratorios/buscadorRaw.form?d-3602157-p='
    objects_per_page = 25
    page_number = 491  # Start from page 1
    csv_filename = 'scraped_data.csv'  # Define the CSV filename
    # Define your headers here based on the table structure
    headers = ['Header1', 'Header2', 'Header3', ...]
    
    while True:
        page_url = f'{base_url}{page_number}&objectsPerPage={objects_per_page}'
        page_data = scrape_page(page_url)
        
        if page_data:
            # Append the data to the same CSV file
            save_to_csv(page_data, csv_filename, headers)
            print(f'Data from page {page_number} appended to {csv_filename}')
            page_number += 1
        else:
            break