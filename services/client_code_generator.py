from app import db
from models.client import Client
import string

def generate_client_code(name):
    cleaned = ''.join(filter(str.isalpha, name.upper()))

    prefix = cleaned[:3]

    if len(prefix) < 3:
        for char in string.ascii_uppercase:
            if len(prefix) == 3:
                break
            prefix += char

    existing = Client.query.filter(Client.client_code.like(f"{prefix}%")).all()

    numbers = []
    for client in existing:
        numbers.append(int(client.client_code[3:]))

    next_number = 1 if not numbers else max(numbers) + 1

    return f"{prefix}{str(next_number).zfill(3)}"
