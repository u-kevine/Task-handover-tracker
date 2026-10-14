import pytest


@pytest.fixture
def seeded(client):
    client.post("/tasks", json={"title": "high open", "priority": "high"})
    client.post("/tasks", json={"title": "high done", "priority": "high"})
    client.post("/tasks", json={"title": "low done", "priority": "low"})
    client.patch("/tasks/2/complete")
    client.patch("/tasks/3/complete")
    return client


def titles(response):
    return [t["title"] for t in response.json()]


def test_filter_completed_true(seeded):
    r = seeded.get("/tasks?completed=true")
    assert r.status_code == 200
    assert titles(r) == ["high done", "low done"]


def test_filter_by_priority(seeded):
    r = seeded.get("/tasks?priority=high")
    assert r.status_code == 200
    assert titles(r) == ["high open", "high done"]


def test_filter_by_priority_and_status(seeded):
    r = seeded.get("/tasks?priority=high&completed=false")
    assert r.status_code == 200
    assert titles(r) == ["high open"]


def test_filter_with_no_matches_returns_empty_list(seeded):
    r = seeded.get("/tasks?priority=medium")
    assert r.status_code == 200
    assert r.json() == []


def test_invalid_priority_filter_rejected(seeded):
    r = seeded.get("/tasks?priority=urgent")
    assert r.status_code == 422
