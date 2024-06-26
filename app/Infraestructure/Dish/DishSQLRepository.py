from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe
from app.Infraestructure.Database.dataBaseConfig import dataBaseSession,DishBD
from app.Domain.Dish.Dish_Factory import Dish_Factory

class DishSQLRepository(Dish_Repository):
    def __init__(self) -> None:
        super().__init__()
        self.__database = dataBaseSession
        self.__factory = Dish_Factory()


    async def searchDishbyId(self, id:Id_Dish) -> Dish:
        try:
            db_dish= self.__database.findUserInDatabase(DishBD, id.id)
            print(db_dish.__dict__)
            #return self.__factory.create(db_dish.id)
        except Exception as e:
            return e

    async def searchAllDishes(self) -> list[Dish]:
        try:
            self.__database.findAllInDatabase(DishBD, id)
            return self.__
        except Exception as e:
            return e

    async def addDish(self, dish:Dish) -> Dish:
        new_dish = DishBD(
            name= dish.name.name, 
            description= dish.description.description, 
            price= dish.price.price
        )
        try:
            self.__database.addInDatabase(new_dish)
            return dish
        except Exception as e:
            return e

    async def deleteDish(self, id:Id_Dish) -> Dish:
        pass

    async def updateDish(self, id:Id_Dish, name:Name_Dish, description:Description_Dish, price:Price_Dish) -> Dish:
        pass

    async def updateRecipe(self, id:Id_Dish, recipe:Recipe) -> Dish:
        pass    