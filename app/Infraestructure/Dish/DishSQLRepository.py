from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession,DishBD

class DishSQLRepository(Dish_Repository):
    def __init__(self) -> None:
        super().__init__()
        self.__database = dataBaseSession


    async def searchDishbyId(self, id:Id_Dish) -> Dish:
        pass

    async def searchAllDishes(self) -> list[Dish]:
        pass

    async def addDish(self, dish:Dish) -> Dish:
        new_dish = DishBD(
            name= dish.name.name, 
            description= dish.description.description, 
            price= dish.price.price
        )
        try:
            self.__database.addInDatabase(new_dish)
            return Dish
        except Exception as e:
            return e

    async def deleteDish(self, id:Id_Dish) -> Dish:
        pass

    async def updateDish(self, id:Id_Dish, name:Name_Dish, description:Description_Dish, price:Price_Dish) -> Dish:
        pass

    async def updateRecipe(self, id:Id_Dish, recipe:Recipe) -> Dish:
        pass    