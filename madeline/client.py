#!/usr/bin/env python

import requests
import json

url = "http://app:5000"

r = requests.get('{url}/version'.format(url=url))

with open('tests/data/examples/cs_001.data') as f:
    data = f.read()

payload = { 'data': data,
            'args': [ '--custom-icon-colors',
                      'ALS=red,PLS=purple,PMA=blue,HSP=green;A=black;FTD=black,Non-FTD=lightgray;A=black'
                    ]
          }

r = requests.post('{url}/submit'.format(url=url), data=json.dumps(payload))

