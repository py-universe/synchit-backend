import requests
import json
 
 
def login(email: str, password: str):
   body = {
       "email": email,
       "password": password
   }
   response = requests.post(url="http://127.0.0.1:8000/api/login", json=body)
   return json.loads(response.text)["token"]
 
token = login("nyior@nyior.com", "password")
 
 
def ping(token: str):
   headers = {
       'authorization': token
   }
   response = requests.post(url="http://127.0.0.1:8000/api/ping", headers=headers)
   return(response)
 
print(ping(token))