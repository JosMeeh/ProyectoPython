#Agregado de Platillos
""" 
- id_Dish: Id_Dish- name_Dish:Name_Dish
- description_Dish:Description_Dish
- price_Dish: Price_Dish
- recipe: Recipe
"""
from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe


class Dish:
    def __init__(self, id:Id_Dish, name:Name_Dish, description:Description_Dish, price:Price_Dish, recipe:Recipe = None):
        self.__id_Dish          = id
        self.__name_Dish        = name
        self.__description_Dish = description
        self.__price_Dish       = price
        if recipe is not None:
            self.__recipe       = recipe

    def getId(self) -> Id_Dish:
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
    