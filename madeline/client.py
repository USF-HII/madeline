#!/usr/bin/env python

import requests
import json

url = "http://app:5000"

r = requests.get('{url}/version'.format(url=url))

print(r.text)

with open('cs_001.data') as f:
    data = f.read()

payload = { 'data': data }

payload = { 'data': 'ban!man' }

r = requests.post('{url}/submit'.format(url=url), data=json.dumps(payload))

with open('output.svg', 'w') as f:
     f.write(r.json()['svg'])

