import os
import uuid
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import UUID

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', 5432)
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '0000')
DB_NAME = os.environ.get('DB_NAME', 'prueba1')
connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


engine = create_engine(connection_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class dataBaseSession():
    def createTables():
        Base.metadata.create_all(engine)
    def addInDatabase(T: any):
        session.add(T)
        session.commit()

    def findInDatabase(T:any,id:str):
        Instance_object = session.query(T).get(id)
        return Instance_object
   
    def findAllInDatabase(T:any):
        Instance_object = session.query(T).all()
        return Instance_object

class Users(Base):
    __tablename__ = "Users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(36))
    role = Column(String(36))
    token = Column(String(1024), nullable=True)

class DishBD(Base):
    __tablename__ = "Dish"
    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name          = Column(String(30))
    description   = Column(String(500))
    price         = Column(Float)

