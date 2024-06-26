from app.Services.Users.UsuarioInterface import UsuarioInterfaces
from app.Infraestructure.Database import dataBaseConfig
from app.Infraestructure.Authentication import AuthService
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession,Users
from app.Infraestructure.Dtos.UsuarioDTO import Usuario
database = dataBaseSession

class UsuarioService(UsuarioInterfaces):
    ROLES_PERMITIDOS = ["Administrador", "Chef", "Camarero", "Cliente"]

    def validateUsuario(self, role: str):
        if role not in self.ROLES_PERMITIDOS:
            return False
        else:
            return True
    def addUser(self,User:any):
        new_user = Users(name=User.name, role=User.role, token=AuthService.generate_token(User))
        if (self.validateUsuario(role = User.role)):
            database.addInDatabase(new_user)
            return {"message": "Succes created user"}

    def updateUser(self,User:any, userd_id:str):
        user__to_update: Users = database.findUserInDatabase(Users, userd_id)
        user__to_update.role = User.role
        if (self.validateUsuario(user__to_update.role)):
            database.addInDatabase(user__to_update)
            return {"message": "Succes updated user"}


