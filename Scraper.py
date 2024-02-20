import requests
from bs4 import BeautifulSoup
import fitz

class Scraper:
    def __init__(self, url):
        self.url = url
       
    def fetch_html(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            html = response.text
        else:
            raise Exception(f"Failed to fetch HTML: {response.status_code}")
        
        return html
    
    def extract_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        article_content = soup.find('div', class_ = 'article-content')

        # create BeautifulSoup object with only the article content 
        extracted_content = BeautifulSoup(str(article_content), 'html.parser')

        return extracted_content.prettify()
    
    def scrape_page(self):
        html = self.fetch_html()
        data = self.extract_content(html)

        return data 
    
    