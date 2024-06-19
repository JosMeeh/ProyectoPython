from fastapi import FastAPI
from app.Services.Database.dataBaseConfig import dataBaseSession,Users
import json
from app.Domain.Usuario import UsuarioController
from app.Services.Authentication import AuthService
from app.Domain.Usuario.UsuarioController import UsuarioController
app = FastAPI()
app.include_router(UsuarioController)
database = dataBaseSession
database.createTables()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/access/{token}")
async def verifyToken(token:str):
    if (AuthService.verifyAccess(token, "Camarero")):
        return {"message": "Authorized"}
    else:
        return {"message": "UnAuthorized"}

##pip install SQLAlchemy
##pip install psycopg2-binary
##pip install python-jose (Si)
##Ejecuten estos comandos para poder correr la aplicacion
