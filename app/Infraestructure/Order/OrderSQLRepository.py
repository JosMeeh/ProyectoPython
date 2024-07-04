from __future__ import annotations

from abc import ABC, abstractmethod
from app.Domain.Order.Order import Order
from app.Domain.Order.Order_Factory import Order_Factory
from app.Domain.Order.Order_Repository import Order_Repository
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession, OrderDB,DishBD, Order_DishesBD
from app.Domain.Order.OrderVO import Order_dishes,Order_ID,Order_Client_name,Mount
from app.Domain.Dish.Dish_VO import Id_Dish
from uuid import uuid4


# Implementacion del repositorio de ordenes

class OrderSQLRepository(Order_Repository):

    def __init__(self) -> None:
        super().__init__()
        self.__database = dataBaseSession
        self.__factory = Order_Factory()

    # Consultar todos los platilos dentro de una orden
    async def searchOrderDishes(self, id:str):

        list_orders:list[Order_DishesBD] | None = self.__database.findDishesofOrder(id)
        order_dish_list:list[tuple[str,int]] = []
        if len(list_orders) != 0:
            for dish in list_orders:
                order_dish_list.append((dish.id_Dish, dish.amount))
            order_dishess:Order_dishes = order_dish_list

            return order_dishess
        return None

    # Consultar una orden por id
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

    # Consultar todas las ordenes
    async def searchAllOrder(self) -> list[Order]:
        try:

            order_db= self.__database.findAllInDatabase(OrderDB)
            order_dishes: list[Order] = []
            for orders_all in order_db:
                order: Order = self.__factory.create(orders_all.id, orders_all.client_name,orders_all.price,None)
                print("PORQUE NO IMPRIMES ESTA BASURA COÑOOOOOOOO")
                print(orders_all.id)
                order_dishess = await self.searchOrderDishes(orders_all.id)
                order.Order_dishes = order_dishess
                order_dishes.append(order)
            return order_dishes
        except Exception as e:
            return e

    # Crear una nueva orden
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

    # Borrar una nueva orden
    async def deleteOrder(self, id:str) -> bool:
        try:
            deleted_order_dishes = self.__database.deletDishofOrders(id)
            delete_order: Order = await self.searchOrderbyId(id)
            deleted = self.__database.deleteInDatabase(OrderDB, id)
            if deleted:
                return delete_order
            else:
                return None
        except Exception as e:
            return e