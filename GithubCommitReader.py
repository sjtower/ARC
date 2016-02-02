__author__ = 'Simon'

# Initial file to test reading a single commit from a Github repository#

# Test reading a single line

import requests
import json

headers = {'Accept': 'application/vnd.github.diff'}

# url = 'https://api.github.com/repos/sjtower/ARC/commits/38518f0354928340c866fc2e4befb2191678fd21'
# url = 'https://api.github.com/repos/hitherejoe/LeanbackCards/commits/89442c828d29a4335a7a1256ba4ba751b8aa72a4'

url = 'https://api.github.com/repos/elastic/elasticsearch/commits/d91a898f6a339a48d546d9205bcbd7c09a390631'
myData = requests.get(url, headers=headers)
# print(json.dumps(myData, indent=2))
# print myData.text

text_split = myData.text.split('\n')
for line in text_split:
    if line.startswith('+'):
        if '=' in line:
            line_split = line.split('=')
            term = line_split[0].split()[-1]
            print term