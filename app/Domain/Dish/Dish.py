from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe

"""
    <<Agregado Platillo>>

    values_objects:
        Id, Name, Description, Price, Recipe
"""
class Dish:
    def __init__(self, id:Id_Dish, name:Name_Dish, description:Description_Dish, price:Price_Dish, recipe:Recipe = None):
        self.__id_Dish          = id
        self.__name_Dish        = name
        self.__description_Dish = description
        self.__price_Dish       = price
        self.__recipe           = None
        if recipe is not None:
            self.__recipe       = recipe

    @property
    def id(self) -> Id_Dish:
        return self.__id_Dish

    @property
    def recipe(self) -> Recipe:
        return self.__recipe

    @recipe.setter
    def recipe(self, new_Recipe:Recipe):
        self.__recipe = new_Recipe

    @property
    def price(self) -> Price_Dish:
        return self.__price_Dish

    @price.setter
    def price(self, new_Price:Price_Dish):
        self.__price_Dish = new_Price

    @property
    def description(self) -> Description_Dish:
        return self.__description_Dish
    
    @property
    def name(self) -> Name_Dish:
        return self.__name_Dish
    