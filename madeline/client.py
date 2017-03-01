#!/usr/bin/env python

import requests

url = "http://madeline-service:5000"

r = requests.get('{url}/version'.format(url=url))

print(r.text)

with open('cs_001.data') as f:
    data = f.read()

payload = { 'data': data }

r = requests.post('{url}/submit'.format(url=url), data=payload)

r.

with open('output.svg', 'w') as f:
     f.write(r.json()['svg'])

