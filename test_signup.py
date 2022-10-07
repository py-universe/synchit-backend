import requests
 

def signup(email: str, password: str, display_name: str):
   body = {
       "email": email,
       "password": password,
       "display_name": display_name,
   }
   response = requests.post(url="http://127.0.0.1:8000/api/v1/auth/signup", json=body)
   return response.text
 
print(signup("nyior@nyior.com", "password", "super_x"))