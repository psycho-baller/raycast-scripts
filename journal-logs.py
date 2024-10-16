#!/usr/bin/venv python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Add to Journal Log
# @raycast.refreshTime 1h
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Log", "optional": false }
# @raycast.packageName Obsidian

# Documentation:
# @raycast.author Rami Maalouf
# @raycast.authorURL https://github.com/psycho-baller

import datetime
import sys

# get current date
today = datetime.datetime.now().strftime("%y-%m-%d")
path = '/Users/rami/Library/CloudStorage/OneDrive-Personal/Obsidian/0 Journal/0 Daily/'
full_path = path + today + '.md'
# open the file
with open(full_path, 'r') as file:
    # read the contents of the file
    contents = file.readlines()

# loop through the contents
for i, line in enumerate(contents):
    # check if the line starts with 'log:: '
    if line.startswith('log:: '):
        # add the given text after the line
        contents[i] = line.strip('\n') + sys.argv[1] + ". " + '\n'

# open the file for writing
with open(full_path, 'w') as file:
    # write the contents back to the file
    file.writelines(contents)
