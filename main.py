from fastapi import FastAPI
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession
from app.Infraestructure.Authentication import AuthService
from app.Infraestructure.Users.UsuarioController import UsuarioController
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
##pip install python-jose
##Ejecuten estos comandos para poder correr la aplicacion
