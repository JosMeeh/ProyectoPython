##Todos los controladores/endpoints de usuario aca
from app.Domain.Users.UsuarioClass import Usuario
import app.Services.Users.UsuarioService as UsuarioService
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession,Users
from app.Infraestructure.Authentication import AuthService
from fastapi import APIRouter

database = dataBaseSession
UsuarioController = APIRouter()

@UsuarioController.post("/Usuario")
async def hello(User :Usuario):
    new_topic = Users(name = User.name, role = User.role, token = AuthService.generate_token(User))
    if (UsuarioService.validateUsuario(role = User.role)):
        database.addInDatabase(new_topic)
        return {"message": "Succes created user"}