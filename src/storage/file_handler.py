import pandas as pd
import time
import os
from datetime import datetime

now = datetime.now()
now_formated = f"{now.day}-{now.month}-{now.year}_{now.hour}-{now.minute}-{now.second}"

def data_to_csv(data):
    if data:
        names=[]
        reviews=[]
        prices=[]
        publish_dates=[]
        for item in data:
            names.append(item["name"])
            reviews.append(item["reviews"])
            prices.append(item["price"])
            publish_dates.append(item["published_at"])

        df = pd.DataFrame({"name":names,"reviews":reviews,"price":prices,"published at":publish_dates})
        df.to_csv(os.path.join(os.path.dirname(__file__),"files",f"{now_formated}.csv"), index=False)