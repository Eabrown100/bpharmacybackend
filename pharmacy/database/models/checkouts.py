from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from pharmacy.database.core import Base

class Checkout(Base):
    __tablename__="checkouts"

    cart_items_id: Mapped[int]= mapped_column(ForeignKey("cart_items.id"), nullable=False, primary_key=True)
    order_id: Mapped[int]= mapped_column(ForeignKey("orders.id"), nullable=False, primary_key=True)
    sub_total: Mapped[float]=mapped_column(nullable=False)