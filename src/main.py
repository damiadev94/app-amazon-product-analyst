import asyncio
import logging
import os
from datetime import datetime
from scraper.request_handler import fetch_url
from scraper.bs4_scraper import scrape_data
from parsers.html_parser import parse_html
from parsers.data_cleaner import clean_items
from storage.file_handler import data_to_csv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# File paths
file_path_to_html = os.path.join(os.path.dirname(__file__), "..", "tests", "amazon-search-earn-money-with-ai.html")
file_path_to_headers = os.path.join(os.path.dirname(__file__), "config", "headers.json")
file_path_to_proxies = os.path.join(os.path.dirname(__file__), "config", "proxies.json")

# Read headers from file
with open(file_path_to_headers, "r") as file:
    headers = file.read()

# Read HTML page from file
with open(file_path_to_html, "r", encoding="utf-8") as file:
    html_page = file.read()

# Name and File Path
now = datetime.now()
now_formated = f"{now.day}-{now.month}-{now.year}_{now.hour}-{now.minute}-{now.second}"
path_to_save = f"'files' , {now_formated}.csv"

async def main():
    url = "https://www.amazon.com/s?k=earn+money+with+ai&ref=nb_sb_noss"
    
    logging.info("Fetching data from URL...")
    html_page = await fetch_url(url, headers=headers)  # Pass headers to fetch_url function
    
    logging.info("Scraping data...")
    scraped_data = scrape_data(html_page)
    
    logging.info("Parsing HTML...")
    parsed_data = parse_html(scraped_data)
    
    logging.info("Cleaning data...")
    cleaned_data = clean_items(parsed_data)
    
    logging.info("Saving data to CSV...")
    data_to_csv(cleaned_data,path_to_save)
    
    print("Cleaned data:", cleaned_data)

if __name__ == "__main__":
    asyncio.run(main())
