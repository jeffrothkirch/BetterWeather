from weather_service import GetWeather, GetSimilarDates
from emotion_service import AnalyzeEmotions
from outdoorness_service import TagWithOutdoorness
from instagram_service import GetInstagramPosts, FilterInstagramPosts
import json


def GetAllMyShit(location, date, token, search_size, num_dates):
    current_weather = GetWeather(location, date)
    top_dates = GetSimilarDates(location, search_size, date)
    top_dates = GetInstaPosts(top_dates, token)
    returnDates = []
    for i in xrange(0,num_dates):
        returnDates.append(top_dates[i])
    returnPics = []
    for date in top_dates:
        if len(date['images']) != 0:
            returnPics.append(date)
    
    emotionalContent = GetEmotionalContent(returnPics)
        
    blob = {'weatherInfo':returnDates, 'emotionalContent':emotionalContent, 'images':returnPics}
    return blob
    
    
def GetInstaPosts(weather_details, token):
    posts = GetInstagramPosts(token)
    pics = []
    for detail in weather_details:
        date = detail['date']
        daysPics = FilterInstagramPosts(date, posts)
        if len(daysPics) == 0:
            detail['images'] = []
            continue
        print(json.dumps(daysPics))
        daysPics = SortByOutdoors(daysPics)
        detail['images'] = daysPics
        pics.append(daysPics)
        print('Found Insta posts: \n' + json.dumps(daysPics))
    return weather_details
    
    
def SortByOutdoors(pics):
    taggedPics = TagWithOutdoorness(pics)
    return sorted(taggedPics, key=lambda x: x['outdoorness'], reverse=True)
    
    
def GetEmotionalContent(datePics):
    allEmotions = []
    for entry in datePics:
        for pic in entry['images']:
            emotions = AnalyzeEmotions(pic['imageUrl'])
            pic['emotionalContent'] =  emotions
            allEmotions.append(emotions)
    averageDict = {}
    print('Found emotional content: \n' + json.dumps(allEmotions))
    for emotions in allEmotions:
        for key in emotions.keys():
            if key in averageDict.keys():
                averageDict[key]['value'] += emotions[key]
                averageDict[key]['number'] += 1
            else:
                averageDict[key] = {'value':emotions[key], 'number':1}
    for key in averageDict.keys():
        averageDict[key]['value'] /= averageDict[key]['number']
    return averageDict