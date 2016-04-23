#!flask/bin/python
from flask import Flask, jsonify, abort, json

app = Flask(__name__)


filename = '04_2016_dump.json'
file_information = (open(filename, 'r')).read()
data = json.loads(file_information)


@app.route('/cached/<location>/<start_time>/<end_time>', methods=['GET'])
def get_task(location, start_time, end_time):
    return jsonify(result=data)

@app.route('/')
def examples():
    return "Example:\ncurl -i http://localhost:8081/cached/new_york_city/2016-04-23/2015-04-23\n"


if __name__ == '__main__':
    app.run(host='localhost', port=8081, debug=True)
