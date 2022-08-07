import requests
data = {"user_name": "saurabh","name": "saurabh","password": "saurabh"}
r = requests.post(URL,data)
URL = "http://127.0.0.1:8000/userdata/"