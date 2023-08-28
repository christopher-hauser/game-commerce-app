from .db import db, environment, SCHEMA, add_prefix_for_prod


class OrderDetail(db.Model):
    __tablename__ = 'orderDetails'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('payments.id')), nullable=False)
    created_at = db.Column(db.Date)
    total = db.Column(db.Float(2))
