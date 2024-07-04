import os
import uuid
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import UUID
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
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
    def createTables():
        Base.metadata.create_all(engine)
    def addInDatabase(T: any):
        session.add(T)
        session.commit()
        return T

    def findInDatabase(T:any,id:str):
        Instance_object = session.query(T).get(id)
        if Instance_object:
            return Instance_object
        else: return None
   
    def findAllInDatabase(T:any):
        Instance_object = session.query(T).all()
        return Instance_object
    
    def findInDatabase(T:any,id:str):
        Instance_object = session.query(T).get(id)
        return Instance_object

    def deleteInDatabase(T:any,id:str):
        Delete_Object = session.query(T).get(id)
        if Delete_Object:
            session.delete(Delete_Object)
            session.commit()
            return True
        else: False

    def updateInDatabase(T:any, id:str, values:dict):
        Instance_object = session.query(T).update(values)
        if Instance_object:
            session.commit()
            return True
        else: False

    def findIngredientsOfDish(id:str):
        Instance_object = session.query(Recipe_IngredientBD).filter(Recipe_IngredientBD.id_Dish == id).all()
        return Instance_object
    def findDishesofOrder(id:str):
        Instance_object = session.query(Order_DishesBD).filter(Order_DishesBD.id_Order == id).all()
        return Instance_object

    def deletDishofOrders(id:str):
        Delete_Object = session.query(Order_DishesBD).filter(Order_DishesBD.id_Order == id).delete(synchronize_session=False)
        if Delete_Object:
            session.commit()
            return True
        else: False

    def deleteIngredientsOfDish(id:str):
        Delete_Object = session.query(Recipe_IngredientBD).filter(Recipe_IngredientBD.id_Dish == id).delete(synchronize_session=False)
        if Delete_Object:
            session.commit()
            return True
        else: False

    def findDishesOfMenu(id:str):
        Instance_object = session.query(Menu_DishesBD).filter(Menu_DishesBD.id_Menu == id).all()
        return Instance_object
    
    def deleteDishesOfMenu(id:str):
        Delete_Object = session.query(Menu_DishesBD).filter(Menu_DishesBD.id_Menu == id).delete(synchronize_session=False)
        if Delete_Object:
            session.commit()
            return True
        else: False





class Users(Base):
    __tablename__ = "Users"
    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name          = Column(String(36))
    role          = Column(String(36))
    token         = Column(String(1024), nullable=True)

class DishBD(Base):
    __tablename__ = "Dish"
    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name          = Column(String(30))
    description   = Column(String(500))
    price         = Column(Float)
    instructions = Column(String(1000))

class IngredientBD(Base):
    __tablename__ = "Ingredient"
    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name          = Column(String(100))
    amount        = Column(Integer)

class OrderDB(Base):
    __tablename__ = "Order"
    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_name   = Column(String(30))
    price         = Column(Float)


class MenuDB(Base):
    __tablename__ = "Menu"
    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name          = Column(String(30))


class Order_DishesBD(Base):
    __tablename__ = "Order_Dishes"
    id_Order       = Column(ForeignKey(OrderDB.id), primary_key=True)
    id_Dish        = Column(ForeignKey(DishBD.id),  primary_key=True)
    amount         = Column(Integer)


class Recipe_IngredientBD(Base):
    __tablename__ = "Recipe_Ingredient"
    id_Dish       = Column(ForeignKey(DishBD.id), primary_key=True)
    id_Ingredient = Column(ForeignKey(IngredientBD.id), primary_key=True)
    amount        = Column(Integer)

class Menu_DishesBD(Base):
    __tablename__ = "Menu_Dishes"
    id_Dish       = Column(ForeignKey(DishBD.id), primary_key=True)
    id_Menu       = Column(ForeignKey(MenuDB.id), primary_key=True)