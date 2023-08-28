from .db import db, environment, SCHEMA, add_prefix_for_prod


class OrderItem(db.Model):
    __tablename__ = 'orderItems'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('orderDetails.id')), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('games.id')), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
