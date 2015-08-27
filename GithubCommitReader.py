__author__ = 'Simon'

# Initial file to test reading a single commit from a Github repository#

import requests
import json

#make request to the commit URL and print response
myData = requests.get('https://api.github.com/repos/sjtower/ARC/git/commits/fae79f8147d34fbbd876bc4822122d116055d3ac').json()
print(json.dumps(myData, indent=2))
# print json.dumps(parsed, indent=4, sort_keys=True)