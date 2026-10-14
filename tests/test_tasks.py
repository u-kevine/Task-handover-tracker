"""Sprint 1 tests. Each test maps to an acceptance criterion."""


# ---------- US1: create a task ----------
def test_create_task_returns_201_and_id(client):
    r = client.post("/tasks", json={"title": "Check ward round notes"})
    assert r.status_code == 201
    body = r.json()
    assert body["id"] == 1
    assert body["title"] == "Check ward round notes"
    assert body["completed"] is False


def test_create_task_with_description(client):
    r = client.post("/tasks", json={"title": "Handover", "description": "Bed 4 needs review"})
    assert r.status_code == 201
    assert r.json()["description"] == "Bed 4 needs review"


def test_create_task_empty_title_rejected(client):
    r = client.post("/tasks", json={"title": ""})
    assert r.status_code == 422
    assert client.get("/tasks").json() == []

def test_create_task_blank_title_rejected(client):
    r = client.post("/tasks", json={"title": "   "})
    assert r.status_code == 422


def test_create_task_missing_title_rejected(client):
    r = client.post("/tasks", json={})
    assert r.status_code == 422

# ---------- US2: list tasks ----------
def test_list_tasks_empty(client):
    r = client.get("/tasks")
    assert r.status_code == 200
    assert r.json() == []


def test_list_tasks_returns_all_created(client):
    client.post("/tasks", json={"title": "A"})
    client.post("/tasks", json={"title": "B"})
    r = client.get("/tasks")
    assert r.status_code == 200
    assert [t["title"] for t in r.json()] == ["A", "B"]
    

# ---------- US3: complete a task ----------
def test_complete_task_sets_completed_true(client):
    client.post("/tasks", json={"title": "A"})
    r = client.patch("/tasks/1/complete")
    assert r.status_code == 200
    assert r.json()["completed"] is True


def test_complete_unknown_task_returns_404(client):
    r = client.patch("/tasks/999/complete")
    assert r.status_code == 404


def test_complete_task_is_idempotent(client):
    client.post("/tasks", json={"title": "A"})
    client.patch("/tasks/1/complete")
    r = client.patch("/tasks/1/complete")
    assert r.status_code == 200
    assert r.json()["completed"] is True