import pandas as pd
import os

def data_to_csv(data,path):
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
        df.to_csv(os.path.join(os.path.dirname(__file__),path), index=False)