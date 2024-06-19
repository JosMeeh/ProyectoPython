from jose import jwt
from app.Domain.Usuario import Usuario
# Función para generar un token JWT

def generate_token(Usuario:Usuario):
    payload = {
        "name": Usuario.name,
        "role": Usuario.role
    }
    secret_key = Usuario.role
    return jwt.encode(payload, secret_key, algorithm="HS256")

# Función para decodificar un token JWT
def verifyAcces(token,role:str):
    try:
        Decode_Token = jwt.decode(token, role, algorithms=["HS256"])
        if "role" in Decode_Token and Decode_Token["role"] == role:
            print("Authorize")
            return True
        else:
            print("UnAuthorize")

    except jwt.ExpiredSignatureError:
        return None
    except jwt.JWTClaimsError:
        return None
