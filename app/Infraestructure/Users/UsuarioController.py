##Todos los controladores/endpoints de usuario aca
from app.Infraestructure.Dtos.UsuarioDTO import Usuario
from app.Services.Users.UsuarioService import UsuarioService
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession,Users
from app.Infraestructure.Authentication import AuthService
from fastapi import APIRouter

Service = UsuarioService()
UsuarioController = APIRouter()

@UsuarioController.post("/Usuario")
async def createUser(User :Usuario):
   return Service.addUser(User)


@UsuarioController.patch("/Usuario/{user_id}")
async def updateUser(User :Usuario,user_id:str):
        return Service.updateUser(User,user_id)

