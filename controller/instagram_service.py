import requests
import json
from datetime import datetime
import math

def GetInstagramPosts(token):
    data = SendRequest(token)
    return data
    
def FilterInstagramPosts(date, data):
    images = []
    for entry in data['data']:
        if (DatesMatch(date, entry)):
            images.append({'imageUrl':entry['images']['standard_resolution']['url']})
    return images
    
    
def SendRequest(token):
    url = 'http://localhost:8083/api/GetPics'
    response = requests.get(url)
    data = json.loads(response.text)
    print('Got Insta data. Number of total posts: ' + str(len(data['data'])) + '\n')

    return data
    
def DatesMatch(date, entry):
    unixTime = entry['created_time']
    picTime = datetime.fromtimestamp(int(unixTime))
    picDate = datetime.strftime(picTime, '%Y-%d-%m')
    #desiredDate = datetime.strptime(date, '%Y-%d-%m')
    return date == picDate
    