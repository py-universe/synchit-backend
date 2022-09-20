from firebase_admin import auth as ath


def create_firebase_user(email: str, password: str):
    user = ath.create_user(
        email=email,
        password=password
    )

    user = {
        'uid': user.uid,
        'email': user.email
    }

    return user


def verify_token(jwt: str):
    user = ath.verify_id_token(jwt)

    return user