from datetime import datetime
from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    stock = db.Column(db.Integer, default=0)
    minimum = db.Column(db.Integer, default=0)

    transactions = db.relationship('Transaction', backref='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.name}>'

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # IN or OUT
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Transaction {self.type} {self.quantity}>'
