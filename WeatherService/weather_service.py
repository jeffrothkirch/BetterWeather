#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

data = [
    {
        'zip_code': '11729',
        'date' : '2008-10-30',
        'temperature_F': 84.3,
        'description': u'sunny', 
    },
    {
        'zip_code': '08544',
        'date' : '2008-10-30',
        'temperature_F': 84.3,
        'description': u'sunny', 
    }
]

@app.route('/<zip_code>/<date>', methods=['GET'])
def get_task(zip_code):
    matching_data = [d for d in data if data['zip_code'] == zip_code]
    if len(matching_data) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/')
def examples():
    return "Example:\ncurl -i http://localhost:8081/todo/api/v1.0/tasks/1\n"

def invalid_argument()
if __name__ == '__main__':
    app.run(host='localhost', port=8081, debug=True)