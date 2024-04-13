import json
import csv
import os
import time

firefox_list = os.environ.get('FIREFOX_READING_LIST')
if not firefox_list:
    raise ValueError('FIREFOX_READING_LIST environment variable is not set')

with open(firefox_list, 'r') as file:
    data = json.load(file)

    current_unix_time = int(time.time())

    with open(f'vivaldi_reading_list_{current_unix_time}.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Title', 'Selection', 'Folder', 'Timestamp'])

        for item in data.items():
            name = item[0]
            element = item[1]

            if name == 'settings':
                continue

            folder = 'Archive' if element.get('viewed', False) else 'Unread'
            writer.writerow([element['url'], element['title'], '', folder, element['addedAt']])
