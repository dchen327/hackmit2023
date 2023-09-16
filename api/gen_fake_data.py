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
        'startDate': start_date.strftime("%m/%d/%Y"),  # Random date within the last 30 days and next 30 days
        'endDate': end_date.strftime("%m/%d/%Y"),  # Random date between 31 and 90 days from now
        'price': price,  # Random price between 10 and 200
        'pictures': pictures,
        'contact': fake.email(),  # Fake email address
        'addlNotes': college_summer_items_descriptions.get(item_name, "Super useful!"),
    }
    return supply_info

supply_info_list = [generate_fake_supply_info() for _ in range(100)]


# write to file
FILE_NAME = 'college_supplies.json'
with open(FILE_NAME, 'w') as json_file:
    json.dump(supply_info_list, json_file)