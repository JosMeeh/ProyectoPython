from fastapi import FastAPI
from app.Application.Dish.Cmd.Service_Dish_Create import Create_Dish_Parameter, Create_Dish_Service
from app.Application.shared.IService import Service_Type
from app.Application.shared.Service_Handler import Service_Handler
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession
from app.Infraestructure.Ingredient.IngredientController import IngredientController
from app.Infraestructure.Authentication import AuthService
from app.Infraestructure.Dtos.DishDTO import DishDTO
from app.Infraestructure.Menu.MenuController import MenuController
from app.Infraestructure.Users.UsuarioController import UsuarioController
from app.Infraestructure.Dish.DishController import DishController
from app.Infraestructure.Order.OrderController import OrderController
from alembic import command
from alembic.config import Config
app = FastAPI()
config = Config('alembic.ini') # Lee la configuración de Alembic
command.upgrade(config, 'head') # Ejecutar la migración

app.include_router(DishController)
app.include_router(UsuarioController)
app.include_router(IngredientController)
app.include_router(OrderController)
app.include_router(MenuController)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/access/{token}")
async def verifyToken(token:str):
    if (AuthService.verifyAccess(token, ["Camarero", "admin", "chef"])):
        return {"message": "Authorized"}
    else:
        return {"message": "UnAuthorized"}
    

##pip install alembic
##pip install SQLAlchemy
##pip install psycopg2-binary
##pip install python-jose
##Ejecuten estos comandos para poder correr la aplicacion



##PARA LAS MIGRACIONES

#alembic revision --autogenerate -m "Nombre de migracion"
# (Este comando crea una nueva migracion con la estructura definida en SQLAlchemy (El archivo dataBaseConfig))


##alembic upgrade head
# (Este comando actualiza la migracion, cosa que al ejecutar el codigo se cree con los cambios que realizaron en la base de datos)

