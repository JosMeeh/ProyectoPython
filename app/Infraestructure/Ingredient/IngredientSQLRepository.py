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

# Consultar un ingrediente por ID
    async def searchIngredientbyId(self, id: Id_Ingredient) -> Ingredient:
        try:
            db_ingredient: IngredientBD = self.__database.findInDatabase(IngredientBD, id.id)
            if db_ingredient is None:
                return None
            ingredient = self.__factory.create(db_ingredient.id, db_ingredient.name, db_ingredient.amount)

            return ingredient
        except Exception as e:
            return e

# Listar todos los ingredientes
    async def searchAllIngredients(self) -> list[Ingredient]:
        try:
            ingredients_db = self.__database.findAllInDatabase(IngredientBD)
            ingredients: list[Ingredient] = []
            for db_ingredient in ingredients_db:
                ingredient: Ingredient = self.__factory.create(db_ingredient.id, db_ingredient.name, db_ingredient.amount)

                ingredients.append(ingredient)
            return ingredients
        except Exception as e:
            return e

# Agregar un nuevo ingrediente
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

#Eliminar un ingrediente
    async def deleteIngredient(self, id: Id_Ingredient) -> bool:
        try:
            deleted_ingredients = self.__database.deleteIngredientsOfDish(id.id)
            delete_ingredient: Ingredient = await self.searchIngredientbyId(id)
            deleted = self.__database.deleteInDatabase(IngredientBD, id.id)
            if deleted:
                return True
            else:
                return False
        except Exception as e:
            return e

    # Modificar un ingrediente
    async def updateIngredient(self, id: Id_Ingredient, name: Name_Ingredient, amount: Amount_Ingredient) -> Ingredient:
        try:
            updated = self.__database.updateInDatabase(IngredientBD, id.id,
                                                            {'name': name.name,
                                                             'amount': amount.amount})
            if updated:
                update_ingredient:Ingredient = await self.searchIngredientbyId(id)
                return update_ingredient
            else:
                return None
        except Exception as e:
            print(e)
            return e
