import csv

from model.email import *

def write_csv(emails, filename):
    keys = emails[0].__dict__.keys()
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for email in emails:
            writer.writerow(email.__dict__)

def read_csv(filename, labeled=False):
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        if labeled:
            return [EmailWLabel(row['sender'], row['subject'], row['content'], row['label']) for row in reader]
        else:
            return [Email(row['sender'], row['subject'], row['content']) for row in reader]
