from abc import ABC, abstractmethod

class UsuarioInterfaces(ABC):
    @abstractmethod
    def validateUsuario(arg:str) -> bool:
        pass