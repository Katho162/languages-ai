import os
import time
from typing import Dict, List
from ..users.schema import UserSchema

import jwt

JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")

def token_response(token: str):
    return {
        "access_token": token
    }

# function used for signing the JWT string
def signJWT(user, permissions: List[str] = []) -> Dict[str, str]:
    payload = {
        "user": user,
        "permissions": permissions,
        "expires": time.time() + 1000 * 60 * 60 * 24 * 31
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        print(decoded_token)
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}