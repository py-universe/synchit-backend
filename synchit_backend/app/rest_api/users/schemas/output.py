from pydantic import BaseModel


class BaseAuthOutputModel(BaseModel):
    uid: str
    email: str
    display_name: str


class SignupOutputModel(BaseAuthOutputModel):
    email_verified: bool


class AuthOutputModel(BaseAuthOutputModel):
   access_token: str
   refresh_token: str


class RefreshToken(BaseModel):
    access_token: str
    refresh_token: str