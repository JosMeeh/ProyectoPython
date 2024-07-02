# Agregado de Ingredient

from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient, Name_Ingredient, Amount_Ingredient


class Ingredient:
    def __init__(self, id: Id_Ingredient, name: Name_Ingredient, amount: Amount_Ingredient):
        self.__id_Ingredient = id
        self.__name_Ingredient = name
        self.__amount_Ingredient = amount

    def getId(self) -> Id_Ingredient:
        return self.__id_Ingredient

    @property
    def name_Ingredient(self) -> Name_Ingredient:
        return self.__name_Ingredient

    @name_Ingredient.setter
    def name_Ingredient(self, name: Name_Ingredient):
        self.__name_Ingredient = name

    @property
    def amount_Ingredient(self) -> Amount_Ingredient:
        return self.__amount_Ingredient

    @amount_Ingredient.setter
    def amount_Ingredient(self, amount: Amount_Ingredient):
        self.__amount_Ingredient = amount
