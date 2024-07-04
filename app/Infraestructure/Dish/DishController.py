from pydantic import UUID4
from app.Application.Dish.Cmd.Service_Dish_Create import Create_Dish_Parameter, Create_Dish_Service
from app.Application.shared.IService import Service_Type, Result_Type
from app.Application.shared.Service_Handler import Service_Handler
from app.Infraestructure.Dish.DishSQLRepository import DishSQLRepository
from fastapi import APIRouter, Response, status
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

#Inicializacion de los servicios y añadidos al Service_Handler
services.addService(Service_Type.Command_Create, Create_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Query_by_Id, SearchById_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Query_all, SearchAll_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Command_Delete, Delete_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
services.addService(Service_Type.Command_Update, Update_Dish_Service(repository=repositorySQL_dish, food_repository=repositorySQL_ingridient))
#-------------------------------------------------------------

@DishController.post("/Dish", tags=["Dish"], status_code=200)
async def createDish(dto:DishDTO,response: Response):
    #Validar que no se agreguen 2 ids de ingredientes iguales
    ingredient_list:set = set()
    for i in dto.ingredient_id_list:
        ingredient_list.add(i[0])
    if (len(ingredient_list) < len(dto.ingredient_id_list)):
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return Error_Response("repeated ingredient Id")
    #-------------------------------------------------------------

    servicesPO = Create_Dish_Parameter(dto.name, dto.description, dto.price, (dto.ingredient_id_list, dto.instructions))
    response_body = await services.execute(servicesPO)

    if response_body.type == Result_Type.Error:
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:  
        response.status_code = status.HTTP_201_CREATED
    return response_body


@DishController.get("/Dish/{id}", tags=["Dish"], status_code=200)
async def searchDishbyId(id:UUID4,response: Response):
    servicesPO = SearchById_Dish_Parameter(id)
    response_body = await services.execute(servicesPO)

    if response_body.type == Result_Type.Error:
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:  
        response.status_code = status.HTTP_200_OK
    return response_body
    

@DishController.get("/Dish", tags=["Dish"], status_code=200)
async def searchDishAll(response: Response):
    servicesPO = SearchAll_Dish_Parameter()
    response_body = await services.execute(servicesPO)
    
    if response_body.type == Result_Type.Error:
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:  
        
        response.status_code = status.HTTP_200_OK
    return response_body


@DishController.delete("/Dish/{id}", tags=["Dish"], status_code=200)
async def deleteDish(id:UUID4,response: Response):
    servicesPO = Delete_Dish_Parameter(id)
    response_body = await services.execute(servicesPO)

    if response_body.type == Result_Type.Error:
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:  
        response.status_code = status.HTTP_200_OK
    return response_body


@DishController.put("/Dish/{id}", tags=["Dish"], status_code=200)
async def updateDish(dto:DishUpdateDTO,response: Response):
    #Validar que no se agreguen 2 ids de ingredientes iguales
    ingredient_list:set = set()
    for i in dto.ingredient_id_list:
        ingredient_list.add(i[0])
    if (len(ingredient_list) < len(dto.ingredient_id_list)):
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return Error_Response("repeated ingredient Id")
    #-------------------------------------------------------------

    servicesPO = Update_Dish_Parameter(dto.id, dto.name, dto.description, dto.price, (dto.ingredient_id_list, dto.instructions))
    response_body = await services.execute(servicesPO)

    if response_body.type == Result_Type.Error:
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:  
        response.status_code = status.HTTP_200_OK
    return response_body
    

    