import requests
import time

url = 'http://10.10.1.116:80/' 

while True:
    try:
        response = requests.get(url)
        print(f"Request made to {url} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    time.sleep(10)
