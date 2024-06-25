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
async def createUser(User :Usuario):
    new_user = Users(name = User.name, role = User.role, token = AuthService.generate_token(User))
    if (Service.validateUsuario(role = User.role)):
        database.addInDatabase(new_user)
        return {"message": "Succes created user"}


@UsuarioController.patch("/Usuario/{user_id}")
async def updateUser(User :Usuario,user_id:str):
    user__to_update:Users = database.findUserInDatabase(Users,user_id)
    user__to_update.role = User.role
    if (Service.validateUsuario(user__to_update.role)):
        database.addInDatabase(user__to_update)
        return {"message": "Succes updated user"}

