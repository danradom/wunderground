import urllib2
import json
import sys
import os


zipcode = sys.argv[1]
periods = int(sys.argv[2])
key = "YOUR_API_KEY"


url = urllib2.urlopen('http://api.wunderground.com/api/' + key + '/forecast10day/q/' + zipcode + '.json')
json_string = url.read()
url.close()
parsed_json = json.loads(json_string)
forecast = parsed_json['forecast']['simpleforecast']['forecastday']
weather = parsed_json['forecast']['txt_forecast']['forecastday']


periods = min(periods,len(forecast))
days = (periods/2)

print "%d day forecast for %s: \n\n" % (days, zipcode)

for i in range(periods):
        period = str(weather[i]['title'])
        temp_low = int(forecast[i]['low']['fahrenheit'])
        temp_high = int(forecast[i]['high']['fahrenheit'])
        cond = str(forecast[i]['conditions'])
       rain_chance = int(forecast[i]['pop'])
        precipitation = str(forecast[i]['qpf_allday']['in'])
        details = str(weather[i]['fcttext'])

        print "%s:  %s" % (period, cond)
        print "low:  %sF " % temp_low
        print "high:  %sF " % temp_high
       print "chance of rain:  %s%%" % rain_chance
       if rain_chance > 0:
               print "precipitation amount:  %s inches" % precipitation
        print "forecast:  %s" % details

        print "\n"
