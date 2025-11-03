# Test placeholder
from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_health():
    r = client.get("/")
    assert r.status_code in (404, 200)  # root may not be implemented

def test_ingest_and_query():
    sample = [{"id": "t1", "text": "The cat sat on the mat."}]
    r = client.post("/ingest", json=sample)
    assert r.status_code == 200
    q = client.post("/query", json={"query": "cat", "k": 1})
    assert q.status_code == 200
    assert "results" in q.json()
