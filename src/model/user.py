from factory import db
from typing import List, Optional

from sqlalchemy import String, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String)

    first_name: Mapped[str] = mapped_column(String)
    mid_name: Mapped[Optional[str]] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    photo_url: Mapped[Optional[str]] = mapped_column(String)

    role: Mapped[str] = mapped_column(String)

    info: Mapped[Optional[str]] = mapped_column(String)

    tags: Mapped[List[str]] = mapped_column(ARRAY(String))

    session: Mapped["Session"] = relationship(back_populates="user")

    projects: Mapped[List["UserProjectAssociation"]] = relationship(back_populates='user')

    chats: Mapped[List["UserChatAssociation"]] = relationship(back_populates='user')

    feed: Mapped["Feed"] = relationship(back_populates="user")

    messages: Mapped[List["Message"]] = relationship(back_populates='user')
