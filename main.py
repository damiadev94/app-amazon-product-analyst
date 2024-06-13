from bs4 import BeautifulSoup
import requests
import pandas as pd
from dotenv import load_dotenv
import os
import time

# Define headers to mimic a browser request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

#Enviroment variables
load_dotenv()
url = os.getenv("URL")
product_title = os.getenv("AMAZON_PRODUCT_TITLE")
product_reviews_quantity = os.getenv("AMAZON_PRODUCT_REVIEWS_QUANTITY")
product_price = os.getenv("AMAZON_PRODUCT_PRICE")
product_publish_date = os.getenv("AMAZON_PRODUCT_PUBLISH_DATE")

# Function to fetch HTML content of a page
def fetch_html(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    
def extract_data():
    response = fetch_html(url)
    if response != None and response.status_code >= 200 and response.status_code < 300:
        soup = BeautifulSoup(response.content,"html.parser")
        results = soup.findAll("div", {'data-component-type': 's-search-result'})
        for result in results:
            print(result)
            print("\n")

def data_to_csv():
    return

def init():
    return    

init()
