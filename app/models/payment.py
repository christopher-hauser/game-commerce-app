from .db import db, environment, SCHEMA, add_prefix_for_prod


class Payment(db.Model):
    __tablename__ = 'payments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    payment_type = db.Column(db.String(255), nullable=False)
    provider = db.Column(db.String(255), nullable=False)
    account_no = db.Column(db.String(16), nullable=False)
    expiry = db.Column(db.Date, nullable=False)
