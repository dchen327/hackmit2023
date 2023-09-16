from http.server import BaseHTTPRequestHandler
import json
import random
from datetime import datetime


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        content_len = int(self.headers.get('Content-Length'))
        params = json.loads(self.rfile.read(content_len))
        puzzle_info = self.create_puzzle(params)
        self.wfile.write(json.dumps(puzzle_info).encode())

    @staticmethod
    def create_puzzle(params):
        four_nums = [random.randint(1, 12) for _ in range(4)]
        return {'gameNums': four_nums}


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
