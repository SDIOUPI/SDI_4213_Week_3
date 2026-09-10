# Contributing Guide

Use the course workflow for every routine change:

```text
Issue → Branch → Change → Commit → Push → Pull Request → Review → Merge → Update Board
```

## Branch naming

Examples:

```text
test/add-low-stock-test
feature/add-inventory-endpoint
docs/update-testing-notes
fix/health-check-response
```

## Pull requests

Every pull request should include:

- a clear title
- a short summary
- the related issue number
- evidence that tests pass

## Testing expectation

Before opening a pull request, run:

```bash
pytest
```

Do not merge code that breaks the automated tests.
