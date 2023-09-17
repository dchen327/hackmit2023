from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime, timedelta
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

college_summer_items_descriptions = {
    'Fridge': "A compact and energy-efficient fridge perfect for keeping your beverages and snacks cold during those hot summer days.",
    'Microwave': "This microwave is a convenient addition to your dorm room, making it easy to heat up leftovers or make a quick snack.",
    'Television': "Enjoy your favorite shows and movies with this high-definition television, perfect for movie nights with your roommates.",
    'Bicycle': "Get around campus quickly and easily with this sturdy and reliable bicycle, complete with a built-in lock.",
    'Cooking Essentials': "Cook like a pro with our cooking essentials kit, which includes pots, pans, utensils, and more for all your culinary needs.",
    'Desk': "Stay organized and focused with this spacious and functional desk, ideal for studying or working on assignments.",
    'Chair': "Sit in comfort with this ergonomic chair, designed to provide support during long study sessions or gaming marathons.",
    'Air Conditioner': "Beat the summer heat with this powerful air conditioner, ensuring a cool and comfortable living space.",
    'Laundry Supplies': "Keep your clothes fresh and clean with our laundry supplies, including detergent, dryer sheets, and laundry baskets.",
    'Cleaning Supplies': "Maintain a clean and tidy living environment with our cleaning supplies, featuring all the essentials for a spotless space.",
    'Desk Lamp': "Illuminate your workspace with this adjustable desk lamp, providing bright and efficient lighting for late-night study sessions.",
    'Storage Bins': "Stay organized with these stackable storage bins, perfect for storing books, snacks, or any other items you need to keep handy.",
    'Ironing Board': "Look sharp and wrinkle-free with this convenient ironing board, essential for keeping your clothes in top condition.",
    'Alarm Clock': "Never miss an important class or appointment with this reliable and stylish alarm clock.",
    'Extension Cord': "Power all your devices with ease using this durable extension cord, featuring multiple outlets for your convenience.",
    'Toaster': "Make quick and delicious breakfasts with this toaster, perfect for busy mornings before class.",
    'Coffee Machine': "Start your day right with a freshly brewed cup of coffee from this easy-to-use coffee machine.",
    'Waffle Maker': "Satisfy your cravings for waffles with this handy waffle maker, perfect for weekend brunches.",
    'Panini Press': "Make gourmet sandwiches at home with this versatile panini press, ideal for creating delicious and crispy sandwiches.",
    'Toolkit': "Tackle DIY projects and repairs with confidence using our comprehensive toolkit, complete with a variety of essential tools.",
    'Board Games': "Have fun and unwind with our collection of board games, perfect for game nights with friends and roommates.",
    'Nintendo Switch': "Experience the world of gaming with the Nintendo Switch, offering a wide range of games for endless entertainment.",
    'Textbook': "Stay ahead in your classes with this textbook, a valuable resource for your academic success."
}


def generate_fake_supply_info(item_name=None, start_date=None, end_date=None, price=None):
    pictures = ['noimage.jpg']
    if item_name is None:
        item_name = random.choice(list(college_summer_items_descriptions.keys()))
        pictures = [item_name.lower().replace(' ', '') + '.jpg']
    if start_date is None:
        start_date = fake.date_between(start_date=datetime(2023, 5, 1), end_date=datetime(2023, 5, 31))
    if end_date is None:
        end_date = fake.date_between(start_date=datetime(2023, 8, 1), end_date=datetime(2023, 8, 27))
    if price is None:
        price = 5 * fake.random_int(min=1, max=50)

    supply_info = {
        'itemName': item_name,
        'description': college_summer_items_descriptions.get(item_name, "Super useful!"),
        'startDate': start_date,  # Random date within the last 30 days and next 30 days
        'endDate': end_date,  # Random date between 31 and 90 days from now
        'price': price,  # Random price between 10 and 200
        'pictures': pictures,
        'contact': fake.email(),  # Fake email address
        'addlNotes': fake.text()  # Fake additional notes
    }
    return supply_info

def convert_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()

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
        start_date = convert_date(params['startDate'] or '2023-05-15')
        end_date = convert_date(params['endDate'] or '2023-08-15')
        max_price = int(params['maxPrice'] or 500)

        with open('api/college_supplies.json', 'r') as json_file:
            supply_info_list = json.load(json_file)
            for supply_info in supply_info_list:
                supply_info['startDate'] = datetime.strptime(supply_info['startDate'], "%m/%d/%Y").date()
                supply_info['endDate'] = datetime.strptime(supply_info['endDate'], "%m/%d/%Y").date()
        
        matches = []
        for supply_info in supply_info_list:
            if (item_name in ['', supply_info['itemName']]) and \
                supply_info['price'] <= max_price and \
                abs((supply_info['startDate'] - start_date).days) <= 7 and \
                abs((supply_info['endDate'] - end_date).days) <= 7:
                matches.append(supply_info)
        
        if not matches:
            for _ in range(random.randint(1, 3)):
                start = start_date + timedelta(days=random.randint(-3, 3))
                end = end_date + timedelta(days=random.randint(-3, 3))
                matches.append(generate_fake_supply_info(
                    item_name,
                    start,
                    end,
                    max(15, max_price - 5 * random.randint(1, 15))
                    ))
        print(matches)
        return {'itemMatches': convert_matches(matches)}

if __name__ == '__main__':
    print(handler.search({}))