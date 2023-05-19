from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Таблица "Пользователи"
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))


# Таблица "Запросы"
class Query(db.Model):
    __tablename__ = 'queries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    query = db.Column(db.String(255))
    discount = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user = db.relationship("User", backref="queries")


# Таблица "Продукты"
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    previous_price = db.Column(db.Float)
    updated_at = db.Column(db.DateTime)

    queries = db.relationship('Query', secondary='products_queries', backref='products')


# Таблица "Продукты_Запросы" (связующая таблица многие ко многим)
products_queries = db.Table('products_queries',
                            db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
                            db.Column('query_id', db.Integer, db.ForeignKey('queries.id'), primary_key=True)
                            )


# Таблица "Уведомления"
class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    query_id = db.Column(db.Integer, db.ForeignKey('queries.id'))
    previous_price = db.Column(db.Float)
    current_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime)

    product = db.relationship("Product", backref="notifications")
    query = db.relationship("Query", backref="notifications")
