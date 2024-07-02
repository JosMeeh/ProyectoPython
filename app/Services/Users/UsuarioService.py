import json

from app.Services.Users.UsuarioInterface import UsuarioInterfaces
from app.Infraestructure.Database import dataBaseConfig
from app.Infraestructure.Authentication import AuthService
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession,Users
from app.Infraestructure.Dtos.UsuarioDTO import Usuario
database = dataBaseSession

from app.Infraestructure.Database import dataBaseConfig
from app.Infraestructure.Authentication import AuthService
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession,Users
from app.Infraestructure.Dtos.UsuarioDTO import Usuario
database = dataBaseSession

class UsuarioService(UsuarioInterfaces):
    ROLES_PERMITIDOS = ["Administrador", "Chef", "Camarero", "Cliente"]

    def validateUsuario(self, role: str):
        if role in self.ROLES_PERMITIDOS:
            return True
        else:
            return False

    def addUser(self,User:any):
        new_user = Users(name=User.name, role=User.role, token=AuthService.generate_token(User))
        if (self.validateUsuario(role = User.role)):
            database.addInDatabase(new_user)
            return {"message": "Succes created user"}

    def updateUser(self,User:any, userd_id:str):
        user__to_update: Users = database.findInDatabase(Users, userd_id)
        if user__to_update:
            user__to_update.role = User.role
            if (self.validateUsuario(user__to_update.role)):
                database.addInDatabase(user__to_update)
                return {"message": "Succes updated user"}
            else: return {"message": "Error invalid role, please use: Administrador, Chef, Camarero"}
        else: return {"message": "User not found"}

    def deleteUser(self,userd_id: str):
        print(userd_id)
        if database.deleteInDatabase(Users,userd_id):
            return {"message": "Succes deleted user"}
        else: return {"message":"User not found"}

    def getUserById(self,userd_id: str):
        User_to_get:Users =  database.findInDatabase(Users,userd_id)
        if User_to_get:
            Print_User ={
                "Nombre": User_to_get.name,
                "Rol": User_to_get.role,
                "Token": User_to_get.token
            }
            return Print_User
        else: return {"message":"User not found"}

    def getAllUsers(self):
        all_users:Users = database.findAllInDatabase(Users)
        User_list =[]
        for user in all_users:
            Print_User ={
            "Nombre": user.name,
            "Rol": user.role,
            "Token": user.token
            }
            User_list.append(Print_User)
        return User_list