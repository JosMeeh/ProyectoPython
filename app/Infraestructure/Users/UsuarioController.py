##Todos los controladores/endpoints de usuario aca
from app.Infraestructure.Dtos.UsuarioDTO import Usuario
from app.Services.Users.UsuarioService import UsuarioService
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession,Users
from app.Infraestructure.Authentication import AuthService
from fastapi import APIRouter

Service = UsuarioService()
database = dataBaseSession
UsuarioController = APIRouter()

@UsuarioController.post("/Usuario")
async def hello(User :Usuario):
    new_topic = Users(name = User.name, role = User.role, token = AuthService.generate_token(User))
    if (Service.validateUsuario(role = User.role)):
        database.addInDatabase(new_topic)
        return {"message": "Succes created user"}
    else: return {"message": "El rol que intenta crear no esta permitido"}


