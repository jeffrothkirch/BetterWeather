#!/usr/bin/python
from flask import Flask, jsonify, abort, json, request
import requests
from requests.auth import HTTPDigestAuth
import urllib2, urllib
import os, shutil
import hashlib
import shutil
import os.path
from operator import itemgetter

import os
print os.environ['HOME']

app = Flask(__name__)

BLUEMIX_USERNAME = os.environ['BLUEMIX_USERNAME']
BLUEMIX_PASSWORD = os.environ['BLUEMIX_PASSWORD'] 

output_file_name = 'images'
temp_dir = 'temp'
url = u'https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classify?version=2015-12-02'
nature_words = [ 'Urban_Scene', 'Nature_Scene', 'Water_Scene', 'Winter_Scene', 'Outdoors', 'Sky_Scene', 'Flower', 'Wild_Fire', 'Earthquake', 'Flood', 'Storm', 'Camping', 'Skyline', 'Cliff', 'Desert', 'Field', 'Wheat_Field', 'Flower_scene', 'Forest_Path', 'Forest', 'Greenery', 'Mountain_Scene', 'Mountains', 'Rock_Arch', 'Rock_Formation', 'Coral_Reef', 'Beach', 'Volcano', 'Creek', 'Swamp', 'Waterfall', 'Waterscape', 'Frost', 'Frozen_Waterbody', 'Ice_Scene', 'Iceberg', 'Icicles', 'Snow_Scene', 'Snowy_Mountains', 'Zoo', 'Blue_Sky', 'Gray_Sky', 'Lightning', 'Night_Sky', 'Rainbow', 'Sunset']
nature_set = set([w.lower() for w in nature_words])
threshold = 0.7

@app.route('/cached/<location>/<start_time>/<end_time>', methods=['GET'])
def get_task(location, start_time, end_time):
    return jsonify(result=[1,2,3])

@app.route('/')
def examples():
    return '''Check Credentials:\ncurl -u "$BLUEMIX_USERNAME":"$BLUEMIX_PASSWORD" -X GET "https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classifiers?version=2015-12-02"
    filter: !curl -F "links=[\"https://img.grouponcdn.com/deal/5EXVDNMDEe1mtyEK6Pgp/ZC-1057x634/v1/c700x420.jpg\", \"http://st.hzcdn.com/fimgs/4d8155e104ef5d51_2301-w500-h666-b0-p0--transitional-bedroom.jpg\"]" localhost:8084/filter
    classify: !curl -F "links=[\"https://img.grouponcdn.com/deal/5EXVDNMDEe1mtyEK6Pgp/ZC-1057x634/v1/c700x420.jpg\", \"http://st.hzcdn.com/fimgs/4d8155e104ef5d51_2301-w500-h666-b0-p0--transitional-bedroom.jpg\"]" localhost:8084/classify
    '''

@app.route('/classify', methods=['POST'])
def classify():
    links_string=request.form.getlist('links')
    links = json.loads(links_string)
    data = fetch_data(links)

    return jsonify(result=data)

@app.route('/filter', methods=['POST'])
def filter():
    links_string=request.form.getlist('links')
    links = json.loads(links_string)
    data = fetch_data(links)

    results = []
    for i, link in enumerate(links):
        if (is_outdoors(data['images'][i])):
            link =data['images'][i]['image']
            results.append(link)
    return jsonify(result=results)

@app.route('/outdoorness', methods=['POST'])
def outdoorness():
    links=request.form.getlist('links')
    data = fetch_data(links)

    results = {}
    for i, link in enumerate(links):    
        link = data['images'][i]['image']
        results[link] = calculate_outdoorness(data['images'][i])

    return jsonify(result=results)

