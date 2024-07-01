from app.Application.Order.Cmd.Service_Order_Create import Create_Order_Parameter, Create_Order_Service
from app.Application.shared.IService import Service_Type
from app.Application.shared.Service_Handler import Service_Handler
from app.Infraestructure.Order.OrderSQLRepository import OrderSQLRepository
from fastapi import APIRouter
from app.Infraestructure.Dtos.OrderDTO import OrderDTO
from app.Domain.Order.OrderVO import Order_dishes,Order_ID,Order_Client_name,Mount

OrderController = APIRouter()
services:Service_Handler = Service_Handler()
repositorySQL = OrderSQLRepository()
services.addService(Service_Type.Command_Create, Create_Order_Service(repository=repositorySQL))
@OrderController.post("/Order")
async def createOrder(dto:OrderDTO):
    servicesPO = Create_Order_Parameter(dto.client_name,dto.mount,dto.order_dishes_list)
    return await services.execute(servicesPO)