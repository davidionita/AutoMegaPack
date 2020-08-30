#
#  hider.py
#  AutoMegaPack for use in MSFS Livery Mega Pack
#
#  Created by CoollDave#0627 on 8/25/20.
#  Copyright (c) 2020 CoollDave#0627. All rights reserved.
#
#  Discord: CoollDave#0627
#

import os
import configparser
import json

rootdir = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config.optionxform = str

for subdir, dirs, files in os.walk(rootdir):

    if ('hider.json' not in files):
        aircraft = open('aircraft.cfg', 'r')
        hider = open('hider.json', 'w+')

        config.read_file(aircraft)
        data = {}
        
        for section in config.sections():
            if (section.startswith("FLTSIM.")):
                title = config.get(section, 'title')
                i = title.find(";")
                title = title[:i-1].strip('"')
                
                numArr = [int(s) for s in list(section) if s.isdigit()]
                num = int(''.join([str(t) for t in numArr]))

                isUserSelectable = config.get(section, 'isUserSelectable')
                i = isUserSelectable.find(";")
                isUserSelectable = int(isUserSelectable[:i-1])

                required = False
                if (num == 0) or (isUserSelectable == 0):
                    required = True

                data[title] = {
                    "num":num,
                    "selected":True, # on by default
                    "required":required
                }

        hider.write(json.dumps(data))

        hider.close()
        aircraft.close()

    break

# -------- Below here is not finished yet, mostly just sample code to finish after the GUI is done

# How to access json object data --- to set json object data, edit the Python dictionary then `hider.write(json.dumps(data))`
hider = open('hider.json', 'r')
hiderData = hider.read()
hider.close()

# Set JSON 'selected' based on checkbox results
checkboxResults={"Airbus A320 Neo Asobo":True, "Airbus A320 Neo Asobo AirTraffic 00":False} # TODO: Get checkbox results dictionary
data = json.loads(hiderData)
for key, value in data.items():
    value['selected'] = checkboxResults[key]

hider = open('hider.json', 'w')
hider.write(json.dumps(data))
hider.close()

# Set CFG 'isUserSelectable' from JSON
with open('aircraft.cfg', 'r') as aircraft:
    config.read_file(aircraft)

for key, value in data.items():
    config.set('FLTSIM.' + str(data[key]["num"]), 'isUserSelectable', int(data[key]["selected"]))

with open('aircraft.cfg', 'w') as aircraft:
    config.write(aircraft)

# Make sure to normalize data (change selected data in both locations) across both aircraft.cfg and hider.json
