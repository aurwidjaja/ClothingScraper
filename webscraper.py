import requests
from bs4 import BeautifulSoup

url = 'https://www.ebay.com/sch/i.html?_nkw=laptop'  # eBay search URL
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the page: {response.status_code}")

soup = BeautifulSoup(html_content, 'html.parser')

with open('ebay_html.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

#https://github.com/alexis-brosseau/Ebay-Scraper
#https://github.com/Lau7an/PoshmarkInventoryAndImageScraper/blob/main/PoshmarkInventoryAndImageScraper.ipynb
#https://github.com/Gertje823/Vinted-Scraper
#https://oxylabs.io/blog/scrapy-web-scraping-tutorial
    # Maybe instead of manually scraping through BeautifulSoup we can use scrapy?


