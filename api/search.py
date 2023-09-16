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
    item_name = random.choice(college_summer_items)
    supply_info = {
        'itemName': item_name,
        'startDate': fake.date_between(start_date=datetime(2023, 5, 1), end_date=datetime(2023, 5, 31)),  # Random date within the last 30 days and next 30 days
        'endDate': fake.date_between(start_date=datetime(2023, 8, 1), end_date=datetime(2023, 8, 27)),  # Random date between 31 and 90 days from now
        'price': 5 * fake.random_int(min=1, max=50),  # Random price between 10 and 200
        'pictures': [item_name.lower().replace(' ', '') + '.jpg'],
        'contact': fake.email(),  # Fake email address
        'addlNotes': fake.text()  # Fake additional notes
    }
    return supply_info

def convert_date(date_str):
    return datetime.strptime(date_str, "%m/%d/%Y").date()

def convert_matches(matches):
    # Convert date objects to strings with the specified format
    for match in matches:
        match['startDate'] = match['startDate'].strftime("%m/%d/%Y")
        match['endDate'] = match['endDate'].strftime("%m/%d/%Y")
    
    return matches


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
        item_name = params['itemName']
        start_date = convert_date(params['startDate'] or '5/15/2023')
        end_date = convert_date(params['endDate'] or '8/15/2023')
        max_price = int(params['maxPrice'] or 500)

        supply_info_list = [generate_fake_supply_info() for _ in range(100)]
        
        matches = []
        for supply_info in supply_info_list:
            if (item_name == '' or supply_info['itemName'] == item_name) and \
                supply_info['price'] <= max_price and \
                abs((supply_info['startDate'] - start_date).days) <= 7 and \
                abs((supply_info['endDate'] - end_date).days) <= 7:
                matches.append(supply_info)
            
        print(matches)
        return {'itemMatches': convert_matches(matches)}

if __name__ == '__main__':
    print(handler.search({}))