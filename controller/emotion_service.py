import requests
import json


def AnalyzeEmotions(imageUrl):
    url = 'http://localhost:8082/cognitive/SendImage'
    emotionOutputs = []
    r = requests.post(url, data={'imageUrl':imageUrl})
    data = json.loads(r.text)
    for rectangle in data:
        emotionOutputs.append(rectangle['scores'])
    averageEmotions = {}
    for emotions in emotionOutputs:
        for key in emotions.keys():
            if key in averageEmotions.keys():
                averageEmotions[key]['value'] += emotions[key]
                averageEmotions[key]['number'] += 1 
            else:
                averageEmotions[key] = {'value':emotions[key],'number':1}
    for key in averageEmotions.keys():
        averageEmotions[key] = averageEmotions[key]['value'] / averageEmotions[key]['number']
    return averageEmotions