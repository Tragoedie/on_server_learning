import requests


response = requests.post('http://httpbin.org/post', data={'UserId': '12345', 'Status': 'On'})

if response.status_code == 200:
    print("OK")
else:
    print("ERROR", response.status_code)