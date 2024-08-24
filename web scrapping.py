import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://techcrunch.com/"

# Fetch the content from the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the fetched content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all article titles by looking for specific tags
    # The tag 'a' with class 'post-block__title__link' typically contains article titles on TechCrunch
    titles = soup.find_all('a', class_='post-block__title__link')

    # Print each title
    for title in titles:
        print(title.text.strip())

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
