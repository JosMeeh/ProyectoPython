from app.Domain.Dish.Dish_VO import Id_Dish
class Order_ID:
    def __init__(self, order_id:str) -> None:
        self.order_id = order_id
    @property
    def Order_id(self):
        return self.order_id
    def Order_setId(order_id: str) -> 'Order_ID':
        return Order_ID(order_id)


class Order_Client_name:
    def __init__(self, name:str) -> None:
        self.name = name
    @property
    def name(self):
        return self.name
    def order_client_name(name: str) -> 'Order_Client_name':
        return Order_Client_name(name)

class Order_dishes:
    def __init__(self, dishes_list: list[tuple[str, int]]) -> None:
        self.dishes_list = dishes_list
        @property
        def dishes_list(self):
            return self.dishes_list
        def setOrder_dishes_list(dishes_list: list[tuple[str, int]]) -> 'Order_dishes':
            return Order_dishes(dishes_list)

class Mount:
    def __init__(self, Mount:float) -> None:
        self.Mount = Mount
    @property
    def Mount(self):
        return self.Mount
    def Mount_setMount(Mount: float) -> 'Mount':
        return Mount(Mount)
