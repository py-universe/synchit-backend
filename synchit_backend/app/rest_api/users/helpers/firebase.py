import json

import firebase_admin
import pyrebase

from firebase_admin import credentials, auth


cred = credentials.Certificate('synchit_firebase_service_keys.json')
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('firebase_config.json')))


def create_firebase_user(email: str, password: str, display_name: str):
    user = auth.create_user(
        email=email,
        password=password,
        display_name=display_name
    )

    print(f"\n USER: {user}")
    user = {
        'uid': user.uid,
        'email': user.email,
        'display_name': user.display_name,
        'email_verified': user.email_verified
    }
    return user


def sign_in_user(email: str, password: str):
    user = pb.auth().sign_in_with_email_and_password(email, password)
    user = {
        'uid': user['localId'],
        'email': user['email'],
        'display_name': user['displayName'],
        'access_token': user['idToken'],
        'refresh_token': user['refreshToken']
    }
    return user


def verify_token(jwt: str):
    user = auth.verify_id_token(jwt)
    return user