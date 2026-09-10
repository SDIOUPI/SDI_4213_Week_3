# SDI 4213 Week 3 Testing Starter

This starter project is designed for the Week 3 in-class lab on application structure and automated testing.

Students will use this repository to practice:

- organizing a small FastAPI application
- running an application locally
- identifying the application entry point
- writing and running unit tests
- writing and running API route tests
- using Git branches and pull requests for testing-related changes

## Project structure

```text
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── services.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_api.py
│   └── test_services.py
├── docs/
│   ├── week3-lab-testing.md
│   └── testing-notes.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the application

```bash
uvicorn app.main:app --reload
```

Open these URLs in a browser:

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/health
http://127.0.0.1:8000/items
http://127.0.0.1:8000/items/1
```

## Run the tests

```bash
pytest
```

To see more detail:

```bash
pytest -v
```

Run only the service/unit tests:

```bash
pytest tests/test_services.py -v
```

Run only the API tests:

```bash
pytest tests/test_api.py -v
```

## Week 3 workflow reminder

Use the same GitHub workflow from Week 2:

```text
Issue → Branch → Change → Commit → Push → Pull Request → Review → Merge → Update Board
```

Do not make routine changes directly on `main`.
