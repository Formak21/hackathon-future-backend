from typing import List, Optional
from datetime import datetime
from factory import db
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Message(db.Model):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped["User"] = relationship(back_populates='messages')

    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id'))
    chat: Mapped["Chat"] = relationship(back_populates='messages')

    type: Mapped[str] = mapped_column(String)
    data: Mapped[str] = mapped_column(String)

    sent_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
