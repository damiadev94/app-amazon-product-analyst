from scraper.request_handler import fetch_url
from scraper.bs4_scraper import scrape_data
from parsers.html_parser import parse_html
from parsers.data_cleaner import clean_items
from storage.file_handler import data_to_csv
import asyncio
import os
import logging

file_path_to_html = os.path.join(os.path.dirname(__file__),"..","tests","amazon-search-earn-money-with-ai.html")
file_path_to_headers = os.path.join(os.path.dirname(__file__),"config","headers.json")
file_path_to_proxies = os.path.join(os.path.dirname(__file__),"config","proxies.json")

with open(file_path_to_headers, "r") as file:
    headers = file.read()

with open(file_path_to_html, "r", encoding="utf-8") as file:
    html_page = file.read()

async def main():
    url="https://www.amazon.com/s?k=earn+money+with+ai&ref=nb_sb_noss"
    logging.info("fetching data...")
    html_page = await fetch_url(url,)
    scraped_data = scrape_data(html_page)
    parsed_data = parse_html(scraped_data)
    cleaned_data = clean_items(parsed_data)
    data_to_csv(cleaned_data)
    print(cleaned_data)

if __name__ == "__main__":
    asyncio.run(main())
