import hashlib

from src.fast_api_template.core.infra.env import env


def hash_string(string: str, salt: str = env.salt, peper: str = env.pepper) -> str:
    combined = f"{salt}{string}{peper}"
    return hashlib.sha256(combined.encode("utf-8")).hexdigest()
