#
#  layout.py
#  AutoMegaPack
#
#  Created by CoollDave#0627 on 8/23/20.
#  Copyright (c) 2020 CoollDave#0627. All rights reserved.
#
#  Discord: CoollDave#0627
#

import os

start = '{ "content": [\n'
middle = ''
end = '\n]}'

rootdir = os.path.dirname(os.path.abspath(__file__))
basedir = rootdir + "/Base Files"
submdir = rootdir + "/Submissions"

baseLayout = open(basedir + "/layout.json", "r")
baseData = baseLayout.read()
middle += baseData

# iterate root
for subdir, dirs, files in os.walk(submdir):

    # iterate each livery submission folder in root
    for dir in dirs:
        submLayout = open(submdir + "/" + dir + "/layout.json", "r")
        submData = submLayout.read()
        middle += ", \n" + submData

    break

rootLayout = open(rootdir + "/layout.json", "w")
rootData = start + middle + end
rootLayout.write(rootData)
