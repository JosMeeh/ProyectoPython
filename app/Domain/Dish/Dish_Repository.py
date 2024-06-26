from abc import ABC, abstractmethod
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe


class Dish_Repository(ABC):
    @abstractmethod
    def searchDishbyId(id:Id_Dish) -> Dish:
        pass

    @abstractmethod
    def searchAllDishes() -> list[Dish]:
        pass

    @abstractmethod
    def addDish(dish:Dish) -> Dish:
        pass

    @abstractmethod
    def deleteDish(id:Id_Dish) -> Dish:
        pass

    @abstractmethod
    def updateDish(id:Id_Dish, name:Name_Dish, description:Description_Dish, price:Price_Dish) -> Dish:
        pass

    @abstractmethod
    def updateRecipe(id:Id_Dish, recipe:Recipe) -> Dish:
        pass        
