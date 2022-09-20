from pydantic import BaseModel


class BaseAuthInputModel(BaseModel):
    email: str
    password: str


class SignupInputModel(BaseAuthInputModel):
    display_name: str
   
    class Config:
        schema_extra = {
            "example": {
                "email": "sample@sample.com", 
                "password": "password", 
                "display_name": "super_x"
            }
        }


class LoginInputModel(BaseAuthInputModel):
   
    class Config:
        schema_extra = {
            "example": {
                "email": "sample@sample.com", "password": "password"
            }
        }

