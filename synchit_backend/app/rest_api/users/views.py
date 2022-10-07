from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
import uvicorn

from .helpers import firebase
from .schemas import input, output

auth_router = APIRouter()


# signup endpoint
@auth_router.post("/signup", response_model=output.AuthOutputModel)
async def signup(signup_data: input.SignupInputModel):
    email = signup_data.email
    password = signup_data.password
    display_name = signup_data.display_name

    if email is None or password is None:
        return HTTPException(
            detail={'message': 'Error! Missing Email or Password'}, 
            status_code=400
        )
    
    try:
        user = firebase.create_firebase_user(
           email=email,
           password=password,
           display_name=display_name
        )
        print(f"\n CREATED USER: {user}\n")
        
        # If user has been created successfully, log them in
        if user['email'] == email:
            user = firebase.sign_in_user(email, password)
            print(f"\n LOGGEDIN USER AFTER SIGNUP: {user}\n")
            return user   
    except Exception as e:
        return HTTPException(
            detail={'message': f"Error Creating User due to: {e}"}, 
            status_code=400
        )
 

# login endpoint
@auth_router.post("/login", response_model=output.AuthOutputModel)
async def login(login_data: input.LoginInputModel):
    email = login_data.email
    password = login_data.password

    try:
        user = firebase.sign_in_user(email, password)
        return user
    except:
        return HTTPException(
            detail={'message': 'There was an error logging in'}, 
            status_code=400
        )
 

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
