from random import *
import time
import requests
import json

while True:
    random_number = randint(1, 100)
    print(random_number)

    metrics_list = []
    metrics_dimensions = {'rng':'python', 'script':'random_gen.py'}
    metrics_list.append({'metric':'custom.random_number', 'value':random_number, 
'timestamp':int(time.time()*1000), 'dimensions':metrics_dimensions})

    metrics_data = {'gauge':metrics_list}
    
    metrics_url = 'https://ingest.us1.signalfx.com/v2/datapoint'
    metrics_headers = {'Content-Type':'application/json', 
'X-SF-TOKEN':'*****'}
    send_metrics = requests.post(metrics_url, headers=metrics_headers, 
data=json.dumps(metrics_data))

    print(send_metrics, send_metrics.json())
    time.sleep(5)
