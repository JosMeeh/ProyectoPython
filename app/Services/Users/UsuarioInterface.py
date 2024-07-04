from abc import ABC, abstractmethod

class UsuarioInterfaces(ABC):
    @abstractmethod
    def addUser(self,User:any):
        pass

    @abstractmethod
    def updateUser(self,User: any, userd_id: str):
        pass

    @abstractmethod
    def deleteUser(self, User: any, userd_id: str):
        pass

    @abstractmethod
    def getUserById(self,userd_id: str):
        pass

    @abstractmethod
    def getAllUsers(self):
        pass