import datetime        
import math
 
 
 
descriptDict = {
'sunny':{'sunniness':1, 'precipitation':0, 'fluffiness':0, 'wetness':0},
        'partially sunny':{'sunniness':.7, 'precipitation':0, 'fluffiness':0, 'wetness':0},
        'partially cloudy':{'sunniness':4, 'precipitation':0, 'fluffiness':0, 'wetness':0},
        'cloudy':{'sunniness':.1, 'precipitation':0, 'fluffiness':0, 'wetness':0},
        'overcast':{'sunniness':0, 'precipitation':0, 'fluffiness':0, 'wetness':0},
        'drizzle':{'sunniness':.1, 'precipitation':.2, 'fluffiness':0.5, 'wetness':1},
        'showers':{'sunniness':.2, 'precipitation':.1, 'fluffiness':.5, 'wetness':1},
        'light rain':{'sunniness':.1, 'precipitation':.5, 'fluffiness':.5, 'wetness':1},
        'rain':{'sunniness':0, 'precipitation':.8, 'fluffiness':.5, 'wetness':1},
        'heavy rain':{'sunniness':0, 'precipitation':1, 'fluffiness':.5, 'wetness':1},
        'flurries':{'sunniness':.2, 'precipitation':.1, 'fluffiness':1, 'wetness':0},
        'light snow':{'sunniness':.1, 'precipitation':.3, 'fluffiness':1, 'wetness':0},
        'snow':{'sunniness':0, 'precipitation':0.8, 'fluffiness':1, 'wetness':0},                                                 
        'heavy snow':{'sunniness':0, 'precipitation':1, 'fluffiness':1, 'wetness':0},                                             
        'blizzard':{'sunniness':0, 'precipitation':.1, 'fluffiness':1, 'wetness':0},                                              
        'hail':{'sunniness':.1, 'precipitation':1, 'fluffiness':0, 'wetness':0},                                                  
        'sleet':{'sunniness':.2, 'precipitation':.5, 'fluffiness':.5, 'wetness':.5},                                              
        'wintery mix':{'sunniness':.1, 'precipitation':.5, 'fluffiness':.4, 'wetness':.8}                                         
}                                                                                                                                     
categories = ['sunniness', 'precipitation', 'fluffiness', 'wetness']                                                                  
                                                                                                                                      
                                                                                                                                      
def RankDates(currentDateWeather, historicalWeather):                                                                                 
    for historicalEntry in historicalWeather:                                                                                         
        historicalEntry['closeness'] = compare_dates(currentDateWeather, historicalEntry)                                             
    return sorted(historicalWeather, key = lambda entry : entry['closeness'])                                                         
                                                                                                                                      
                                                                                                                                      
def compare_dates(currentDateWeather, otherDate):                                                                                     
    descript_weight = 0.5    
    cloud_weight = 0.1
    temp_weight = 0.5
    precipitation_weight = 10
    
    curHigh = currentDateWeather['high']
    curLow = currentDateWeather['low']
    curDesc = currentDateWeather['descriptor']
    curPrecip = currentDateWeather['precipitation']
    curClouds = currentDateWeather['cloudcover']
    oldLow = otherDate['low']
    oldHigh = otherDate['high']
    oldDesc = otherDate['descriptor']
    oldPrecip = otherDate['precipitation']
    oldClouds = currentDateWeather['cloudcover']
 
    dist = get_squared_dist(curHigh,oldHigh) * temp_weight
    dist += get_squared_dist(curLow, oldLow) * temp_weight
    dist += get_squared_dist(curClouds, oldClouds) * cloud_weight 
    dist += get_squared_dist(curPrecip, oldPrecip) * precipitation_weight
    dist += get_descript_dist(curDesc, oldDesc) * descript_weight
    return math.sqrt(dist)



def get_squared_dist(value1, value2):
    return math.pow(value1 - value2, 2)

def get_descript_dist(descriptor1, descriptor2):
    descriptor2 = str.lower(descriptor2.encode('ASCII', 'ignore'))
    descriptor1 = str.lower(descriptor1.encode('ASCII', 'ignore'))
    if descriptor1 not in descriptDict and descriptor2 not in descriptDict:
        return 0
    if descriptor1 not in descriptDict or descriptor2 not in descriptDict:
        return 1
    val1 = descriptDict[descriptor1]
    val2 = descriptDict[descriptor2]
    dist = get_descript_dist_sub(val1, val2, 'sunniness')
    dist += get_descript_dist_sub(val1, val2, 'precipitation')
    dist += get_descript_dist_sub(val1, val2, 'fluffiness')
    dist += get_descript_dist_sub(val1, val2, 'wetness')
    return dist

def get_descript_dist_sub(entry1, entry2, category):
    return get_squared_dist(entry1[category], entry2[category])  