def is_outdoors(data_entry):
    # names = ['Outdoors', 'Burning', 'Racquet_Sport', 'Bat_Sport', 'Team_Field_Sport', 'Team_Indoor_Sport', 'Team_Sport', 'Track_and_Field', 'Boating', 'Power_Boating', 'Rowing', 'Swimming', 'Water_Sport', 'Ice_Sport', 'Skiing', 'Snow_Sport', 'Winter_Sport', 'Sports_Field', 'Sports_Track', 'Urban_Scene', 'Nature_Scene', 'Water_Scene', 'Winter_Scene', 'Outdoors', 'Sky_Scene', 'Flower', 'Wild_Fire', 'Earthquake', 'Flood', 'Storm', 'Camping', 'Wedding', 'Concert', 'Adventure_Sport', 'Climbing', 'Land_Sailing', 'Air_Sport', 'Ballooning', 'Hand_Gliding', 'Camel_Racing', 'Dog_Racing', 'Equestrian', 'Horce_Racing', 'Polo', Golf', ;Greco_Roman_Wrestling', 'Mud_Wrestling', 'Cycling', 'Fishing', 'Rollerskating', 'Skateboarding', 'American_Football', 'Football', 'Soccer', 'Rugby', 'Field_Hocky', 'Track', 'Jet_Skiing', 'Crew', 'Sailing', 'Windsurfing', 'Cliff_Diving', 'Sledding', 'Tobagganing', 'Ski_Jumping']
    scores = [(d['classifier_id'], d['score']) for d in data_entry['scores']]
    filtered_scores = [s  for s in scores if s[0].lower() in nature_set and s[1] > 0.6]

    return len(filtered_scores) > 0
    

def delete_folder(path):
    for the_file in os.listdir(path):
        file_path = os.path.join(path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def delete_file(path):
    try:
        os.remove(path)
    except OSError:
        pass

def fetch_data(links):
    # clean everything out
    delete_folder(temp_dir)
    delete_file(output_file_name)

    # download the links
    for i,link in enumerate(links):
        # extension = os.path.splitext(link)[1]
        extension = 'jpg'
        urllib.urlretrieve(link, '%s/%s.%s' % (temp_dir, i, extension))

    # zip the images
    shutil.make_archive(output_file_name, 'zip', temp_dir)

    # make watson requests
    r = requests.post(url, files={'images_file.zip': open(output_file_name + '.zip', 'rb')}, auth=(BLUEMIX_USERNAME, BLUEMIX_PASSWORD))
    

    # massage the data back
    if (r.status_code == 200):
        data = json.loads(r.text)

        for i, link in enumerate(links):
            j = get_index(data['images'], i)
            data['images'][j]['image'] = link

        return data
    # transform them back to links
    abort(403)


def get_index(entry, i):
    for j,e in enumerate(entry):
        if str(e['image']) == "%s.%s" % (i, 'jpg'):
            return j

def is_outdoors(data_entry):
    # names = ['Outdoors', 'Burning', 'Racquet_Sport', 'Bat_Sport', 'Team_Field_Sport', 'Team_Indoor_Sport', 'Team_Sport', 'Track_and_Field', 'Boating', 'Power_Boating', 'Rowing', 'Swimming', 'Water_Sport', 'Ice_Sport', 'Skiing', 'Snow_Sport', 'Winter_Sport', 'Sports_Field', 'Sports_Track', 'Urban_Scene', 'Nature_Scene', 'Water_Scene', 'Winter_Scene', 'Outdoors', 'Sky_Scene', 'Flower', 'Wild_Fire', 'Earthquake', 'Flood', 'Storm', 'Camping', 'Wedding', 'Concert', 'Adventure_Sport', 'Climbing', 'Land_Sailing', 'Air_Sport', 'Ballooning', 'Hand_Gliding', 'Camel_Racing', 'Dog_Racing', 'Equestrian', 'Horce_Racing', 'Polo', Golf', ;Greco_Roman_Wrestling', 'Mud_Wrestling', 'Cycling', 'Fishing', 'Rollerskating', 'Skateboarding', 'American_Football', 'Football', 'Soccer', 'Rugby', 'Field_Hocky', 'Track', 'Jet_Skiing', 'Crew', 'Sailing', 'Windsurfing', 'Cliff_Diving', 'Sledding', 'Tobagganing', 'Ski_Jumping']
    if ('scores' in data_entry):
        scores = [(d['classifier_id'], d['score']) for d in data_entry['scores']]
        filtered_scores = [s  for s in scores if s[0].lower() in nature_set and s[1] > 0.6]

        return len(filtered_scores) > 0
    return False
    
def calculate_outdoorness(data_entry):
    if ('scores' in data_entry):
        scores = [(d['classifier_id'], d['score']) for d in data_entry['scores']]
        filtered_scores = [s  for s in scores if s[0].lower() in nature_set]

        if len(filtered_scores) == 0:
            return 0.0
        return max([f[1] for f in filtered_scores])
    return 0.0

def delete_folder(path):
    for the_file in os.listdir(path):
        file_path = os.path.join(path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def delete_file(path):
    try:
        os.remove(path)
    except OSError:
        pass

if __name__ == '__main__':
    app.run(host='localhost', port=8084, debug=True)
