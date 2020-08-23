#
#  layout.py
#  AutoMegaPack
#
#  Created by David Ionita on 8/23/20.
#  Copyright © 2020 David Ionita. All rights reserved.
#
#  Discord: CoollDave#0627
#

import os

start = '{ "content": [\n'
middle = ''
end = '\n]}'

rootdir = "C:/Users/David/Desktop/AutoMegaPack"
basedir = "C:/Users/David/Desktop/AutoMegaPack/Base Files"
submdir = "C:/Users/David/Desktop/AutoMegaPack/Submissions"

baseLayout = open(basedir + "/layout.json", "r")
baseData = baseLayout.read()
middle += baseData

# iterate root
for subdir, dirs, files in os.walk(submdir):

    # iterate each livery submission folder in root
    for dir in dirs:
        submLayout = open(submdir + "/" + dir + "/layouts.json", "r")
        submData = submLayout.read()
        middle += ", \n" + submData

    break

rootLayout = open(rootdir + "/layout.json", "w")
rootData = start + middle + end
rootLayout.write(rootData)
