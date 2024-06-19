from pydantic import BaseModel
from enum import Enum
import json

ROLES_PERMITIDOS = ["Administrador", "Chef", "Camarero", "Cliente"]
class Usuario(BaseModel):
    name:str
    role :str
    def validateUsuario(role:str):
        if role not in ROLES_PERMITIDOS:
            raise ValueError(f"El rol '{role}' no es válido. Los roles permitidos son: {', '.join(ROLES_PERMITIDOS)}")
            return False
        else: return True