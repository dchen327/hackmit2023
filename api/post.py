from http.server import BaseHTTPRequestHandler
import json
import random


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        content_len = int(self.headers.get('Content-Length'))
        params = json.loads(self.rfile.read(content_len))
        puzzle_info = self.post(params)
        self.wfile.write(json.dumps(puzzle_info).encode())

    real_supply_info_list = []

    def post(self, params):
        title = params['title']
        description = params['description']
        startDate = params['startDate']
        endDate = params['endDate']
        price = params['price']
        contact = params['contact']

        FILE_NAME = 'college_supplies.json'
        with open(FILE_NAME, 'r') as json_file:
            existing_data = json.load(json_file)
        supply_info = {
            'itemName': title, 
            'description': " ",
            'startDate': startDate,
            'endDate': endDate,
            'price': price,
            'contact': contact,
            'addlNotes': description
            }
        
        # append data to existing data
        existing_data.append(supply_info)

        print(existing_data[-1])
        with open(FILE_NAME, 'w') as json_file:
            json.dump(existing_data, json_file)
        return True