from pydantic import BaseModel


class BaseAuthOutputModel(BaseModel):
    uid: str
    email: str
    display_name: str


class SignupOutputModel(BaseAuthOutputModel):
    email_verified: bool


class LoginOutputModel(BaseAuthOutputModel):
   access_token: str
   refresh_token: str


