def clean_items(items):
    if items:
        cleaned_items = []
        for item in items:
            cleaned_item={}
            for i in item:
                v = item[i].strip()
                cleaned_item[i] = v if v is not None else ""
            cleaned_items.append(cleaned_item)
        print("data cleaned successfully")
        return cleaned_items
    else:
        print("Error cleaning data")
        return
