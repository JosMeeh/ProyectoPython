from abc import ABC, abstractmethod
from app.Domain.Order.Order import Order
from app.Domain.Order.OrderVO import Order_dishes,Order_ID,Order_Client_name,Mount


class Order_Repository(ABC):
    @abstractmethod
    async def searchOrderbyId(self, id:Order_ID) -> Order:
        pass

    @abstractmethod
    async def searchAllOrder(self) -> list[Order]:
        pass

    @abstractmethod
    async def addOrder(self, order:Order, order_dishes_list: list[tuple[str,int]]) -> Order:
        pass

    @abstractmethod
    async def deleteOrder(self, id:Order_ID) -> bool:
        pass


