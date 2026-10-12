# Sprint 1 Plan

## Sprint Goal

Deliver the core of the tracker: a user can create tasks, see them in a list, and mark them complete,
with an automated CI pipeline running tests on every push.

## Selected Stories

| ID | Issue | User Story | Points |
|----|-------|-----------|--------|
| US1 | #2 | Create a task with a title and description | 3 |
| US2 | #3 | List all tasks | 2 |
| US3 | #5 | Mark a task as complete | 2 |
| T1 | #__ | Technical task: set up CI pipeline (GitHub Actions) | - |

**Planned velocity:** 7 story points.

## Why these stories

They are the three Must-have stories and together form a usable minimum product. US1 comes first
because US2 and US3 depend on tasks existing. The CI task is done early so that every later commit is
tested automatically.

## Task Breakdown

**US1**
- Define task models and validation
- Write failing tests for create (test first)
- Implement `POST /tasks`

**US2**
- Write tests for list
- Implement `GET /tasks`

**US3**
- Write tests for complete (including 404)
- Implement `PATCH /tasks/{id}/complete`

**T1**
- Add `.github/workflows/ci.yml` to install dependencies and run `pytest` with coverage

## Working Agreements

- One feature branch per story, merged by pull request with `Closes #<issue>`.
- Commit small and often, using prefixes such as `feat:`, `test:`, `ci:` and `docs:`.
- Write tests before the code where possible.
- A story counts as done only when it meets the Definition of Done in `docs/backlog.md`.

## Risks

- First time using GitHub Actions: mitigate by setting up CI before writing feature code.
- Estimates are untested: velocity this sprint will be used to calibrate Sprint 2.
