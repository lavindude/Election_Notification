import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import json
import musicalbeeps

AZ_Biden = 0
AZ_Trump = 0

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
                player = musicalbeeps.Player(volume = 0.3, mute_output = False)
                player.play_note("A", 0.2)
                player.play_note("A", 0.2)
        
        elif item['race_id'] == "PA-G-P-2020-11-03":
            if PA_Biden != item['candidates'][0]['votes']:
                print("Biden:", item['candidates'][0]['votes'])
                print("Trump:", item['candidates'][1]['votes'])
                print()
                PA_Biden = item['candidates'][0]['votes']
                PA_Trump = item['candidates'][1]['votes']
                player = musicalbeeps.Player(volume = 0.3, mute_output = False)
                player.play_note("A", 0.2)
                player.play_note("A", 0.2)
    




