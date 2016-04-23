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

if __name__ == '__main__':
    main()
