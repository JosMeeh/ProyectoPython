##Todos los controladores/endpoints de usuario aca
from app.Domain.Usuario.UsuarioClass import Usuario
import app.Domain.Usuario.UsuarioService as UsuarioService
from app.Services.Database.dataBaseConfig import dataBaseSession,Users
from app.Services.Authentication import AuthService
from fastapi import APIRouter

database = dataBaseSession
UsuarioController = APIRouter()

@UsuarioController.post("/Usuario")
async def hello(User :Usuario):
    new_topic = Users(name = User.name, role = User.role, token = AuthService.generate_token(User))
    if (UsuarioService.validateUsuario(role = User.role)):
        database.addInDatabase(new_topic)
        return {"message": "Succes created user"}