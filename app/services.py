from app.models import Item


# In-memory starter data. Later in the course, this can be replaced with a database.
ITEMS: list[Item] = [
    Item(id=1, name="Laptop", quantity=3, category="equipment"),
    Item(id=2, name="Docking station", quantity=5, category="equipment"),
]


def get_all_items() -> list[Item]:
    """Return all inventory items."""
    return ITEMS


def get_item_by_id(item_id: int) -> Item | None:
    """Return one item by ID, or None if it does not exist."""
    for item in ITEMS:
        if item.id == item_id:
            return item
    return None


def calculate_total_quantity(items: list[Item]) -> int:
    """Return the total quantity across a list of items."""
    return sum(item.quantity for item in items)


def is_low_stock(item: Item, threshold: int = 2) -> bool:
    """Return True when an item quantity is at or below the threshold."""
    return item.quantity <= threshold


def create_item(item: Item) -> Item:
    """Add a new item to the in-memory list.

    Raises:
        ValueError: if an item with the same ID already exists.
    """
    if get_item_by_id(item.id) is not None:
        raise ValueError(f"Item with id {item.id} already exists")

    ITEMS.append(item)
    return item
