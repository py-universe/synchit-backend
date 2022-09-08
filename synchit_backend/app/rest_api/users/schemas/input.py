from authx.models import user
from authx.models import social

class Register(user.UserInRegister):
    pass


class Login(user.UserInLogin):
    pass


class UserUpdate(user.UserInChangeUsername):
    room_id: str


class SocialCreate(social.SocialInCreate):
    pass


class SocialLogin(social.SocialInCreate):
    pass

