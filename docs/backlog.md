# Product Backlog - Task & Handover Tracker

## Product Vision

For busy clinicians and students, the Task & Handover Tracker is a lightweight service that lets
them capture, prioritise and complete daily tasks in one place, so that nothing is missed between
shifts.

## Prioritisation and Estimation

- **Priority:** MoSCoW (Must / Should / Could)
- **Estimation:** Story points using the Fibonacci scale (1, 2, 3, 5, 8). Points are relative:
  US7 (a single health endpoint) is the 1-point reference story, and other stories are sized against it.

## Backlog Overview

| ID | Issue | User Story | Priority | Points | Sprint |
|----|-------|-----------|----------|--------|--------|
| US1 | #2 | As a user, I can create a task with a title and description | Must | 3 | 1 |
| US2 | #3 | As a user, I can list all tasks | Must | 2 | 1 |
| US3 | #5 | As a user, I can mark a task as complete | Must | 2 | 1 |
| US4 | #4 | As a user, I can set a priority (low/medium/high) on a task | Should | 3 | 2 |
| US5 | #6 | As a user, I can filter tasks by status or priority | Should | 3 | 2 |
| US6 | #7 | As a user, I can edit or delete a task | Should | 3 | Backlog |
| US7 | #8 | As an operator, I can check a `/health` endpoint | Must | 1 | 2 |
| US8 | #9 | As an operator, I get request logs and error logging | Should | 2 | 2 |

**Total:** 19 points. Sprint 1 = 7 points, Sprint 2 = 9 points, US6 deferred (3 points).

## Acceptance Criteria

### US1 - Create a task (3 pts)
- **Given** a valid title, **when** I POST `/tasks`, **then** I receive `201` and the task with a unique ID.
- **Given** a title and a description, **when** I POST `/tasks`, **then** both are stored and returned.
- **Given** an empty or blank title, **when** I POST `/tasks`, **then** I receive `422` and no task is created.

### US2 - List tasks (2 pts)
- **Given** no tasks exist, **when** I GET `/tasks`, **then** I receive `200` and an empty list.
- **Given** several tasks exist, **when** I GET `/tasks`, **then** I receive `200` and all tasks in creation order.

### US3 - Complete a task (2 pts)
- **Given** an existing task, **when** I PATCH `/tasks/{id}/complete`, **then** I receive `200` and `completed` is `true`.
- **Given** an ID that does not exist, **when** I PATCH `/tasks/{id}/complete`, **then** I receive `404`.
- **Given** an already completed task, **when** I complete it again, **then** it stays completed and I receive `200`.

### US4 - Set priority (3 pts)
- **Given** a task created without a priority, **when** it is returned, **then** its priority is `medium`.
- **Given** a priority of `low`, `medium` or `high`, **when** I POST `/tasks`, **then** the task is created with that priority.
- **Given** an invalid priority such as `urgent`, **when** I POST `/tasks`, **then** I receive `422`.

### US5 - Filter tasks (3 pts)
- **Given** completed and open tasks, **when** I GET `/tasks?completed=true`, **then** only completed tasks are returned.
- **Given** tasks of mixed priority, **when** I GET `/tasks?priority=high`, **then** only high-priority tasks are returned.
- **Given** both filters, **when** I GET `/tasks?priority=high&completed=false`, **then** only tasks matching both are returned.
- **Given** a filter with no matches, **when** I GET `/tasks`, **then** I receive `200` and an empty list.

### US6 - Edit or delete a task (3 pts, not planned)
- **Given** an existing task, **when** I update its title or description, **then** the changes are saved and returned.
- **Given** an existing task, **when** I DELETE it, **then** I receive `204` and it no longer appears in the list.
- **Given** an ID that does not exist, **when** I edit or delete, **then** I receive `404`.

### US7 - Health endpoint (1 pt)
- **Given** the service is running, **when** I GET `/health`, **then** I receive `200` and `{"status": "ok"}` plus basic info.
- **Given** the CI pipeline runs, **when** tests execute, **then** the health endpoint is covered by an automated test.

### US8 - Logging and error tracking (2 pts)
- **Given** any request, **when** it is handled, **then** the method, path, status code and duration are logged.
- **Given** an unexpected server error, **when** it occurs, **then** it is logged with a stack trace and the client receives a generic `500` message.
- **Given** a request for an unknown task, **when** it is handled, **then** a warning is logged.

## Definition of Done

A story is **Done** only when all of the following are true:

1. Code is committed on a feature branch and merged to `main` through a pull request.
2. Unit/integration tests cover every acceptance criterion and pass locally.
3. The CI pipeline is green on the pull request.
4. Acceptance criteria are demonstrated (Swagger UI screenshot or test output).
5. The README or API docs are updated where behaviour changed.
6. The linked issue is closed and its card moved to Done on the project board.
