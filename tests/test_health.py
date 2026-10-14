

def test_health_returns_ok(client):
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert "version" in body


def test_health_reports_task_count(client):
    client.post("/tasks", json={"title": "A"})
    assert client.get("/health").json()["task_count"] == 1
