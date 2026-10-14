"""Sprint 2 - US8: request logging and error tracking."""
import logging

from fastapi.testclient import TestClient

from app.main import app, store


def test_request_is_logged(client, caplog):
    with caplog.at_level(logging.INFO, logger="tracker"):
        client.get("/tasks")
    assert any("GET /tasks -> 200" in m for m in caplog.messages)


def test_unknown_task_logs_warning(client, caplog):
    with caplog.at_level(logging.WARNING, logger="tracker"):
        client.patch("/tasks/999/complete")
    assert any(
        r.levelname == "WARNING" and "Task 999 not found" in r.getMessage()
        for r in caplog.records
    )


def test_unexpected_error_logged_and_generic_500(monkeypatch, caplog):
    store.clear()

    def boom(*args, **kwargs):
        raise RuntimeError("database exploded")

    monkeypatch.setattr(store, "list", boom)
    client = TestClient(app, raise_server_exceptions=False)
    with caplog.at_level(logging.ERROR, logger="tracker"):
        r = client.get("/tasks")
    assert r.status_code == 500
    assert r.json() == {"detail": "Internal server error"}
    assert "database exploded" not in r.text
    assert any(r.exc_info for r in caplog.records if r.levelname == "ERROR")
