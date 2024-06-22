import os
import uuid
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import UUID

DBHOST = os.environ.get('DB_HOST', 'localhost')
DBPORT = os.environ.get('DB_PORT', 5432)
DBUSER = os.environ.get('DB_USER', 'postgres')
DBPASSWORD = os.environ.get('DB_PASSWORD', '12345678')
DBNAME = os.environ.get('DBNAME', 'proyecto')

connection_string = f'postgresql://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBNAME}'
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

class Users(Base):
    __tablename__ = "Users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(36))
    role = Column(String(36))
    token = Column(String(1024), nullable=True)

