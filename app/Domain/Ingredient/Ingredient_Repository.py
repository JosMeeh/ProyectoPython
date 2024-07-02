from abc import ABC, abstractmethod
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient, Name_Ingredient, Amount_Ingredient


class Ingredient_Repository(ABC):
    @abstractmethod
    async def searchIngredientbyId(self, id: Id_Ingredient) -> Ingredient:
        pass

    @abstractmethod
    async def searchAllIngredients(self) -> list[Ingredient]:
        pass

    @abstractmethod
    async def addIngredient(self, dish: Ingredient) -> Ingredient:
        pass

    @abstractmethod
    async def deleteIngredient(self, id: Id_Ingredient) -> bool:
        pass

    @abstractmethod
    async def updateIngredient(self, id: Id_Ingredient, name: Name_Ingredient, amount: Amount_Ingredient) -> Ingredient:
        pass
