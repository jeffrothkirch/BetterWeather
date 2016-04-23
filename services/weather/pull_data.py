#!/usr/bin/python 
import urllib2
import datetime
from datetime import timedelta

'''
    ./pull_data.py

    pulls the data for the months specified and the target year.
'''

def calculate_pull_dates(start_date, end_date):

    dates = []

    for year in range(start_date.year, end_date.year+1):
        for month in range(1,13):
            dates.append(datetime.date(year, month, end_date.day))

    dates_in_range = [d for d in dates if (d >= start_date and d <= end_date)]
    return dates_in_range


months = range(1,13)
year = 2016
dummy_day = 23

write_dir = 'csv'

start_date = datetime.date(2015, 4, 23)
end_date = datetime.date(2016, 4, 23)

foo = raw_input("Pulling data from %s to %s. Press any key to continue." % (start_date, end_date))

#https://www.wunderground.com/history/airport/KNYC/2016/4/23/MonthlyHistory.html?req_city=New%20York&req_state=NY&req_statename=New%20York&reqdb.zip=10001&reqdb.magic=5&reqdb.wmo=99999&MR=1&format=1
base_url = "https://www.wunderground.com/history/airport/KNYC/%s/%s/%s/MonthlyHistory.html?req_city=New%%20York&req_state=NY&req_statename=New%%20York&reqdb.zip=10001&reqdb.magic=5&reqdb.wmo=99999&MR=1&format=1"
pull_dates = calculate_pull_dates(start_date, end_date)

for date in pull_dates:
    url = base_url % (date.year, date.month, date.day)
    page = urllib2.urlopen(url)

    filename = "%02d_%02d.csv" % (date.year, date.month)
    f_handle = open("%s/%s" % (write_dir, filename), "w+")
    data = page.read().strip()
    num_rows = len(data.split("\n"))-1

    f_handle.write(data)
    f_handle.close()

    print "Read Page. NumRows=%s, Code=%s, URL=%s" % (num_rows, page.getcode(), url)

print 'Done reading data'
