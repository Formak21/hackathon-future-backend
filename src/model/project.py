from typing import List, Optional
from src.factory import db
from sqlalchemy import String, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Project(db.Model):
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)

    title: Mapped[str] = mapped_column(String)
    goals: Mapped[str] = mapped_column(String)
    region: Mapped[str] = mapped_column(String)

    short_info: Mapped[Optional[str]] = mapped_column(String)
    contacts: Mapped[Optional[str]] = mapped_column(String)
    requirements: Mapped[Optional[str]] = mapped_column(String)
    format: Mapped[Optional[str]] = mapped_column(String)
    url_for_preview: Mapped[Optional[str]] = mapped_column(String)

    tags: Mapped[List[str]] = mapped_column(ARRAY(String))
    docs: Mapped[List[str]] = mapped_column(ARRAY(String))

    head: Mapped["User"] = relationship(back_populates="user")



