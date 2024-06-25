from abc import ABC, abstractmethod

class UsuarioInterfaces(ABC):
    @abstractmethod
    def validateUsuario(self,arg:str) -> bool:
        pass