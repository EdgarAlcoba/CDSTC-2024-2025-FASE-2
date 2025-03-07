from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = ""

if __name__ == '__main__':
    app.run(port=5050, host='0.0.0.0')