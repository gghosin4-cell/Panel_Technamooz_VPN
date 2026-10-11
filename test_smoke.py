"""Small dependency-light smoke suite for the Railway deployment.
Run with: python test_smoke.py
"""
import os
import tempfile

os.environ.setdefault("RAILWAY_ENVIRONMENT_NAME", "test")
os.environ.setdefault("ADMIN_PASSWORD", "smoke-password-strong")
os.environ.setdefault("ADMIN_USERNAME", "SmokeAdmin")
os.environ.setdefault("SECRET_KEY", "smoke-secret-stable")
os.environ.setdefault("DATA_DIR", tempfile.mkdtemp(prefix="technamooz-smoke-"))

from fastapi.testclient import TestClient
import main


def run():
    with TestClient(main.app, base_url="https://smoke.test") as client:
        assert client.get("/health").status_code == 200
        assert client.get("/login").status_code == 404
        assert client.get(main.ADMIN_PANEL_PATH).status_code == 200
        captcha = client.get("/api/captcha").json()
        response = client.post("/api/login", json={
            "username": "SmokeAdmin",
            "password": "smoke-password-strong",
            "captcha_id": captcha["captcha_id"],
            "captcha_code": captcha["captcha_code"],
        })
        assert response.status_code == 200
        assert client.get("/dashboard").status_code == 200
        created = client.post("/api/links", json={"label": "Smoke node", "protocol": "vless-ws"})
        assert created.status_code == 200
        backup = client.get("/api/backup")
        assert backup.status_code == 200
        assert b"password_hash" not in backup.content
        assert b'"token": ""' not in backup.content
    print("smoke=PASS", main.ADMIN_PANEL_PATH)


if __name__ == "__main__":
    run()
