from firebase_admin import auth as ath


def create_firebase_user(email: str, password: str, display_name: str):
    user = ath.create_user(
        email=email,
        password=password,
        display_name=display_name
    )

    user = {
        'uid': user.uid,
        'email': user.email,
        'display_name': user.display_name,
        'email_verified': user.email_verified
    }

    return user


def verify_token(jwt: str):
    user = ath.verify_id_token(jwt)

    return user