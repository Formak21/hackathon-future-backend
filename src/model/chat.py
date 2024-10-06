from typing import Optional, List
from factory import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Chat(db.Model):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    title: Mapped[Optional[str]] = mapped_column(String)

    messages: Mapped[List["Message"]] = relationship(back_populates='chat')
