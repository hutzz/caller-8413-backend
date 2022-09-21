from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)
#app.config.from_object(Config)
app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DATABASE')

from app import routes # access routes.py

load_dotenv()




    