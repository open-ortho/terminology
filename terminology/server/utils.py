import os

def generate_new_flask_secret_key():
    return os.urandom(24).hex()