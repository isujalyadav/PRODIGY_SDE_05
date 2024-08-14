import urllib.request
from html.parser import HTMLParser
import csv

# Custom HTML parser class
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.products = []
        self.current_data = {}
        self.in_name = False
        self.in_price = False
        self.in_rating = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'div' and 'class' in attrs and attrs['class'] == 'product-card':
            self.current_data = {}
        if tag == 'h2' and 'class' in attrs and attrs['class'] == 'product-title':
            self.in_name = True
        if tag == 'span' and 'class' in attrs and attrs['class'] == 'product-price':
            self.in_price = True
        if tag == 'span' and 'class' in attrs and attrs['class'] == 'product-rating':
            self.in_rating = True

    def handle_endtag(self, tag):
        if tag == 'div' and self.current_data:
            self.products.append(self.current_data)
        if tag == 'h2':
            self.in_name = False
        if tag == 'span':
            self.in_price = False
            self.in_rating = False

    def handle_data(self, data):
        if self.in_name:
            self.current_data['Name'] = data.strip()
        if self.in_price:
            self.current_data['Price'] = data.strip()
        if self.in_rating:
            self.current_data['Rating'] = data.strip()

def scrape_ecommerce_site(url):
    # Send a GET request to the URL
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')

    # Parse the HTML content with the custom parser
    parser = MyHTMLParser()
    parser.feed(html_content)

    # Extracted product data
    products = parser.products

    # Save the data to a CSV file
    save_to_csv(products)

def save_to_csv(products):
    # Define the CSV file path
    filename = 'products.csv'

    # Specify the field names
    fieldnames = ['Name', 'Price', 'Rating']

    # Write the data to the CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

    print(f'Data saved to {filename}')

if __name__ == "__main__":
    # Example URL of the e-commerce site (replace with actual URL)
    url = 'https://example.com/products'

    # Start the scraping process
    scrape_ecommerce_site(url) 