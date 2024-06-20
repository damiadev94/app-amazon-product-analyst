from bs4 import BeautifulSoup
import asyncio
import logging

def scrape_data(html:str):
        if html:
            soup = BeautifulSoup(html,"html.parser")
            logging.info("data scraped successfully.")
            return soup
        else:
            print("Error scraping data")

