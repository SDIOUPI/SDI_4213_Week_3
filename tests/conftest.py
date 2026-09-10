import pytest

from app.models import Item
from app import services


@pytest.fixture(autouse=True)
def reset_items():
    """Reset in-memory data before each test so tests do not affect each other."""
    services.ITEMS.clear()
    services.ITEMS.extend(
        [
            Item(id=1, name="Laptop", quantity=3, category="equipment"),
            Item(id=2, name="Docking station", quantity=5, category="equipment"),
        ]
    )
