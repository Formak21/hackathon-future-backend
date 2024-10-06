from typing import List, Optional
from factory import db
from sqlalchemy import String, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Bid(db.Model):
    __tablename__ = "bid"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True, nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey('project.id'), primary_key=True, nullable=False)

    user: Mapped["User"] = relationship(back_populates='projects')
    project: Mapped["Project"] = relationship(back_populates='users')

