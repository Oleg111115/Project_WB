from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///WB.db')

Session = sessionmaker(bind=engine)
session = Session()

# создаем базовый класс, от которого будут наследоваться все остальные классы-модели
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Query(Base):
    __tablename__ = 'queries'

    query_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    query = Column(String)
    discount = Column(Float)

    user = relationship("User", backref="queries")

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    query_id = Column(Integer, ForeignKey('queries.query_id'))
    name = Column(String)
    price = Column(Float)
    previous_price = Column(Float)
    updated_at = Column(DateTime)

    query = relationship("Query", backref="products")

# Создание таблиц
Base.metadata.create_all(engine)

# Закрытие соединения с базой данных
session.close()
