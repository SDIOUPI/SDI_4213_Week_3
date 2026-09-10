# Week 3 In-Class Lab: Automated Unit Testing

## Course

**SDI 4213-980: DevOps – CI/CD**

## Lab focus

This lab introduces automated testing using the Week 3 FastAPI starter project. You will run the application locally, run automated tests, inspect the difference between unit tests and API route tests, intentionally break a test, fix it, and add a new test using the GitHub workflow from Week 2.

The goal is to understand why automated testing is the foundation of CI/CD.

## Learning objectives

By the end of this lab, you should be able to:

1. Explain why automated tests are important for DevOps and CI/CD.
2. Distinguish between manual testing, unit testing, and API route testing.
3. Run a FastAPI application locally.
4. Run tests using `pytest`.
5. Read basic test results.
6. Modify application code and observe test failures.
7. Add a new automated unit test.
8. Complete testing work using an issue, branch, commit, pull request, review, and merge.

---

# Part 1: Start from the latest main branch

Before making any changes, start from `main` and pull the latest version.

```bash
git checkout main
git pull
```

Or:

```bash
git switch main
git pull
```

Check that your working tree is clean:

```bash
git status
```

---

# Part 2: Create a virtual environment and install dependencies

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

---

# Part 3: Run the application locally

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

Open the following URLs in your browser:

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/health
http://127.0.0.1:8000/items
http://127.0.0.1:8000/items/1
```

Answer these questions in `docs/testing-notes.md`:

1. What response do you see at `/health`?
2. What response do you see at `/items`?
3. Why might a `/health` endpoint be useful in a DevOps pipeline?

---

# Part 4: Run the automated tests

Stop the app if it is running, or open a second terminal.

Run all tests:

```bash
pytest
```

Run tests with more detail:

```bash
pytest -v
```

Run only the service tests:

```bash
pytest tests/test_services.py -v
```

Run only the API tests:

```bash
pytest tests/test_api.py -v
```

Answer these questions in `docs/testing-notes.md`:

1. How many tests passed?
2. Which test file contains unit tests?
3. Which test file contains API route tests?

---

# Part 5: Inspect the unit tests

Open:

```text
tests/test_services.py
```

Find this test:

```python
def test_calculate_total_quantity():
    items = [
        Item(id=10, name="Keyboard", quantity=2),
        Item(id=11, name="Mouse", quantity=4),
    ]

    assert calculate_total_quantity(items) == 6
```

This is a unit test because it checks one function: `calculate_total_quantity`.

Answer this question in `docs/testing-notes.md`:

Why is this test considered a unit test?

---

# Part 6: Inspect the API route tests

Open:

```text
tests/test_api.py
```

Find this test:

```python
def test_health_check_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

This test calls the FastAPI route and checks the HTTP response.

Answer this question in `docs/testing-notes.md`:

Why is this different from directly testing a single Python function?

---

# Part 7: Intentionally break a test

Open:

```text
app/main.py
```

Find the health check function:

```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

Change it to:

```python
@app.get("/health")
def health_check():
    return {"status": "broken"}
```

Run the tests:

```bash
pytest
```

Answer these questions in `docs/testing-notes.md`:

1. Which test failed?
2. What did the test expect?
3. What did the application return instead?

---

# Part 8: Fix the broken test

Change the health check function back to:

```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

Run the tests again:

```bash
pytest
```

Confirm that all tests pass.

---

# Part 9: Create an issue for a new test

Create a GitHub Issue titled:

```text
Add test for low stock item
```

Use this description:

```text
Add a unit test that confirms an item is identified as low stock when its quantity is below the selected threshold.
```

Assign the issue to yourself and move it to **In Progress** on the project board.

---

# Part 10: Create a branch for your testing work

Start from `main`:

```bash
git checkout main
git pull
```

Or:

```bash
git switch main
git pull
```

Create a new branch:

```bash
git checkout -b test/add-low-stock-test
```

Or:

```bash
git switch -c test/add-low-stock-test
```

Confirm you are on the branch:

```bash
git branch
```

---

# Part 11: Add a new unit test

Open:

```text
tests/test_services.py
```

Add this test:

```python
def test_is_low_stock_true_when_quantity_below_threshold():
    item = Item(id=30, name="USB cable", quantity=1)

    assert is_low_stock(item, threshold=2) is True
```

Run the tests:

```bash
pytest
```

Confirm that all tests pass.

---

# Part 12: Commit and push your test

Check your changes:

```bash
git status
git diff
```

Stage your changes:

```bash
git add tests/test_services.py docs/testing-notes.md
```

Commit your changes:

```bash
git commit -m "Add low stock unit test"
```

Push your branch:

```bash
git push -u origin test/add-low-stock-test
```

---

# Part 13: Open a pull request

Open a pull request from:

```text
test/add-low-stock-test
```

into:

```text
main
```

Use this pull request title:

```text
Add low stock unit test
```

In the description, include:

```text
This pull request adds a new unit test for the is_low_stock function and updates the team's testing notes.

Closes #<issue-number>
```

Replace `<issue-number>` with the issue number from GitHub.

---

# Part 14: Review and merge

A teammate should review the pull request.

The reviewer should check:

- Does the new test actually test low stock behavior?
- Does `pytest` pass?
- Are the testing notes updated?
- Was the work completed on a branch?

After approval, merge the pull request into `main`.

Delete the branch after merging.

Move the related issue to **Done** on the project board.

---

# Required deliverables

Submit the following:

1. Link to the GitHub repository.
2. Link to the issue titled `Add test for low stock item`.
3. Link to the pull request titled `Add low stock unit test`.
4. Screenshot or copied output showing that `pytest` passed.
5. Updated `docs/testing-notes.md`.

---

# Reflection questions

Answer these in `docs/testing-notes.md` or a separate submission:

1. What is the difference between a unit test and an API route test?
2. What happened when you intentionally broke the `/health` endpoint?
3. Why is automated testing important before creating a CI/CD pipeline?
4. How will these tests be useful when GitHub Actions is introduced next week?

---

# Final reminder

The main workflow for this lab is:

```text
Run app → Run tests → Break test → Fix test → Add test → Branch → Pull request → Review → Merge
```

This prepares your project for continuous integration in Week 4.
