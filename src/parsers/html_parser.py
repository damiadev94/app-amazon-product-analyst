from bs4 import BeautifulSoup
import logging

def parse_html(bs):
    if isinstance(bs, BeautifulSoup):
        try:
            logging.info("parsing data...")
            parsed_products = []
            products = bs.find_all("div", attrs={"data-component-type":"s-search-result"})
            for product in products:
                name = product.find("span",class_="a-size-medium a-color-base a-text-normal")
                reviews = product.find("span","a-price-whole")
                price = product.find("span","a-price-whole")
                published_at = product.find("span","a-size-base a-color-secondary a-text-normal")
                item = {
                    "name":f"name: {name.get_text() if name is not None else ""}",
                    "reviews":f"reviews: {reviews.get_text() if reviews is not None else ""}",
                    "price":f"price: {price.get_text() if price is not None else ""}",
                    "published_at":f"date: {published_at.get_text() if published_at is not None else ""}"
                }
                parsed_products.append(item)
            logging.info("data parsed successfully")
            return parsed_products
        except:
            logging.error("Error parsing data.")
            return
    
