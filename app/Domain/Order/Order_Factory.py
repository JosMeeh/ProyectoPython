from app.Domain.Order.Order import Order
from app.Domain.Order.OrderVO import Order_dishes,Order_ID,Order_Client_name,Mount
from app.Domain.Dish.Dish_VO import Id_Dish
from uuid import uuid4

class Order_Factory:
    def __init__(self) -> None:
        pass

    def create(self, idPO: str, name_client: str,Mount_order: float,
               Order_dishes_list: list[tuple[str, int]]) -> Order:
        idVO = Order_ID(idPO)
        nameVO = name_client
        MountVO = Mount_order
        Order_disherVO = Order_dishes_list
        return Order(idVO,Order_disherVO,nameVO,MountVO)



