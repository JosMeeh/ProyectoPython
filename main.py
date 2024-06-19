from fastapi import FastAPI
from app.Services.Database.dataBaseConfig import dataBaseSession,Users
import json
from app.Services.Authentication import Auth_service
from app.Domain.Usuario import Usuario
app = FastAPI()
database = dataBaseSession
database.createTables()



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/hello")
async def hello(User :Usuario):
    new_topic = Users(name = User.name, role = User.role, token = Auth_service.generate_token(User))
    if Usuario.validateUsuario(User.role):
        database.addInDatabase(new_topic)
        return {"message": "Succes created user"}


@app.get("/access/{token}")
async def verifyToken(token:str):
    Auth_service.verifyAcces(token,"Administrador")
    return {"message": "Welcome to System "}

##pip install SQLAlchemy
##pip install psycopg2-binary
##pip install python-jose (Si)
##Ejecuten estos comandos para poder correr la aplicacion
