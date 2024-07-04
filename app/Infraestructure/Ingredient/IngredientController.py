##Todos los controladores/endpoints de usuario aca
from app.Application.Dish.Cmd.Service_Dish_Create import Create_Dish_Parameter, Create_Dish_Service
from app.Application.Ingredient.Cmd.Service_Ingredient_Create import Create_Ingredient_Service, \
    Create_Ingredient_Parameter
from app.Application.shared.IService import Service_Type
from app.Application.shared.Service_Handler import Service_Handler
from fastapi import APIRouter

from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient
from app.Infraestructure.Dtos.IngredientDTO import IngredientDTO
from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe
from app.Infraestructure.Ingredient.IngredientSQLRepository import IngredientSQLRepository

IngredientController = APIRouter()
services: Service_Handler = Service_Handler()
repositorySQL = IngredientSQLRepository()
services.addService(Service_Type.Command_Create, Create_Ingredient_Service(repository=repositorySQL))


@IngredientController.post("/Ingredient",  tags=["Ingredient"])
async def createIngredient(dto: IngredientDTO):
    servicesPO = Create_Ingredient_Parameter(dto.name, dto.amount)
    return await services.execute(servicesPO)


@IngredientController.get("/Ingredient/{id}",  tags=["Ingredient"])
async def createIngredient(id: str):
    test_ingredient = await repositorySQL.searchIngredientbyId(Id_Ingredient(id))
    jsonIngredient = {"id": test_ingredient.getId(), "name": test_ingredient.name_Ingredient, "amount": test_ingredient.amount_Ingredient}
    return jsonIngredient

