from fastapi import FastAPI
from easyauth.server import EasyAuthServer


async def add_auth(app: FastAPI) -> None:
    app.auth = await EasyAuthServer.create(
        app,
        '/auth/token',
        auth_secret='abcd1234',
        admin_title='EasyAuth - Company',
        admin_prefix='/admin',
        env_from_file='../server_postgres.json'
    )