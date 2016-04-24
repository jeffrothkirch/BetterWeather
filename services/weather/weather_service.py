#!/usr/bin/python
from flask import Flask, jsonify, abort, json

app = Flask(__name__)


filename5 = 'data.json'
filename12 = 'all_data.json'

file_information5 = (open(filename5, 'r')).read().replace( '\x00', '' )
year5_data = json.loads(file_information5)
file_information12 = (open(filename12, 'r')).read().replace( '\x00', '' )
year12_data = json.loads(file_information12)


@app.route('/cached/<location>/<start_time>/<end_time>', methods=['GET'])
def get_task(location, start_time, end_time):
    return jsonify(result=year5_data)

@app.route('/all/<location>/<start_time>/<end_time>', methods=['GET'])
def get_all(location, start_time, end_time):
    return jsonify(result=year12_data)

@app.route('/')
def examples():
    return "Example:\ncurl -i http://localhost:8081/cached/new_york_city/2016-04-23/2015-04-23\n"


if __name__ == '__main__':
    app.run(host='localhost', port=8081, debug=True)
