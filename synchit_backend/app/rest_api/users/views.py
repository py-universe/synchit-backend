from fastapi import APIRouter, Request, Depends
from fastapi.exceptions import HTTPException
import uvicorn

from sqlalchemy.orm import Session

from .helpers import firebase
from .schemas import input, output
from synchit_backend.db.dependencies import get_db_session
from .db_crud import create_user_profile

auth_router = APIRouter()


# signup endpoint
@auth_router.post("/signup", response_model=output.AuthOutputModel)
async def signup(
    signup_data: input.SignupInputModel,
    db: Session = Depends(get_db_session)
):
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
        
        # If user has been created successfully, log them in
        if user['email'] == email:
            create_user_profile(db=db, user_id=user['uid'])
            user = firebase.sign_in_user(email, password)
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


# login endpoint
@auth_router.post("/refresh-token", response_model=output.RefreshToken)
async def refresh(data: input.RefreshToken):
    refresh_token = data.refresh_token

    try:
        user = firebase.refresh_token(refresh_token=refresh_token)
        return user
    except:
        return HTTPException(
            detail={'message': 'There was an error refreshing the token'}, 
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
