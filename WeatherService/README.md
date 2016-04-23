Weather Application
========

To start this service:

`python weather_service.py`

Then to get instructions:

`curl localhost:8081`

To use the API:

`curl -i http://localhost:8081/cached/new_york_city/2016-04-23/2015-04-23`

Example of returned data:
```
{
  "result": [
    {
      "cloudcover": "6",
      "date": "2016-4-1",
      "events": "Rain",
      "max_dew_pointf": "58",
      "max_gust_speedmph": "30",
      "max_humidity": "78",
      "max_sea_level_pressurein": "29.76",
      "max_temperaturef": "79",
      "max_visibilitymiles": "10",
      "max_wind_speedmph": "12",
      "mean_humidity": "61",
      "mean_sea_level_pressurein": "29.61",
      "mean_temperaturef": "70",
      "mean_visibilitymiles": "10",
      "mean_wind_speedmph": "7",
      "meandew_pointf": "55",
      "min_dewpointf": "43",
      "min_humidity": "43",
      "min_sea_level_pressurein": "29.46",
      "min_temperaturef": "61",
      "min_visibilitymiles": "8",
      "precipitationin": "0.01",
      "winddirdegrees": "217"
    },
    {
      "cloudcover": "7",
      "date": "2016-4-2",
      "events": "Rain",
      "max_dew_pointf": "45",
      "max_gust_speedmph": "20",
      "max_humidity": "80",
      "max_sea_level_pressurein": "29.65",
      "max_temperaturef": "61",
      "max_visibilitymiles": "10",
      "max_wind_speedmph": "9",
      "mean_humidity": "63",
      "mean_sea_level_pressurein": "29.54",
      "mean_temperaturef": "55",
      "mean_visibilitymiles": "10",
      "mean_wind_speedmph": "5",
      "meandew_pointf": "42",
      "min_dewpointf": "37",
      "min_humidity": "46",
      "min_sea_level_pressurein": "29.35",
      "min_temperaturef": "49",
      "min_visibilitymiles": "4",
      "precipitationin": "0.15",
      "winddirdegrees": "67"
    }
  ]
```

