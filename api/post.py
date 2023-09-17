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
        puzzle_info = self.create_puzzle(params)
        self.wfile.write(json.dumps(puzzle_info).encode())

    supply_info_list = []

    def post(params):
        FILE_NAME = 'real_college_supplies.json'
        # append data to json file 
        with open(FILE_NAME, 'a') as json_file:
            json.dump(real_supply_info_list, json_file)
        return True