from flask import Flask, jsonify
from pymongo import MongoClient
import os
import psycopg2
from datetime import datetime

app = Flask(__name__)

@app.route('/weather/<city>')
def get_weather(city):
	return jsonify({"city": city, "temperature": 22, "condition": "sunny"})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)

