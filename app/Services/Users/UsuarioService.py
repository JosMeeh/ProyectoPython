from app.Services.Users.UsuarioInterface import UsuarioInterfaces
class UsuarioService(UsuarioInterfaces):
    ROLES_PERMITIDOS = ["Administrador", "Chef", "Camarero", "Cliente"]

    def validateUsuario(self, role: str) -> bool:
        if role not in self.ROLES_PERMITIDOS:
            return False
        else:
            return True


