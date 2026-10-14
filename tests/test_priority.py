def test_priority_defaults_to_medium(client):
    r = client.post("/tasks", json={"title": "A"})
    assert r.status_code == 201
    assert r.json()["priority"] == "medium"


def test_create_task_with_each_valid_priority(client):
    for p in ["low", "medium", "high"]:
        r = client.post("/tasks", json={"title": f"Task {p}", "priority": p})
        assert r.status_code == 201
        assert r.json()["priority"] == p


def test_invalid_priority_rejected(client):
    r = client.post("/tasks", json={"title": "A", "priority": "urgent"})
    assert r.status_code == 422
    assert client.get("/tasks").json() == []
