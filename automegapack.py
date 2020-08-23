#
#  automegapack.py
#  AutoMegaPack
#
#  Created by CoollDave#0627 on 8/23/20.
#  Copyright (c) 2020 CoollDave#0627. All rights reserved.
#
#  Discord: CoollDave#0627
#

# Put this file in the folder that houses all aircrafts
# Make sure that folder only contains subfolders that are in the AutoMegaPack organizational system
# subprocess may cause an antivirus detection - this is NORMAL as it is spawning new processes to run the Python scripts recursively

import os
import subprocess

rootdir = os.path.dirname(os.path.abspath(__file__))

# iterate root
for subdir, dirs, files in os.walk(rootdir):

    # iterate each livery submission folder in root
    for dir in dirs:
        aircraftdir = rootdir + "/" + dir
        subprocess.call(aircraftdir + "/aircraft.py", shell=True)
        subprocess.call(aircraftdir + "/layout.py", shell=True)

    break
