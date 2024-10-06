from src.factory import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Session(db.Model):
    __tablename__ = "session"

    id: Mapped[str] = mapped_column(String, unique=True, primary_key=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="session")
