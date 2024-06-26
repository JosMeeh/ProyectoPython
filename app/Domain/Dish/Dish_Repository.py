from abc import ABC, abstractmethod
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe


class Dish_Repository(ABC):
    @abstractmethod
    async def searchDishbyId(self, id:Id_Dish) -> Dish:
        pass

    @abstractmethod
    async def searchAllDishes(self) -> list[Dish]:
        pass

    @abstractmethod
    async def addDish(self, dish:Dish) -> Dish:
        pass

    @abstractmethod
    async def deleteDish(self, id:Id_Dish) -> Dish:
        pass

    @abstractmethod
    async def updateDish(self, id:Id_Dish, name:Name_Dish, description:Description_Dish, price:Price_Dish) -> Dish:
        pass

    @abstractmethod
    async def updateRecipe(self, id:Id_Dish, recipe:Recipe) -> Dish:
        pass        
