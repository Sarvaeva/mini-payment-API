from fastapi.testclient import TestClient
from app.main import app
from app import db, models

client = TestClient(app)

def setup_function():
    models.Base.metadata.drop_all(bind=db.engine)
    models.Base.metadata.create_all(bind=db.engine)

def test_create_and_read_account():
    r = client.post("/accounts", json={"name": "A", "balance": 50.0})
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "A"
    assert data["balance"] == 50.0

    r2 = client.get(f"/accounts/{data['id']}")
    assert r2.status_code == 200
    assert r2.json()["name"] == "A"

def test_read_missing_account():
    r = client.get("/accounts/999999")
    assert r.status_code == 404