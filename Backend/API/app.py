from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
# Variables de entorno

if __name__ == '__main__':
    app.run(port=4040, host='0.0.0.0')