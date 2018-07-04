import requests
import time
from threading import Thread

get_notifications = "http://localhost:5000/api/push_notifications"
put_notifications = "http://localhost:5000/api/push_notifications/update"
payload = {'player_id': 0}

while (True):
    r = requests.get(get_notifications, params = payload)
    data = r.json()
    if (data[0]['received'] == 0):
        r = requests.put(put_notifications, params = payload, data = {'received': 1})
        print(r.json())
        
    time.sleep(0.1)

