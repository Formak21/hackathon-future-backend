from typing import List, Optional
from factory import db
from sqlalchemy import String, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserProjectAssociation(db.Model):
    __tablename__ = "user_project_association"

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True, nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey('project.id'), primary_key=True, nullable=False)

    role: Mapped[str] = mapped_column(String)

    user: Mapped["User"] = relationship(back_populates='projects')
    project: Mapped["Project"] = relationship(back_populates='users')


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

    users: Mapped[List["UserProjectAssociation"]] = relationship(back_populates='project')
    bids: Mapped[List["Bid"]] = relationship(back_populates='project')
