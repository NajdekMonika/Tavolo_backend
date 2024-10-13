import string
import random
import json

def generate_random_key(length=6):
        characters = string.ascii_letters + string.digits  # Includes both letters and numbers
        random_key = ''.join(random.choice(characters) for _ in range(length))
        return random_key

def json_to_dict(json):
        with open(json) as file:
            data = json.load(file)
        return data