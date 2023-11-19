import random
import json
import csv

import faker


MOCK_DOCUMENT_HITS_AMOUNT = 20000
MOCK_DATASET_PATH = 'part-B/data/mock_documents.csv'



def generate_mock_dataset():
    fake = faker.Faker()
    documents = []

    for _ in range(MOCK_DOCUMENT_HITS_AMOUNT):
        document = {
            'timestamp': fake.date_time_this_decade().isoformat() + 'Z',
            'session': fake.random_element(['S74650220', 'S74650221', 'S74650222', 'S74650223', 'S74650224', 'S74650225', 'S74650226', 'S74650220', 'S74650221', 'S74650220']),
            'remote_address': fake.ipv4(),
            'path': fake.url(),
            'referrer': fake.word(),
            'timezone_offset': fake.random_element(['-120', '-60', '-240']),
            'language': fake.language_code(),
            'city': fake.city(),
            'region': fake.state(),
            'country': fake.country(),
            'continent': fake.random_element(['Europe', 'NA', 'SA']),
            'latitude': round(random.uniform(-90, 90), 4),
            'longitude': round(random.uniform(-180, 180), 4),
            'browser': fake.user_agent(),
            'browser_version': fake.random_element(['rv:11.0', 'rv:12.0', 'rv:13.0']),
            'agent_type': fake.random_element(['Browser', 'Mobile', 'Tablet']),
            'agent_category': fake.random_element(['Personal computer', 'Mobile device', 'Tablet']),
            'os': fake.random_element(['Windows', 'Linux', 'Mac OS']),
            'platform': fake.random_element(['Windows', 'Linux', 'Mac OS']),
        }
        documents.append(document)
        
    columns = [
        'timestamp',
        'session',
        'remote_address',
        'path',
        'referrer',
        'timezone_offset',
        'language',
        'city',
        'region',
        'country',
        'continent',
        'latitude',
        'longitude',
        'browser',
        'browser_version',
        'agent_type',
        'agent_category',
        'os',
        'platform',
    ]
    with open(
        MOCK_DATASET_PATH, 
        'w', 
        newline='', 
        encoding='utf-8',
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file, 
            fieldnames=columns,
        )
        writer.writeheader()
        writer.writerows(documents)

if __name__ == '__main__':
    generate_mock_dataset()
    