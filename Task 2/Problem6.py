import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))
    return password

print("Random password:", generate_password())
