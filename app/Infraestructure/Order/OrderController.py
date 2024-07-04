from app.Application.Order.Cmd.Service_Order_Create import Create_Order_Parameter, Create_Order_Service
from app.Application.Order.Query.Service_Order_Byid import SearchById_Order_Service, SearchById_Order_Parameter
from app.Application.Order.Query.Service_Order_all import SearchAll_Order_Service,SearchAll_Order_Parameter

from app.Application.shared.IService import Service_Type
from app.Application.shared.Service_Handler import Service_Handler
from app.Infraestructure.Order.OrderSQLRepository import OrderSQLRepository
from app.Infraestructure.Dish.DishSQLRepository import DishSQLRepository
from fastapi import APIRouter
from app.Infraestructure.Dtos.OrderDTO import OrderDTO
from app.Domain.Order.OrderVO import Order_dishes,Order_ID,Order_Client_name,Mount

OrderController = APIRouter()
services:Service_Handler = Service_Handler()
repositorySQL = OrderSQLRepository()
repositorySQL_Dish = DishSQLRepository()
services.addService(Service_Type.Command_Create, Create_Order_Service(repository=repositorySQL))
services.addService(Service_Type.Query_by_Id, SearchById_Order_Service(repository=repositorySQL, dish_repository=repositorySQL_Dish))
services.addService(Service_Type.Query_all, SearchAll_Order_Service(repository=repositorySQL, dish_repository=repositorySQL_Dish))

# Controlador con los endpoints definidos para la gestion de ordenes

@OrderController.post("/Order",  tags=["Order"])
async def createOrder(dto:OrderDTO):
    servicesPO = Create_Order_Parameter(dto.client_name,dto.mount,dto.order_dishes_list)
    return await services.execute(servicesPO)

@OrderController.get("/Order/{id}",  tags=["Order"])
async def searchOrderbyId(id:str):
    servicesPO = SearchById_Order_Parameter(id)
    return await services.execute(servicesPO)

@OrderController.get("/order",  tags=["Order"])
async def searchOrderAll():
    servicesPO = SearchAll_Order_Parameter()
    return await services.execute(servicesPO)

@OrderController.delete("/Order/{id}",  tags=["Order"])
async def deleteDish(id:str):
    return await repositorySQL.deleteOrder(id)