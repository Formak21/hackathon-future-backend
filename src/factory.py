from flask import Flask
from flask.json.provider import DefaultJSONProvider
from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class UpdatedJSONProvider(DefaultJSONProvider):
    def default(self, o):
        if isinstance(o, date) or isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://user:pass@psql_cont:5432/dbtest"
app.json = UpdatedJSONProvider(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app, model_class=Base)
