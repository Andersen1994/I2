from flask import Flask
import os
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)

@app.route('/')
def hello_world():
    config = get_config()
    secret = get_secret()
    return f'Hello, World!\n {config}\n {secret}'

def get_config():
    try:
        load_dotenv(find_dotenv())
        config = os.environ.get('CUSTOM_CONFIG')
        return f'config: {config}'
    except Exception as inst:
        print(inst)
        return 'config not found!'

def get_secret():
    try:
        load_dotenv(find_dotenv())
        config = os.environ.get('CUSTOM_SECRET')
        return f'secret: {config}'
    except Exception as inst:
        print(inst)
        return 'config not found!'