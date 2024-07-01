from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient, Name_Ingredient, Amount_Ingredient
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession, IngredientBD
from app.Domain.Ingredient.Ingredient_Factory import Ingredient_Factory


class IngredientSQLRepository(Ingredient_Repository):
    def __init__(self) -> None:
        super().__init__()
        self.__database = dataBaseSession
        self.__factory = Ingredient_Factory()

    async def searchIngredientbyId(self, id: Id_Ingredient) -> Ingredient:
        try:
            db_ingredient = self.__database.findInDatabase(IngredientBD, id.id)
            print(db_ingredient.__dict__, db_ingredient.name)
            return self.__factory.create(db_ingredient.id, db_ingredient.name, db_ingredient.amount)
        except Exception as e:
            return e

    async def searchAllIngredients(self) -> list[Ingredient]:
        try:
            self.__database.findAllInDatabase(IngredientBD, id)
            return self.__
        except Exception as e:
            return e

    async def addIngredient(self, ingredient: Ingredient) -> Ingredient:
        new_ingredient = IngredientBD(
            name=ingredient.name_Ingredient.name,
            amount=ingredient.amount_Ingredient.amount
        )
        try:
            self.__database.addInDatabase(new_ingredient)
            return ingredient
        except Exception as e:
            return e

    async def deleteIngredient(self, id: Id_Ingredient) -> bool:
        pass

    async def updateIngredient(self, id: Id_Ingredient, name: Name_Ingredient, amount: Amount_Ingredient) -> Ingredient:
        pass
