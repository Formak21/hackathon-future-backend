from typing import Optional
from factory import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Chat(db.Model):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)

    title: Mapped[Optional[str]] = mapped_column(String)

    user: Mapped["User"] = relationship(back_populates='chats')
