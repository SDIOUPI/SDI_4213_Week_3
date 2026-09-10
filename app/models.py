from pydantic import BaseModel, Field


class Item(BaseModel):
    """Simple inventory item used in the Week 3 testing lab."""

    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    category: str = Field(default="general", min_length=1)
