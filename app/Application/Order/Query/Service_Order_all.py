from __future__ import annotations
from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Dish.Dish_Factory import Dish_Factory
from app.Domain.Order.Order import Order
from app.Domain.Order.Order_Factory import Order_Factory
from app.Domain.Order.Order_Repository import Order_Repository
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish import Dish
from app.Domain.Order.OrderVO import Order_dishes
from app.Domain.Order.OrderVO import Order_ID
from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient
from app.Application.Order.Query.Service_Order_Byid import SearchById_Order_Response

# Servicio para listar todos las ordenes del sistema

# Define los parametros que va a recibir el servicio

class SearchAll_Order_Parameter(IService_Parameter):
    def __init__(self) -> None:
        super().__init__(Service_Type.Query_all)
        self.id = id

# Define la respuesta del servicio
class SearchAll_Order_Response(IService_Response):
    def __init__(self, orders: list[SearchById_Order_Response]) -> None:
        super().__init__(Result_Type.Result)
        self.orders = orders


""" 

"""


class SearchAll_Order_Service(IService):
    def __init__(self, repository: Order_Repository, dish_repository: Dish_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__dish_repository = dish_repository
        self.__factory = Order_Factory()

    async def execute(self, servicePO: SearchAll_Order_Parameter) -> IService_Response:

        # buscar entidad en repositorio
        saved_orders: list[Order] | Exception = await self.__repository.searchAllOrder()
        return saved_orders
        # VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_orders, Exception):
            return Error_Response(saved_orders)
        # -----

        # CREAR RESPONSE
        orders_response: list[SearchById_Order_Response] = []
        for order in saved_orders:
            response = SearchById_Order_Response(
                order.Order_ID().Order_id,
                order.OrderClientname,
                order.Order_Mount,
                None
            )

        dishes_response.append(response)
        return orders_response