import requests
import random
import logging
import asyncio

async def fetch_url(url,proxies,headers):
    proxies_to_use = {
        "http":proxies,
        "https":proxies
    }
    print(f"selected proxy: {proxies_to_use[0]}")
    logging.info(proxies_to_use[0])

    try:
        response = await requests.get(url,headers=headers,proxies=proxies_to_use)
        response.raise_for_status()
        logging.info("data fetched successfully")
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching: {e}")
        return  
    
