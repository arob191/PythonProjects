import requests
from bs4 import BeautifulSoup
import csv
import time

# URL of the website to scrape
url = 'https://pares.mcu.es/MovimientosMigratorios/buscadorRaw.form?d-3602157-p=1&objectsPerPage=25'

# Define a delay duration in seconds (e.g., 10 seconds)
delay = 100

# Send a GET request to the website with a delay between each request
try:
    while True:
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all elements with class 'even' and 'odd'
            even_elements = soup.find_all(class_='even')
            odd_elements = soup.find_all(class_='odd')
            
            # Combine even and odd elements
            all_elements = even_elements + odd_elements
            
            # Open a CSV file to write the data
            with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                # Write header row
                writer.writerow(['Content'])
                
                # Iterate over all elements and write their content to the CSV
                for element in all_elements:
                    writer.writerow([element.text.strip()])
                    print(element.text.strip())
            
            # Wait for the specified delay duration before making the next request
            time.sleep(delay)
        else:
            print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
            break
except KeyboardInterrupt:
    print('Stopped by user.')

# Print a success message
print("Scraping completed successfully.")