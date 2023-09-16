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

    @staticmethod
    def create_puzzle(params):
        four_nums = [random.randint(1, 12) for _ in range(4)]
        return {'gameNums': four_nums}
