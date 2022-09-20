from pydantic import BaseModel


class BaseAuthInput(BaseModel):
    email: str
    password: str


class SignupInput(BaseAuthInput):
    display_name: str
   
    class Config:
        schema_extra = {
            "example": {
                "email": "sample@sample.com", 
                "password": "password", 
                "display_name": "super_x"
            }
        }


class LoginInput(BaseAuthInput):
   
    class Config:
        schema_extra = {
            "example": {
                "email": "sample@sample.com", "password": "password"
            }
        }

