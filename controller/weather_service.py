import datetime
import urllib2
import json
import weather_logic

WeatherServicePort = 8081

def ToString(date):
    return date.strftime('%Y-%m-%d')
def fromString(dateString):
    return datetime.datetime.strptime(dateString, '%Y-%m-%d')
    
def GetWeather(location, dateString):
    allDates = get_all_dates(location, dateString)
    for dateEntry in allDates:
        if dateEntry['date'] == dateString:
            return dateEntry
    return None

def GetSimilarDates(location, numDates, compareDateString):
    allDates = get_all_dates(location, compareDateString)
    compareDateDetails = GetWeather(location, compareDateString)
    rankedDates = weather_logic.RankDates(compareDateDetails, allDates)
    return rankedDates[:numDates]
    
def GetPastForDate(location, desiredDate, desiredDelta):
    details = get_all_dates(location, desiredDate)
    returnValues = []
    desiredDateDate = fromString(desiredDate)
    endDateDate = desiredDateDate - desiredDelta
    for dateEntry in details:
        pastDateString = dateEntry['date']
        pastDate = fromString(pastDateString)
        if (pastDateString[5:] == desiredDate[5:] and pastDate > endDateDate):
            returnValues.append(dateEntry)
    return returnValues

def get_all_dates(location, datestring):
    url = 'http://localhost:8081/cached/'+location+'/'+datestring+'/'+datestring
    r = urllib2.urlopen(url).read() 
    allDates = convert_to_desired(json.loads(r))
    return allDates
    

def convert_to_desired(response):
    convertedEntries = []
    oldFormat = response['result']
    for date in oldFormat:
        converted = {}
        converted['date'] = date['date']
        converted['descriptor'] = date['events']
        converted['low'] = tryfloat(date['min_temperaturef'])
        converted['high'] = tryfloat(date['max_temperaturef'])
        converted['precipitation'] = tryfloat(date['precipitationin'])
        converted['cloudcover'] = tryfloat(date['cloudcover'])
        convertedEntries.append(converted)
    return convertedEntries

def tryfloat(value):
    try:
        return float(value)
    except ValueError:
        return 0

