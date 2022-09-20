from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
import uvicorn

from .helpers import firebase
from . import auth


auth_router = APIRouter()


# signup endpoint
@auth_router.post("/signup")
async def signup(request: Request):
    req = await request.json()
    email = req['email']
    password = req['password']
    if email is None or password is None:
        return HTTPException(detail={'message': 'Error! Missing Email or Password'}, status_code=400)
    try:
        user = firebase.create_firebase_user(
           email=email,
           password=password
        )

        return JSONResponse(content={'message': f'Successfully created user: {user}'}, status_code=200)    
    except Exception as e:
        return HTTPException(detail={'message': f"Error Creating User due to: {e}"}, status_code=400)
 

# login endpoint
@auth_router.post("/login")
async def login(request: Request):
   req_json = await request.json()
   email = req_json['email']
   password = req_json['password']
   try:
       user = auth.pb.auth().sign_in_with_email_and_password(email, password)
    
       jwt = user['idToken']
       return JSONResponse(content={'token': jwt}, status_code=200)
   except:
       return HTTPException(detail={'message': 'There was an error logging in'}, status_code=400)
 

# ping endpoint
@auth_router.post("/ping")
async def validate(request: Request):
   headers = request.headers
   jwt = headers.get('authorization')
   print(f"jwt:{jwt}")
   user = firebase.verify_token(jwt)
   return user["uid"]
 

if __name__ == "__main__":
   uvicorn.run("main:app")
