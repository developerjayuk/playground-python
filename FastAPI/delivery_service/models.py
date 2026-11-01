from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel


# OrderStatus (Enum) -> preparing, picked_up, in_transit, delivered
class OrderStatus(str, Enum):
    PREPARING = "preparing"
    PICKED_UP = "picked_up"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"


class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_name: str
    delivery_address: str
    items: str
    status: OrderStatus = Field(default=OrderStatus.PREPARING)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


# Schema for creating a new order
class OrderCreate(SQLModel):
    customer_name: str
    delivery_address: str
    items: str


class OrderUpdateStatus(SQLModel):
    status: OrderStatus | None
    delivery_address: str | None = None


class StatusLog(SQLModel):
    order_id: int
    old_status: str
    new_status: str
    changed_at: datetime
