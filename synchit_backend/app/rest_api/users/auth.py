import json

import firebase_admin
import pyrebase
from firebase_admin import credentials


cred = credentials.Certificate('synchit_firebase_service_keys.json')
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('firebase_config.json')))

