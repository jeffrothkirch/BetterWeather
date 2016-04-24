import requests
import json

def TagWithOutdoorness(pics):
    url = 'http://localhost:8084/outdoorness'
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    imageUrls = []
    for pic in pics:
        print(pic['imageUrl'])
        imageUrls.append(pic['imageUrl'])
    imageUrls = {'links':imageUrls}
    response = requests.post(url, data=json.dumps(imageUrls), headers=headers)
    print(response.text)
    try:
        outdoorDict = json.loads(response.text)['result'] # {url1: _, url2: _,...}
    except:
        outdoorDict = {}
    for pic in pics:
        if pic['imageUrl'] not in outdoorDict:
            pic['outdoorness'] = 0
            continue
        pic['outdoorness'] = outdoorDict[pic['imageUrl']]
    return pics