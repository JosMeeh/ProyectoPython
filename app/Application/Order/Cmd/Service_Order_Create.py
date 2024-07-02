from __future__ import annotations
from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Order.Order_Factory import Order_Factory
from app.Domain.Order.Order import Order
from app.Domain.Order.Order_Repository import Order_Repository


class Create_Order_Parameter(IService_Parameter):
    def __init__(self, client_name:str, mount:float, order_dishes:list[tuple[str, int]]) -> None:
        super().__init__(Service_Type.Command_Create)
        self.client_name = client_name
        self.mount = mount
        self.order_dishes = order_dishes

class Create_Dish_Response(IService_Response):
    def __init__(self, client_name:str, mount:float, order_dishes:list[tuple[str, int]]) -> None:
        super().__init__(Result_Type.Result)
        self.client_name = client_name
        self.mount = mount
        self.order_dishes = order_dishes


class Create_Order_Service(IService):
    def __init__(self, repository: Order_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__factory = Order_Factory()

    async def execute(self, servicePO: Create_Order_Parameter) -> IService_Response:
        # crear con fabrica el Agregado Dish
        new_order: Order = self.__factory.create(
            "--",
            servicePO.client_name,
            servicePO.mount,
            servicePO.order_dishes,
        )
        # guardar entidad en repositorio
        saved_order: Order | Exception = await self.__repository.addOrder(new_order,new_order.Order_dishes)
        # VALIDAR QUE SE HA GUARDADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_order, Exception):
            return Error_Response(saved_order)
        # -----

        # CREAR RESPONSE
        response = Create_Dish_Response(
            servicePO.client_name,
            servicePO.order_dishes,
            servicePO.mount,
        )
        return response