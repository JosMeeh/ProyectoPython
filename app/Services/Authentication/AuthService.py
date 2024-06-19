from jose import jwt
from app.Domain.Usuario.UsuarioClass import Usuario
# Función para generar un token JWT

def generate_token(Usuario:Usuario):
    payload = {
        "name": Usuario.name,
        "role": Usuario.role
    }
    secret_key = Usuario.role
    return jwt.encode(payload, secret_key, algorithm="HS256")

# Función para decodificar un token JWT
def verifyAccess(token,role:str):
    try:
        Decode_Token = jwt.decode(token, role, algorithms=["HS256"])
        print(Decode_Token)
        if "role" in Decode_Token and Decode_Token["role"] == role:
            print("Authorize")
            return True
        else:
            print("UnAuthorize")
            return False
    except jwt.ExpiredSignatureError:
        return False
    except jwt.JWTClaimsError:
        return False
    except jwt.JWTError as e:
        return False
    except Exception as e:
        return False
def verifyAccessAdmin(token):
    try:
        Decode_Token = jwt.decode(token, "Administrador", algorithms=["HS256"])
        print(Decode_Token)
        if "role" in Decode_Token and Decode_Token["role"] == "Administrador":
            print("Authorize")
            return True
        else:
            print("UnAuthorize")
            return False
    except jwt.ExpiredSignatureError:
        return False
    except jwt.JWTClaimsError:
        return False
    except jwt.JWTError as e:
        return False
    except Exception as e:
        return False