#!/usr/bin/python
import fileinput
import csv
import json
import time
from os import listdir


def shape_data(dimensions, row):
    obj = {}

    for i, dim in enumerate(dimensions):
        obj[dim.strip()] = row[i]

    return obj

def transform_element(string):
    return string.strip().lower().replace(' ', '_')

def transform_header(header):
    custom_mapping = {
        'EDT' : 'date',
        'EST' : 'date'
    }
    
    custom_header = [custom_mapping.get(h) if custom_mapping.get(h) else h for h in header]
    lower_case_header = [transform_element(x) for x in custom_header]
    return lower_case_header

def get_descriptor(data_entry):
    event_value = data_entry['events']
    
    mapping = {'Fog' : 'overcast',
               'Fog-Rain' : 'raining',
               'Fog-Rain-Snow' :'raining-snowing',
               'Fog-Snow' : 'snowing',
               'Rain' : 'raining',
               'Rain-Snow' : 'raining-snowing',
               'Snow' : 'snowing',
               'Thunderstorm' : 'thunder'
            }      

    thunder_raining_threshold = 0.3

    value = mapping.get(event_value,'')

    if value:
        return value

    if value == 'thunder':
        if is_number(data_entry['precipitationin']) and float(data_entry['precipitationin']) < thunder_raining_threshold:
            value = 'thunder'
        else:
            value = 'thunder-raining'

    if value  == '':
        if is_number(data_entry['precipitationin']) and float(data_entry['precipitationin']) > 0.2:
            value = 'raining'
        elif is_number(data_entry['mean_wind_speedmph']) and float(data_entry['mean_wind_speedmph']) > 8.0:
            value = 'very-windy'
        elif is_number(data_entry['cloudcover']) and float(data_entry['cloudcover']) > 6:
            value = 'overcast'
        elif is_number(data_entry['cloudcover']) and float(data_entry['cloudcover']) >= 3: 
            value = 'sunny-cloudy'
        else:
            value = 'sunny'

    return value

def shape_descriptors(data_entry):
    data_entry['events'] = get_descriptor(data_entry)
    return data_entry

def transform_csv_to_object(filename):
    csvfile = open(filename, 'rb')
    csvreader = csv.reader(csvfile, delimiter=',')
    header = csvreader.next()

    if len(header) == 0:
        raise Exception("Cannot find headers in file:%s" % filename)

    transformed_header = transform_header(header)
    line_data = [line for line in csvreader]
    raw_data = [shape_data(transformed_header, line) for line in line_data]

    data = [transform_date_field(d) for d in raw_data]
    data = [shape_descriptors(d) for d in raw_data]
    return data

def transform_date_field(data_entry):    
    date_value = data_entry['date']
    
    parsed_time = time.strptime(date_value, "%Y-%m-%d")
    formmated_time = time.strftime("%Y-%m-%d", parsed_time)
    data_entry['date'] = formmated_time
    return data_entry

def main():
    targetdir = 'csv'

    all_data = []
    for file in listdir(targetdir):
        filename = "%s/%s" % (targetdir, file)
        shaped_data = transform_csv_to_object(filename)
        all_data.extend(shaped_data)

    print json.dumps(all_data, sort_keys=True, indent=4, separators=(',', ': '))    

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
if __name__ == '__main__':
    main()
