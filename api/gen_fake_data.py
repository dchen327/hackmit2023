import json
from datetime import datetime
from faker import Faker
import random

fake = Faker()

college_summer_items = [
    'Fridge',
    'Microwave',
    'Television',
    'Bicycle',
    'Cooking Essentials',
    'Desk',
    'Chair',
    'Air Conditioner',
    'Laundry Supplies',
    'Cleaning Supplies',
    'Desk Lamp',
    'Storage Bins',
    'Ironing Board',
    'Alarm Clock',
    'Extension Cord',
    'Toaster',
    'Coffee Machine',
    'Waffle Maker',
    'Panini Press',
    'Toolkit',
    'Board Games',
    'Nintendo Switch',
    'Textbook'
]

def generate_fake_supply_info():
    item_name = random.choice(college_summer_items)
    supply_info = {
        'itemName': item_name,
        'startDate': fake.date_between(start_date=datetime(2023, 5, 1), end_date=datetime(2023, 5, 31)).strftime("%m/%d/%Y"),  # Random date within the last 30 days and next 30 days
        'endDate': fake.date_between(start_date=datetime(2023, 8, 1), end_date=datetime(2023, 8, 27)).strftime("%m/%d/%Y"),  # Random date between 31 and 90 days from now
        'price': 5 * fake.random_int(min=1, max=50),  # Random price between 10 and 200
        'pictures': [item_name.lower().replace(' ', '') + '.jpg'],
        'contact': fake.email(),  # Fake email address
        'addlNotes': fake.text()  # Fake additional notes
    }
    return supply_info

supply_info_list = [generate_fake_supply_info() for _ in range(100)]


# write to file
FILE_NAME = 'college_supplies.json'
with open(FILE_NAME, 'w') as json_file:
    json.dump(supply_info_list, json_file)