# coding=utf-8
from flask import *
import json, data

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
	dict = {"Page": "Main", "Status": "Loaded successfully"}

	return json.dumps(dict)

@app.route("/website", methods=['GET'])
def website():
	dict = {"Page": "Website", "Status": "Loaded successfully"}

	return json.dumps(dict)

@app.route("/duaa/", methods=['GET'])
def azan():
	dict = data.duaa_list
	return json.dumps(dict)

@app.route("/monajat/", methods=['GET'])
def monajat():
	dict = data.monajat_list
	return json.dumps(dict)

@app.route("/duaa/<duaa_id>", methods=['GET'])
def duaas(duaa_id):
	dict = data.duaa_list["duaa"][str(duaa_id)]
	return json.dumps(dict)

@app.route("/monajat/<monajat_id>", methods=['GET'])
def monajats(monajat_id):
	dict = data.monajat_list["monajat"][str(monajat_id)]
	return json.dumps(dict)

@app.route("/days-prayers/", methods=['GET'])
def days_prayers():
	dict = data.days_prayers
	return json.dumps(dict)

@app.route("/days-prayers/<day_id>", methods=['GET'])
def day_prayers(day_id):
	dict = data.days_prayers["daysprayers"][day_id]
	return json.dumps(dict)

@app.route("/taqeebat/", methods=['GET'])
def taqeebat():
	dict = data.taqeebat
	return json.dumps(dict)

@app.route("/taqeebat/<taqeebat_id>", methods=['GET'])
def taqeebats(taqeebat_id):
	dict = data.taqeebat["taqeebat"][taqeebat_id]
	return json.dumps(dict)

@app.route("/salawat/", methods=['GET'])
def salawat():
	dict = data.salawat
	return json.dumps(dict)

@app.route("/salawat/<salawat_id>", methods=['GET'])
def salawats(salawat_id):
	dict = data.salawat["salawat"][salawat_id]
	return json.dumps(dict)

@app.route("/ramadan/", methods=['GET'])
def ramadan():
	dict = data.ramadan
	return json.dumps(dict)

@app.route("/ramadan/<ramadan_day>", methods=['GET'])
def ramadans(ramadan_day):
	dict = data.ramadan["ramadan"][ramadan_day]
	return json.dumps(dict)

@app.route("/ziyarat/", methods=['GET'])
def ziyarat():
	dict = data.ziyarat
	return json.dumps(dict)

@app.route("/ziyarat/<ziyarat_id>", methods=['GET'])
def ziyarats(ziyarat_id):
	dict = data.ziyarat["ziyarat"][ziyarat_id]
	return json.dumps(dict)

app.run(port=5555)