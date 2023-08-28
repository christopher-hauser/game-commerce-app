from .db import db, environment, SCHEMA, add_prefix_for_prod


class Publisher(db.Model):
    __tablename__ = 'publishers'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255))
    site_link = db.Column(db.String(1000))
