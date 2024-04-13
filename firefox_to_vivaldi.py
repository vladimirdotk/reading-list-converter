""" Reading list converter. Converts browsers reading from Firefox to Vivaldi format. """

import json
import csv
import os
import time

firefox_list = os.environ.get('FIREFOX_READING_LIST')
if not firefox_list:
    raise ValueError('FIREFOX_READING_LIST environment variable is not set')

with open(firefox_list, 'r', encoding='utf-8') as file:
    data = json.load(file)

    current_unix_time = int(time.time())
    vivaldi_reading_list = f'vivaldi_reading_list_{current_unix_time}.csv'

    with open(vivaldi_reading_list, 'w', encoding='utf-8', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Title', 'Selection', 'Folder', 'Timestamp'])

        for item in data.items():
            name = item[0]
            element = item[1]

            if name == 'settings':
                continue

            FOLDER = 'Archive' if element.get('viewed', False) else 'Unread'
            writer.writerow([element['url'], element['title'], '', FOLDER, element['addedAt']])
