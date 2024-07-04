from __future__ import annotations

from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe
from app.Infraestructure.Database.dataBaseConfig import Recipe_IngredientBD, dataBaseSession,DishBD
from app.Domain.Dish.Dish_Factory import Dish_Factory
from app.Domain.Ingredient.Ingredient_Factory import Ingredient_Factory 

class DishSQLRepository(Dish_Repository):
    def __init__(self) -> None:
        super().__init__()
        self.__database = dataBaseSession
        self.__factory = Dish_Factory()

    async def searchIngredients(self, id:str, instructions:str)->Recipe:
        list_ingredients:list[Recipe_IngredientBD] | None = self.__database.findIngredientsOfDish(id)
        dish_list_ingredients:list[tuple[str,int]] = []
        if len(list_ingredients) != 0:
            for ingredient in list_ingredients:
                dish_list_ingredients.append((ingredient.id_Ingredient, ingredient.amount))
            recipe:Recipe = self.__factory.createRecipe(dish_list_ingredients, instructions)
            return recipe
        return None


    async def searchDishbyId(self, id:Id_Dish) -> Dish:
        try:
            db_dish:DishBD = self.__database.findInDatabase(DishBD, id.id)
            if db_dish is None:
                return None
            dish = self.__factory.create(db_dish.id, db_dish.name, db_dish.description, db_dish.price, None)
            recipe = await self.searchIngredients(id.id, db_dish.instructions)
            if recipe is not None:
                dish.recipe = recipe
            return dish
        except Exception as e:
            return e


    async def searchAllDishes(self) -> list[Dish]:
        try:
            dishes_db = self.__database.findAllInDatabase(DishBD)
            dishes:list[Dish] = []
            for db_dish in dishes_db:
                dish:Dish = self.__factory.create(db_dish.id, db_dish.name, db_dish.description, db_dish.price, None)
                recipe = await self.searchIngredients(db_dish.id, db_dish.instructions)
                if recipe is not None:
                    dish.recipe = recipe
                dishes.append(dish)
            return dishes
        except Exception as e:
            return e


    async def addDish(self, dish:Dish) -> Dish:
        new_dish = DishBD(
            name            = dish.name.name, 
            description     = dish.description.description, 
            price           = dish.price.price,
            instructions    = "None"
        )
        if dish.recipe is not None:
            new_dish.instructions    = dish.recipe.instructions
        try:
            saved_dish:DishBD = self.__database.addInDatabase(new_dish)
            if dish.recipe is not None:
                for ingredient in dish.recipe.ingredients:
                    recipe_ingredient = Recipe_IngredientBD(
                        id_Dish = saved_dish.id,
                        id_Ingredient = ingredient[0].id,
                        amount = ingredient[1]
                    )
                    self.__database.addInDatabase(recipe_ingredient)
            return dish
        except Exception as e:
            return e


    async def deleteDish(self, id:Id_Dish) -> Dish:
        try:
            deleted_ingredients = self.__database.deleteIngredientsOfDish(id.id)
            delete_dish:Dish = await self.searchDishbyId(id)
            deleted = self.__database.deleteInDatabase(DishBD, id.id)
            if deleted:
                return delete_dish
            else:
                return None
        except Exception as e:
            return e


    async def updateDish(self, id:Id_Dish, name:Name_Dish, description:Description_Dish, price:Price_Dish, recipe:Recipe) -> Dish:
        try:
            updated = self.__database.updateInDatabase(DishBD, id.id, 
                                                            {'name':name.name,
                                                             'description':description.description,
                                                             'price':price.price})
            if updated:
                update_recipe = await self.updateRecipe(id, recipe)
                update_dish:Dish = await self.searchDishbyId(id)
                return update_dish
            else:
                return None
        except Exception as e:
            print(e)
            return e  


    async def updateRecipe(self, id:Id_Dish, recipe:Recipe) -> Recipe:
        try:
            deleted_ingredients = self.__database.deleteIngredientsOfDish(id.id)
            updated_dish = self.__database.updateInDatabase(DishBD, id.id, {'instructions':recipe.instructions})
            for ingredient in recipe.ingredients:
                recipe_ingredient = Recipe_IngredientBD(
                    id_Dish = id.id,
                    id_Ingredient = ingredient[0].id,
                    amount = ingredient[1]
                )
                self.__database.addInDatabase(recipe_ingredient)
            if updated_dish:
                return recipe
            else:
                return None
        except Exception as e:
            return e  