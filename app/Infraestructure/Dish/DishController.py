##Todos los controladores/endpoints de usuario aca
from app.Application.Dish.Cmd.Service_Dish_Create import Create_Dish_Parameter, Create_Dish_Service
from app.Application.shared.IService import Service_Type
from app.Application.shared.Service_Handler import Service_Handler
from app.Infraestructure.Dish.DishSQLRepository import DishSQLRepository
from fastapi import APIRouter
from app.Infraestructure.Dtos.DishDTO import DishDTO
from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe

DishController = APIRouter()
services:Service_Handler = Service_Handler()
repositorySQL = DishSQLRepository()
services.addService(Service_Type.Command_Create, Create_Dish_Service(repository=repositorySQL))

@DishController.post("/Dish")
async def createDish(dto:DishDTO):
    servicesPO = Create_Dish_Parameter(dto.name, dto.description, dto.price, (dto.ingridient_id_list, dto.instructions))
    return await services.execute(servicesPO)

@DishController.get("/Dish/{id}")
async def createDish(id:str):
    test_dish = await repositorySQL.searchDishbyId(Id_Dish(id))
    

    

    