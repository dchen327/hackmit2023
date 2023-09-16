from http.server import BaseHTTPRequestHandler
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
    supply_info = {
        'itemName': random.choice(college_summer_items),
        'startDate': fake.date_between(start_date='-120d', end_date='-110d'),  # Random date within the last 30 days and next 30 days
        'endDate': fake.date_between(start_date='-30d', end_date='-10d'),  # Random date between 31 and 90 days from now
        'price': 5 * fake.random_int(min=1, max=50),  # Random price between 10 and 200
        'pictures': [fake.file_name(extension='jpg') for _ in range(fake.random_int(min=0, max=5))],  # Random list of picture filenames
        'contact': fake.email(),  # Fake email address
        'addlNotes': fake.text()  # Fake additional notes
    }
    return supply_info

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        ''' 
        Takes in a demand object, returns a list of supply objects 
        that match
        '''
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        content_len = int(self.headers.get('Content-Length'))
        params = json.loads(self.rfile.read(content_len))
        search_results = self.search(params)
        self.wfile.write(json.dumps(search_results).encode())

    @staticmethod
    def search(params):
        print(params)
        demand_info = {
            'itemName': 'TV',
            # when you're free to lend item
            'startDate': datetime.strptime('5/15/2023', "%m/%d/%Y"),
            # when you need item back
            'endDate': datetime.strptime('8/12/2023', "%m/%d/%Y"),
        }

        supply_info = {
            'itemName': 'TV',  # what you have
            # when you're free to lend item
            'startDate': datetime.strptime('5/15/2023', "%m/%d/%Y"),
            # when you need item back
            'endDate': datetime.strptime('8/12/2023', "%m/%d/%Y"),
            'price': 50,  # how many dollars to charge
            'pictures': [],  # list of picture filenames (hardcode)
            'contact': 'bobsmith@college.edu',
            'addlNotes': '',  # additional notes in text
        }

        supply_info_list = [generate_fake_supply_info() for _ in range(3)]

        # Convert date objects to strings with the specified format
        for supply_info in supply_info_list:
            supply_info['startDate'] = supply_info['startDate'].strftime("%m/%d/%Y")
            supply_info['endDate'] = supply_info['endDate'].strftime("%m/%d/%Y")
            
        return {'itemMatches': supply_info_list}

if __name__ == '__main__':
    print(handler.search({}))