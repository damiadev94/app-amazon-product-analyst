import os
import json
import requests
import logging
import threading

initial_proxies = []
cleaned_proxies = []

#OPEN JSON WITH PROXIES DATA, SAVES IN "DATA"
relative_path = os.path.join(os.path.dirname(__file__), "..", "config", "proxies.json")
with open(relative_path, "r") as file:
    data = json.load(file)

for proxy in data["proxies"]:
    initial_proxies.append(proxy["proxy"])

################################################################################################

#EXTRACT THE PROXIE URL, SAVES IN "PROXIES"
def clean_proxies(proxies,len,headers):
    for i in range(len):
        try:
            test = requests.get(proxies[i],headers=headers)
            if test.status_code < 300:
                cleaned_proxies.append(proxy)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error at request: {e}")
    return cleaned_proxies

thread1 = threading.Thread(target=clean_proxies,args={"proxies":cleaned_proxies,"len":len(cleaned_proxies)})

def start():
    thread1.start()
    thread1.join()
    print("Thread1 has finished.")
    return cleaned_proxies