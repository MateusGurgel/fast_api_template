import hashlib
from typing import Dict

import jwt

from src.fast_api_template.core.infra.env import env


def hash_string(string: str, salt: str = env.salt, peper: str = env.pepper) -> str:
    combined = f"{salt}{string}{peper}"
    return hashlib.sha256(combined.encode("utf-8")).hexdigest()


def encrypt_payload(data: Dict[str, str], secret: str = env.secret) -> str:
    return jwt.encode(data, secret, algorithm="HS256")
