from factory import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Bid(db.Model):
    __tablename__ = "bid"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True, nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey('project.id'), primary_key=True, nullable=False)
    status: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)
    user: Mapped["User"] = relationship(back_populates='bids')
    project: Mapped["Project"] = relationship(back_populates='bids')
