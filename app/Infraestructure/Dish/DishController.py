from pydantic import UUID4
from app.Application.Dish.Cmd.Service_Dish_Create import Create_Dish_Parameter, Create_Dish_Service
from app.Application.shared.IService import Service_Type
from app.Application.shared.Service_Handler import Service_Handler
from app.Infraestructure.Dish.DishSQLRepository import DishSQLRepository
from fastapi import APIRouter
from app.Infraestructure.Dtos.DishDTO import DishDTO, DishUpdateDTO
from app.Application.Dish.Query.Service_Dish_ById import SearchById_Dish_Service, SearchById_Dish_Parameter
from app.Application.Dish.Query.Service_Dish_All import SearchAll_Dish_Service, SearchAll_Dish_Parameter
from app.Infraestructure.Ingredient.IngredientSQLRepository import IngredientSQLRepository
from app.Application.Dish.Cmd.Service_Dish_Delete import Delete_Dish_Service, Delete_Dish_Parameter
from app.Application.Dish.Cmd.Service_Dish_Update import Update_Dish_Parameter, Update_Dish_Service
from app.Application.shared.Error_Response import Error_Response

DishController = APIRouter()
services:Service_Handler    = Service_Handler()
repositorySQL_dish          = DishSQLRepository()
repositorySQL_ingridient    = IngredientSQLRepository()

services.addService(Service_Type.Command_Create, Create_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Query_by_Id, SearchById_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Query_all, SearchAll_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Command_Delete, Delete_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Command_Update, Update_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))


@DishController.post("/Dish")
async def createDish(dto:DishDTO):
    ingredient_list:set = set()
    for i in dto.ingredient_id_list:
        ingredient_list.add(i[0])
    if (len(ingredient_list) < len(dto.ingredient_id_list)):
        return Error_Response("repeated ingredient Id")
    
    servicesPO = Create_Dish_Parameter(dto.name, dto.description, dto.price, (dto.ingredient_id_list, dto.instructions))
    return await services.execute(servicesPO)

@DishController.get("/Dish/{id}")
async def searchDishbyId(id:UUID4):
    servicesPO = SearchById_Dish_Parameter(id)
    return await services.execute(servicesPO)
    
@DishController.get("/Dish")
async def searchDishAll():
    servicesPO = SearchAll_Dish_Parameter()
    return await services.execute(servicesPO)

@DishController.delete("/Dish/{id}")
async def deleteDish(id:UUID4):
    servicesPO = Delete_Dish_Parameter(id)
    return await services.execute(servicesPO)

@DishController.put("/Dish/{id}")
async def updateDish(dto:DishUpdateDTO):
    ingredient_list:set = set()
    for i in dto.ingredient_id_list:
        ingredient_list.add(i[0])
    if (len(ingredient_list) < len(dto.ingredient_id_list)):
        return Error_Response("repeated ingredient Id")

    servicesPO = Update_Dish_Parameter(dto.id, dto.name, dto.description, dto.price, (dto.ingredient_id_list, dto.instructions))
    return await services.execute(servicesPO)
    

    