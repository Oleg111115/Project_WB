from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///WB.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Таблица "Пользователи"
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))

    queries = relationship("Query", backref="user")

# Таблица "Запросы"
class Query(Base):
    __tablename__ = 'queries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    query = Column(String(255))
    discount = Column(Float)
    created_at = Column(DateTime, default=datetime.now)

    products = relationship("Product", secondary="products_queries", backref="queries")
    notifications = relationship("Notification", backref="query")

# Таблица "Продукты"
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.now)

    queries = relationship("Query", secondary="products_queries", backref="products")
    history = relationship("History", backref="product")

# Таблица "Продукты_Запросы" (связующая таблица многие ко многим)
products_queries = Table('products_queries', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True),
    Column('query_id', Integer, ForeignKey('queries.id'), primary_key=True)
)

# Таблица "Уведомления"
class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    query_id = Column(Integer, ForeignKey('queries.id'))
    previous_price = Column(Float)
    current_price = Column(Float)
    created_at = Column(DateTime)

    product = relationship("Product", backref="notifications")

# Таблица "История"
class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    created_at = Column(DateTime, default=datetime.now)
    price = Column(Float)
    product = relationship("Product", backref="history")

# Создание таблиц
Base.metadata.create_all(engine)

# Закрытие соединения с базой данных
session.close()
