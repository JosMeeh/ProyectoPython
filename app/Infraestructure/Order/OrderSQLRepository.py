from abc import ABC, abstractmethod
from app.Domain.Order.Order import Order
from app.Domain.Order.Order_Factory import Order_Factory
from app.Domain.Order.Order_Repository import Order_Repository
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession, OrderDB,DishBD
from app.Domain.Order.OrderVO import Order_dishes,Order_ID,Order_Client_name,Mount
from app.Domain.Dish.Dish_VO import Id_Dish
from uuid import uuid4



class OrderSQLRepository(Order_Repository):

    def __init__(self) -> None:
        super().__init__()
        self.__database = dataBaseSession
        self.__factory = Order_Factory()

    async def searchOrderbyId(self, id:Order_ID) -> Order:
        Order_object:Order = self.__database.findInDatabase(OrderDB,id)
        return Order_object

    async def searchAllOrder(self) -> list[Order]:
        pass

    async def addOrder(self, order:Order,order_dishes_list: list[tuple[str,int]]) -> Order:
        new_order = OrderDB(
            # id_Order = order.Order_ID(uuid4()),
            client_name = order.OrderClientname,
            price = order.Order_Mount
        )
        try:
            self.__database.addInDatabase(new_order)
            # for dish in order_dishes_list:
            #     id_dish_verification:DishBD = self.__database.findInDatabase(DishBD,dish[0])
            #     if(id_dish_verification):
            #         new_order_dishes = Order_DishesDB(
            #             id_order=new_order.id,
            #             id_dish=dish[0],
            #             amount=dish[1]
            #         )
            #         self.__database.addInDatabase(new_order_dishes)
            #     else: print(f'{dish[0]} Not Found')
        except Exception as e:
            return order
            return e

    async def deleteOrder(self, id:Order_ID) -> bool:
        pass