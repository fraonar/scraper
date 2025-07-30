import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class YelpScraper:
    def __init__(self, location, max_pages=5):
        self.location = location
        self.max_pages = max_pages
        self.businesses = []

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def scrape(self):
        search_url = f"https://www.yelp.com/search?find_desc=Restaurants&find_loc={self.location.replace(' ', '+')}"
        self.driver.get(search_url)
        time.sleep(2)

        for page in range(self.max_pages):
            self._parse_page()
            try:
                next_button = self.driver.find_element("xpath", "//a[@class='css-1um8m8n']")
                next_button.click()
                time.sleep(2)
            except Exception as e:
                print("No more pages to scrape or an error occurred:", e)
                break

    def _parse_page(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        business_cards = soup.find_all("div", class_="css-1l5lt1i")

        for card in business_cards:
            name = card.find("a", class_="css-1422juy").text
            phone = card.find("p", class_="css-1p9ibgf").text if card.find("p", class_="css-1p9ibgf") else None
            address = card.find("address").text if card.find("address") else None
            website = card.find("a", class_="css-1um8m8n")['href'] if card.find("a", class_="css-1um8m8n") else None

            self.businesses.append({
                'name': name,
                'phone': phone,
                'address': address,
                'website': website
            })

    def close(self):
        self.driver.quit()

    def get_businesses(self):
        return self.businesses