##Todos los controladores/endpoints de usuario aca
from pydantic import UUID4
from app.Application.Ingredient.Cmd.Service_Ingredient_Create import Create_Ingredient_Parameter, Create_Ingredient_Service
from app.Application.shared.IService import Service_Type
from app.Application.shared.Service_Handler import Service_Handler
from app.Infraestructure.Ingredient.IngredientSQLRepository import IngredientSQLRepository
from fastapi import APIRouter
from app.Infraestructure.Dtos.IngredientDTO import IngredientDTO, IngredientUpdateDTO
from app.Application.Ingredient.Query.Service_Ingredient_ById import SearchById_Ingredient_Service, SearchById_Ingredient_Parameter
from app.Application.Ingredient.Query.Service_Ingredient_All import SearchAll_Ingredient_Service, SearchAll_Ingredient_Parameter
from app.Infraestructure.Ingredient.IngredientSQLRepository import IngredientSQLRepository
from app.Application.Ingredient.Cmd.Service_Ingredient_Delete import Delete_Ingredient_Service, Delete_Ingredient_Parameter
from app.Application.Ingredient.Cmd.Service_Ingredient_Update import Update_Ingredient_Parameter, Update_Ingredient_Service

IngredientController = APIRouter()
services: Service_Handler = Service_Handler()
repositorySQL = IngredientSQLRepository()
services.addService(Service_Type.Command_Create, Create_Ingredient_Service(repository=repositorySQL))
services.addService(Service_Type.Query_by_Id, SearchById_Ingredient_Service(repository=repositorySQL))
services.addService(Service_Type.Query_all, SearchAll_Ingredient_Service(repository=repositorySQL))
services.addService(Service_Type.Command_Delete, Delete_Ingredient_Service(repository=repositorySQL))
services.addService(Service_Type.Command_Update, Update_Ingredient_Service(repository=repositorySQL))


@IngredientController.post("/Ingredient")
async def createIngredient(dto: IngredientDTO):
    servicesPO = Create_Ingredient_Parameter(dto.name, dto.amount)
    return await services.execute(servicesPO)


@IngredientController.get("/Ingredient/{id}")
async def searchIngredientbyId(id:UUID4):
    servicesPO = SearchById_Ingredient_Parameter(id)
    return await services.execute(servicesPO)

@IngredientController.get("/Ingredient")
async def searchIngredientAll():
    servicesPO = SearchAll_Ingredient_Parameter()
    return await services.execute(servicesPO)

@IngredientController.delete("/Ingredient/{id}")
async def deleteIngredient(id:UUID4):
    servicesPO = Delete_Ingredient_Parameter(id)
    return await services.execute(servicesPO)

@IngredientController.put("/Ingredient/{id}")
async def updateIngredient(dto:IngredientUpdateDTO):
    servicesPO = Update_Ingredient_Parameter(dto.id, dto.name, dto.amount)
    return await services.execute(servicesPO)
