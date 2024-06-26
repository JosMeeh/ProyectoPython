from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient

""" 
    <<Value Object>>
    - id del plato de comida
"""
class Id_Dish:
    def __init__(self, id:str) -> None:
        self.__id = id

    @property
    def id(self):
        return self.__id
    
    def setId(id:str)  -> 'Id_Dish':
        return Id_Dish(id)
    
""" 
    <<Value Object>>
    - nombre del plato de comida
"""
class Name_Dish:
    def __init__(self, name:str) -> None:
        if (len(name) <= 30):
            self.__name = name
        else:
            self.__name = name[0:30]

    @property
    def name(self):
        return self.__name
    
    def setName(name:str) -> 'Name_Dish':
        return Name_Dish(name)
    
""" 
    <<Value Object>>
    - descripcion del plato de comida
"""
class Description_Dish:
    def __init__(self, description:str) -> None:
        if (len(description) <= 500):
            self.__description = description
        else:
            self.description = description[0:500]

    @property
    def description(self):
        return self.__description
    
    def setName(description:str) -> 'Description_Dish':
        return Description_Dish(description)

""" 
    <<Value Object>>
    - precio del plato de comida
"""
class Price_Dish:
    def __init__(self, price:float) -> None:
        if (price < 0): price * -1
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    def setPrice(price:float) -> 'Price_Dish':
        return Price_Dish(price)
    
""" 
    <<Value Object>>
    - receta del plato de comida
        - lista de id de ingredientes + cantidad que se necesita de cada uno en gramos
        - instrucciones sobre como preparar el plato
"""
class Recipe:
    def __init__(self, ingredients:list[tuple[Id_Ingredient, int]], instructions:str) -> None:
        self.__ingredients  = ingredients
        self.__instructions = instructions

    @property
    def ingredients(self):
        return self.__ingredients
    
    @property
    def instructions(self):
        return self.__instructions
    
    def setRecipe(ingredients:list[tuple[Id_Ingredient, int]], instructions:str) -> 'Recipe':
        return Recipe(ingredients, instructions)