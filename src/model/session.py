from src.factory import dbModel
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Session(dbModel):
    __tablename__ = "session"

    session_id: Mapped[str] = mapped_column(String, unique=True, primary_key=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="session")
