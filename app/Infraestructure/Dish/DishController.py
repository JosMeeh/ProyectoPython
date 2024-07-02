##Todos los controladores/endpoints de usuario aca
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

DishController = APIRouter()
services:Service_Handler    = Service_Handler()
repositorySQL_dish          = DishSQLRepository()
repositorySQL_ingridient    = IngredientSQLRepository()

services.addService(Service_Type.Command_Create, Create_Dish_Service(repository=repositorySQL_dish))
services.addService(Service_Type.Query_by_Id, SearchById_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Query_all, SearchAll_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Command_Delete, Delete_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Command_Update, Update_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))


@DishController.post("/Dish")
async def createDish(dto:DishDTO):
    servicesPO = Create_Dish_Parameter(dto.name, dto.description, dto.price, (dto.ingridient_id_list, dto.instructions))
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
    servicesPO = Update_Dish_Parameter(dto.id, dto.name, dto.description, dto.price, (dto.ingridient_id_list, dto.instructions))
    return await services.execute(servicesPO)

@DishController.patch("/test")
async def test():
    from app.Infraestructure.Database.dataBaseConfig import Recipe_IngredientBD, dataBaseSession,DishBD
    from app.Domain.Dish.Dish_VO import Recipe, Id_Dish, Name_Dish, Description_Dish, Price_Dish
    from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient
    database = dataBaseSession
    print("test1")
    response = await repositorySQL_dish.updateDish(Id_Dish("1a0ef5f6-3e0d-4ee2-9dbf-b0a477007579"),
                                                    Name_Dish("papas al horno"),
                                                    Description_Dish("sabrosas papas horneadas con mantequilla de mammut"),
                                                    Price_Dish(5.5),
                                                    Recipe([
                                                         (Id_Ingredient("31f2624c-3402-4011-81fc-5d03eee14555"), 2)
                                                         ], "cocinar la comida"))
    return response
    

    