from app.Domain.Order.OrderVO import Order_dishes,Order_ID,Order_Client_name,Mount
##Agregado de pedidos

class Order:

    def __init__(self, OrderID:Order_ID, OrderDishes:Order_dishes, OrderClient_name:Order_Client_name, OrderMount:Mount):
        self.OrderID          = OrderID
        self.OrderDishes      = OrderDishes
        self.OrderClient_name = OrderClient_name
        self.OrderMount       = OrderMount

    def Order_ID(self) -> Order_ID:
        return self.OrderID

    @property
    def Order_dishes(self) -> Order_dishes:
        return self.OrderDishes

    @Order_dishes.setter
    def Order_dishes(self, new_order_dishes: Order_dishes):
        self.OrderDishes = new_order_dishes
    @property
    def Order_Mount(self) -> Mount:
        return self.OrderMount

    @Order_Mount.setter
    def Order_Mount(self, new_Mount: Mount):
        self.OrderMount = new_Mount

    @property
    def OrderClientname(self) -> Order_Client_name:
        return self.OrderClient_name
