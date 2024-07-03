from pydantic import UUID4
from app.Application.Menu.Cmd.Service_Menu_Create import Create_Menu_Parameter, Create_Menu_Service
from app.Application.shared.IService import Service_Type
from app.Application.shared.Service_Handler import Service_Handler
from app.Infraestructure.Dish.DishSQLRepository import DishSQLRepository
from fastapi import APIRouter
from app.Infraestructure.Dtos.MenuDTO import MenuDTO, MenuUpdateDTO
from app.Application.Menu.Query.Service_Menu_ById import SearchById_Menu_Service, SearchById_Menu_Parameter
from app.Application.Menu.Query.Service_Menu_All import SearchAll_Menu_Service, SearchAll_Menu_Parameter
from app.Infraestructure.Menu.MenuSQLRepository import MenuSQLRepository
from app.Application.Menu.Cmd.Service_Menu_Delete import Delete_Menu_Service, Delete_Menu_Parameter
from app.Application.Menu.Cmd.Service_Menu_Update import Update_Menu_Service, Update_Menu_Parameter

MenuController = APIRouter()
services:Service_Handler    = Service_Handler()
repositorySQL_dish          = DishSQLRepository()
repositorySQL_menu          = MenuSQLRepository()

services.addService(Service_Type.Command_Create, Create_Menu_Service(repository=repositorySQL_menu,food_repository=repositorySQL_dish))
services.addService(Service_Type.Query_by_Id, SearchById_Menu_Service(repository=repositorySQL_menu,food_repository=repositorySQL_dish))
services.addService(Service_Type.Query_all, SearchAll_Menu_Service(repository=repositorySQL_menu,food_repository=repositorySQL_dish))
services.addService(Service_Type.Command_Delete, Delete_Menu_Service(repository=repositorySQL_menu,food_repository=repositorySQL_dish))
services.addService(Service_Type.Command_Update, Update_Menu_Service(repository=repositorySQL_menu,food_repository=repositorySQL_dish))

@MenuController.post("/Menu")
async def createMenu(dto:MenuDTO):
    servicesPO = Create_Menu_Parameter(dto.name, dto.dish_list)
    return await services.execute(servicesPO)

@MenuController.get("/Menu/{id}")
async def searchMenubyId(id:UUID4):
    servicesPO = SearchById_Menu_Parameter(id)
    return await services.execute(servicesPO)
    
@MenuController.get("/Menus")
async def searchMenuAll():
    servicesPO = SearchAll_Menu_Parameter()
    return await services.execute(servicesPO)

@MenuController.delete("/Menu/{id}")
async def deleteMenu(id:UUID4):
    servicesPO = Delete_Menu_Parameter(id)
    return await services.execute(servicesPO)

@MenuController.put("/Menu/{id}")
async def updateMenu(dto:MenuUpdateDTO):
    servicesPO = Update_Menu_Parameter(dto.id, dto.name, dto.dish_list)
    return await services.execute(servicesPO)
    

    