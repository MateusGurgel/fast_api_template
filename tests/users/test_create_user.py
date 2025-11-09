from sqlmodel import Session
from starlette.testclient import TestClient

from fast_api_template.core.main import app
from fast_api_template.core.infra.postgres import (
    get_session,
)


async def test_login(session: Session) -> None:

    def get_session_override() -> Session:
        return session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)

    user_payload = {"email": "user@example.com", "password": "senha123"}

    # 1º try, should create user
    response1 = client.post("/v1/users/", json=user_payload)
    print(response1.json())
    assert response1.status_code == 201

    # 2º try, should fail
    response2 = client.post("/v1/users/", json=user_payload)
    assert response2.status_code == 400
    assert "the email already exists" in response2.text.lower()
