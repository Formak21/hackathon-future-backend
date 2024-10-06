from typing import List, Optional
from factory import db
from sqlalchemy import String, ForeignKey, ARRAY, ForeignKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Chat(db.Model):
    pass