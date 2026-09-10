import pytest

from app.models import Item
from app.services import (
    calculate_total_quantity,
    create_item,
    get_all_items,
    get_item_by_id,
    is_low_stock,
)


def test_get_all_items_returns_starter_items():
    items = get_all_items()

    assert len(items) == 2
    assert items[0].name == "Laptop"


def test_get_item_by_id_returns_matching_item():
    item = get_item_by_id(1)

    assert item is not None
    assert item.id == 1
    assert item.name == "Laptop"


def test_get_item_by_id_returns_none_for_missing_item():
    item = get_item_by_id(999)

    assert item is None


def test_calculate_total_quantity():
    items = [
        Item(id=10, name="Keyboard", quantity=2),
        Item(id=11, name="Mouse", quantity=4),
    ]

    assert calculate_total_quantity(items) == 6


def test_is_low_stock_true_when_quantity_at_threshold():
    item = Item(id=20, name="Projector", quantity=2)

    assert is_low_stock(item, threshold=2) is True


def test_is_low_stock_false_when_quantity_above_threshold():
    item = Item(id=21, name="Monitor", quantity=4)

    assert is_low_stock(item, threshold=2) is False


def test_create_item_adds_new_item():
    new_item = Item(id=3, name="Webcam", quantity=7, category="equipment")

    created = create_item(new_item)

    assert created.name == "Webcam"
    assert get_item_by_id(3) is not None
    assert len(get_all_items()) == 3


def test_create_item_rejects_duplicate_id():
    duplicate = Item(id=1, name="Duplicate laptop", quantity=1)

    with pytest.raises(ValueError):
        create_item(duplicate)

def test_is_low_stock_true_when_quantity_below_threshold():
    item = Item(id=22, name="Headphones", quantity=1)

    assert is_low_stock(item, threshold=2) is True