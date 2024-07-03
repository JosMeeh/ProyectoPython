from __future__ import annotations

from abc import ABC, abstractmethod
from app.Domain.Order.Order import Order
from app.Domain.Order.Order_Factory import Order_Factory
from app.Domain.Order.Order_Repository import Order_Repository
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession, OrderDB,DishBD, Order_DishesBD
from app.Domain.Order.OrderVO import Order_dishes,Order_ID,Order_Client_name,Mount
from app.Domain.Dish.Dish_VO import Id_Dish
from uuid import uuid4



class OrderSQLRepository(Order_Repository):

    def __init__(self) -> None:
        super().__init__()
        self.__database = dataBaseSession
        self.__factory = Order_Factory()

    async def searchOrderDishes(self, id:str):
        list_orders:list[Order_DishesBD] | None = self.__database.findDishesofOrder(id)
        order_dish_list:list[tuple[str,int]] = []
        if len(list_orders) != 0:
            for dish in list_orders:
                order_dish_list.append((dish.id_Dish, dish.amount))
            order_dishess:Order_dishes = order_dish_list

            return order_dishess
        return None
    async def searchOrderbyId(self, id: str) -> Order:
        try:
            db_order: OrderDB = self.__database.findInDatabase(OrderDB, id)
            if db_order is None:
                return None
            order_dishes = await self.searchOrderDishes(id)
            order = self.__factory.create(db_order.id, db_order.client_name,db_order.price,order_dishes)
            return order
        except Exception as e:
            return e

    async def searchAllOrder(self) -> list[Order]:
        pass

    async def addOrder(self, order:Order,order_dishes_list: list[tuple[str,int]]) -> Order:
        new_order = OrderDB(
            # id_Order = order.Order_ID(uuid4()),
            client_name = order.OrderClientname,
            price = order.Order_Mount
        )
        try:
            saved_order:OrderDB = self.__database.addInDatabase(new_order)
            if order_dishes_list is not None:
                for dish in order_dishes_list:
                    order_d_list:Order_DishesBD = Order_DishesBD(
                        id_Order=saved_order.id,
                        id_Dish=dish[0],
                        amount=dish[1]
                    )
                    self.__database.addInDatabase(order_d_list)
            return order
        except Exception as e:
            return e

    async def deleteOrder(self, id:Order_ID) -> bool:
        pass