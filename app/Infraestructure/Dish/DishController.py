##Todos los controladores/endpoints de usuario aca
from app.Application.Dish.Cmd.Service_Dish_Create import Create_Dish_Parameter, Create_Dish_Service
from app.Application.shared.IService import Service_Type
from app.Application.shared.Service_Handler import Service_Handler
from app.Infraestructure.Dish.DishSQLRepository import DishSQLRepository
from fastapi import APIRouter
from app.Infraestructure.Dtos.DishDTO import DishDTO

DishController = APIRouter()
services:Service_Handler = Service_Handler()
services.addService(Service_Type.Command_Create, Create_Dish_Service(repository=DishSQLRepository()))

@DishController.post("/Dish")
async def createDish(dto:DishDTO):
    servicesPO = Create_Dish_Parameter(dto.name, dto.description, dto.price, (dto.ingridient_id_list, dto.instructions))
    return await services.execute(servicesPO)
    

    

    