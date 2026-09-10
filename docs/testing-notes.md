# Testing Notes

Use this file during the Week 3 lab to record what your team learned about automated testing.

## Manual testing

Manual testing means a person checks whether the application works.

Example:

1. Start the app with `uvicorn app.main:app --reload`.
2. Open `http://127.0.0.1:8000/health` in a browser.
3. Confirm that the response is `{"status":"ok"}`.

## Automated testing

Automated testing means code checks whether the application behaves correctly.

Example:

```python
def test_health_check_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

## Unit tests

Unit tests check small pieces of logic, usually functions.

In this project, `tests/test_services.py` contains unit tests for functions in `app/services.py`.

## API route tests

API route tests check whether the application endpoints respond correctly.

In this project, `tests/test_api.py` contains tests for routes in `app/main.py`.

## Team notes

Add your notes below.

-
-
-
