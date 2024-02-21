# Python Built-in Imports
import base64
import binascii
from pathlib import Path


from starlette.authentication import (AuthenticationBackend, AuthenticationError, SimpleUser, AuthCredentials)
#reload = True

AUTH_USERNAME = "abc"
AUTH_PASSWORD = "Abc123$"

chat_url = "http://localhost:9000/bot/query"



class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return
        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error):
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")
        # TODO: You'd want to verify the username and password here,
        #       possibly by installing `DatabaseMiddleware`
        #       and retrieving user information from `request.database`.
        #AUTH_USERNAME, AUTH_PASSWORD,tomcat_path=get_auth_details()
        if username == AUTH_USERNAME and password == AUTH_PASSWORD:
            return AuthCredentials(["authenticated"]), SimpleUser(username)
        else:
            return
      
