from .db import db, environment, SCHEMA, add_prefix_for_prod


class Game(db.Model):
    __tablename__ = 'games'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('categories.id')), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('publishers.id')), nullable=False)
    platform_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('platforms.id')), nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_rating = db.Column(db.Float(2))
    metacritic_rating = db.Column(db.Float(2))
    description = db.Column(db.String(1000))
    release_date = db.Column(db.Date)
