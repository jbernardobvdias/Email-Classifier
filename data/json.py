import json

from model.email import *

def write_json(emails, filename):
    data = []
    for email in emails:
        item = email.__dict__.copy()
        data.append(item)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def read_json(filename, labeled=False):
    with open(filename, 'r') as f:
        data = json.load(f)
    if labeled:
        return [EmailWLabel(**item) for item in data]
    else:
        return [Email(**item) for item in data]
