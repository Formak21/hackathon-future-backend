from typing import List, Optional
from factory import db
from sqlalchemy import String, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Feed(db.Model):
    __tablename__ = "feed"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)

    title: Mapped[str] = mapped_column(String)
    format: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(String)

    url_for_preview: Mapped[Optional[str]] = mapped_column(String)

    tags: Mapped[List[str]] = mapped_column(ARRAY(String))

    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"))
    project: Mapped["Project"] = relationship(back_populates="feed")
