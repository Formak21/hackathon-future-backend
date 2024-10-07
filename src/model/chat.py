from typing import Optional, List
from factory import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserChatAssociation(db.Model):
    __tablename__ = "user_chat_association"

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True, nullable=False)
    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id'), primary_key=True, nullable=False)

    user: Mapped["User"] = relationship(back_populates='chats')
    chat: Mapped["Chat"] = relationship(back_populates='users')


class Chat(db.Model):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[Optional[str]] = mapped_column(String)

    users: Mapped[List["UserChatAssociation"]] = relationship(back_populates='chat')
    messages: Mapped[List["Message"]] = relationship(back_populates='chat')

    def __dict__(self):
        return {"id": self.id,
                "title": self.title,
                "messages": [dict(message) for message in self.messages],
                "users": [dict(user) for user in self.users]}
