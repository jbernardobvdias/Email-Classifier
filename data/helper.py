import pandas as pd
from data.csv import *
from data.json import *

def build_dataframe(emails):
    rows = []
    for email in emails:
        full_text = f"{email.subject} {email.content}"  # Combine fields if needed
        rows.append({"text": full_text, "label": email.label})
    return pd.DataFrame(rows)

def read(filename, label):
    filetype = filename.split(".")[-1]
    if filetype == "csv":
        return build_dataframe(read_csv(filename, label))
    if filetype == "json":
        return build_dataframe(read_json(filename, label))
    
def save(filename, filetype):
    if filetype == "csv":
        return build_dataframe(write_csv(filename))
    if filetype == "json":
        return build_dataframe(write_json(filename))
