#!/usr/bin/env python

import requests
import json

# put your keys in the header
headers = {
    "app_id": "<replace me>",
    "app_key": "<replace me>"
}

url = "https://api.kairos.com/detect"

files = {'image': open('portrait.png', 'rb')}

r = requests.post( url, headers=headers, files=files )
print(type(r.text))
# print(json.dumps(r.text, indent=4))
print(json.dumps(json.loads(r.text), indent=4))
