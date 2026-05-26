from flask import Flask, jsonify
from pymongo import MongoClient
import os
import psycopg2
from datetime import datetime

app = Flask(__name__)

POSTGRES_URL = os.environ.get('POSTGRES_URL')
MONGO_URL = os.environ.get('MONGO_URL')

def get_pg_connection():
	return psycopg2.connect(POSTGRES_URL)

def get_mongo_db():
	client = MongoClient(MONGO_URL)
	return client["weatherdb"]

@app.route('/weather/<city>')
def get_weather(city):
	conn = get_pg_connection()
	cur = conn.cursor()
	cur.execute("SELECT temperature, condition FROM weather WHERE city = %s", (city,))
	row = cur.fetchone()
	conn.close()

	if not row:
		return jsonify({"error": "city not found"}), 404
	
	temperature, condition = row

	db = get_mongo_db()
	db.request_logs.insert_one({
		"city": city,
		"timestamp": datetime.now(),
		"result": condition
	})

	return jsonify({"city": city, "temperature": temperature, "condition": condition})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)

#helloworld 
#hmminteresting