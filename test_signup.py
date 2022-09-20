import requests
 

def signup(email: str, password: str):
   body = {
       "email": email,
       "password": password
   }
   response = requests.post(url="http://127.0.0.1:8000/api/signup", json=body)
   return response.text
 
print(signup("nyior@nyior.com", "password"))