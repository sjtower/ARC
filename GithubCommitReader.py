__author__ = 'Simon'

# Initial file to test reading a single commit from a Github repository#

# Test reading a single line

import requests
import json

headers = {'Accept': 'application/vnd.github.diff'}

url = 'https://api.github.com/repos/sjtower/ARC/commits/fae79f8147d34fbbd876bc4822122d116055d3ac'
# url = 'https://api.github.com/repos/pengwynn/dotfiles/commits/aee60a4cd56fb4c6a50e60f17096fc40c0d4d72c'
myData = requests.get(url, headers=headers)
# print(json.dumps(myData, indent=2))
print myData.text