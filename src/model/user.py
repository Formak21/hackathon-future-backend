from src.factory import db
from typing import List, Optional
from sqlalchemy import String, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(String)

    first_name: Mapped[str] = mapped_column(String)
    mid_name: Mapped[Optional[str]] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)

    role: Mapped[str] = mapped_column(String)

    info: Mapped[str] = mapped_column(String)

    tags: Mapped[List[str]] = mapped_column(ARRAY(String))

    session: Mapped["Session"] = relationship(back_populates="user")
