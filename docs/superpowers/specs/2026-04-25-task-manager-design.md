# Personal Task Manager - Design Spec

## Overview

A personal task management web application built with Flask. Single-user, no authentication, focused on quick task tracking with status, priority, and due dates.

## Architecture

**Approach:** Simple starter - single module Flask app with minimal structure.

**Stack:**
- Backend: Flask + SQLAlchemy
- Database: SQLite
- Frontend: Jinja2 templates + Bootstrap 5 CDN
- No authentication

## Project Structure

```
day4/
├── app.py              # Flask app entry point, routes
├── models.py           # SQLAlchemy models
├── templates/
│   ├── base.html       # Common layout
│   ├── index.html      # Task list (main page)
│   └── _task.html      # Task card partial
├── static/
│   ├── style.css
│   └── main.js
├── requirements.txt
└── instance/
    └── tasks.db        # SQLite (auto-created)
```

## Data Model

### Task Table

| Field | Type | Description |
|-------|------|-------------|
| id | Integer PK | Auto-increment |
| title | String(200) | Task title (required) |
| description | Text | Details (optional) |
| status | Enum | `todo`, `in_progress`, `done` |
| priority | Enum | `low`, `medium`, `high` |
| due_date | Date | Deadline (optional) |
| created_at | DateTime | Creation timestamp |
| updated_at | DateTime | Last modified timestamp |

Default status: `todo`. Default priority: `medium`.

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Task list with filter/sort |
| `/task/new` | GET/POST | Create task |
| `/task/<id>/edit` | GET/POST | Edit task |
| `/task/<id>/delete` | POST | Delete task |
| `/task/<id>/status` | POST | Quick status change |

### Filtering & Sorting

Query parameters on `/`:
- `?status=todo` - filter by status
- `?sort=due_date` - sort by field
- `?sort=priority` - sort by priority

## UI Design

- **Bootstrap 5** via CDN for clean default styling
- **Main page:** Tab-based layout (Todo / In Progress / Done)
- **Task card:** Title, priority badge, due date, quick status buttons
- **Create/Edit:** Separate form pages with validation
- **No JavaScript framework** - vanilla JS for minor interactions

## Dependencies

```
flask
flask-sqlalchemy
```

## Success Criteria

- Can create, view, edit, delete tasks
- Can filter tasks by status
- Can set priority and due date
- Responsive layout that works on mobile
