#
#  aircraft.py
#  AutoMegaPack
#
#  Created by CoollDave#0627 on 8/23/20.
#  Copyright (c) 2020 CoollDave#0627. All rights reserved.
#
#  Discord: CoollDave#0627
#

import os
import re

data = ''

rootdir = os.path.dirname(os.path.abspath(__file__))
basedir = rootdir + "/Base Files"
submdir = rootdir + "/Submissions"

baseAircraft = open(basedir + "/aircraft.cfg", "r")
baseData = baseAircraft.read()
data += baseData

finalStr = re.findall('\[FLTSIM\.\d\]', data)[-1]
finalNumArr = [int(s) for s in list(finalStr) if s.isdigit()]
num = int(''.join([str(x) for x in finalNumArr]))

def iterPercent(matchobj):
    global num
    num += 1
    if matchobj.group(0) == '[FLTSIM.%]':
        return '[FLTSIM.' + str(num) + ']'
    else:
        return '[FLTSIM.%]'

# iterate root
for subdir, dirs, files in os.walk(submdir):

    # iterate each livery submission folder in root
    for dir in dirs:
        submAircraft = open(submdir + "/" + dir + "/aircraft.cfg", "r")
        submData = submAircraft.read()

        new_submData = re.sub(r'\[FLTSIM\.%\]', iterPercent, submData)
        data += "\n" + new_submData + "\n"

    break

rootLayout = open(rootdir + "/aircraft.cfg", "w")
rootData = data
rootLayout.write(rootData)
