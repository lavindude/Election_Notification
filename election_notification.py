import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import json
from win10toast import ToastNotifier

toaster = ToastNotifier()

AZ_Biden = 0
AZ_Trump = 0

GA_Biden = 0
GA_Trump = 0

NV_Biden = 0
NV_Trump = 0

NC_Biden = 0
NC_Trump = 0

PA_Biden = 0
PA_Trump = 0

while True:
    text = urllib.request.urlopen('https://raw.githubusercontent.com/alex/nyt-2020-election-scraper/master/results.json').read()
    jsonStateData = json.loads(text)

    states_data = jsonStateData['data']['races']

    for item in states_data:
        if item['race_id'] == "AZ-G-P-2020-11-03":
            if AZ_Biden != item['candidates'][0]['votes']:
                print("Arizona:")
                print("Biden:", item['candidates'][0]['votes'])
                print("Trump:", item['candidates'][1]['votes'])
                print()
                AZ_Biden = item['candidates'][0]['votes']
                AZ_Trump = item['candidates'][1]['votes']
                concatenated = "Biden: " + str(item['candidates'][0]['votes']) + "   Trump: " + str(item['candidates'][1]['votes'])
                toaster.show_toast("Arizona:", concatenated)
        
        elif item['race_id'] == "PA-G-P-2020-11-03":
            if PA_Biden != item['candidates'][0]['votes']:
                print("Pennsylvania:")
                print("Biden:", item['candidates'][0]['votes'])
                print("Trump:", item['candidates'][1]['votes'])
                print()
                PA_Biden = item['candidates'][0]['votes']
                PA_Trump = item['candidates'][1]['votes']
                concatenated = "Biden: " + str(item['candidates'][0]['votes']) + "   Trump: " + str(item['candidates'][1]['votes'])
                toaster.show_toast("Pennsylvania:", concatenated)

        elif item['race_id'] == "GA-G-P-2020-11-03":
            if GA_Biden != item['candidates'][0]['votes']:
                print("Georgia:")
                print("Biden:", item['candidates'][0]['votes'])
                print("Trump:", item['candidates'][1]['votes'])
                print()
                GA_Biden = item['candidates'][0]['votes']
                GA_Trump = item['candidates'][1]['votes']
                concatenated = "Biden: " + str(item['candidates'][0]['votes']) + "   Trump: " + str(item['candidates'][1]['votes'])
                toaster.show_toast("Georgia:", concatenated)

        elif item['race_id'] == "NV-G-P-2020-11-03":
            if NV_Biden != item['candidates'][0]['votes']:
                print("Nevada:")
                print("Biden:", item['candidates'][0]['votes'])
                print("Trump:", item['candidates'][1]['votes'])
                print()
                NV_Biden = item['candidates'][0]['votes']
                NV_Trump = item['candidates'][1]['votes']
                concatenated = "Biden: " + str(item['candidates'][0]['votes']) + "   Trump: " + str(item['candidates'][1]['votes'])
                toaster.show_toast("Nevada:", concatenated)

        elif item['race_id'] == "NC-G-P-2020-11-03":
            if NC_Biden != item['candidates'][0]['votes']:
                print("North Carolina:")
                print("Biden:", item['candidates'][0]['votes'])
                print("Trump:", item['candidates'][1]['votes'])
                print()
                NC_Biden = item['candidates'][0]['votes']
                NC_Trump = item['candidates'][1]['votes']
                concatenated = "Biden: " + str(item['candidates'][0]['votes']) + "   Trump: " + str(item['candidates'][1]['votes'])
                toaster.show_toast("North Carolina:", concatenated)
    




