#! bin/sh
import fileinput
import csv
import json

def shape_data(dimensions, row):
    obj = {}

    for i, dim in enumerate(dimensions):
        obj[dim.strip()] = row[i]

    return obj


def transform_element(string):
    return string.strip().lower().replace(' ', '_')

def transform_header(header):
    custom_header = [custom_mapping.get(h) if custom_mapping.get(h) else h for h in header]
    lower_case_header = [transform_element(x) for x in custom_header]
    return lower_case_header

def transform_csv_to_object(filename):
    csvfile = open(filename, 'rb')
    csvreader = csv.reader(csvfile, delimiter=',')
    header = csvreader.next()
    transformed_header = transform_header(header)
    line_data = [line for line in csvreader]
    shaped_data = [shape_data(transformed_header, line) for line in line_data]
    return shaped_data

def main():
    filename='April2016.csv'

    custom_mapping = {
        'EDT' : 'date'
    }

    shaped_data = transform_csv_to_object(filename)

    print json.dumps(shaped_data, sort_keys=True,
                indent=4, separators=(',', ': '))

if __name__ == '__main__':
    main()