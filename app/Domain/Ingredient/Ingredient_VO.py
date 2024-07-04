# Value Objets del Ingrediente

"""
    <<Value Object>>
    - id del ingrediente
"""

class Id_Ingredient:
    def __init__(self, id:str) -> None:
        self.__id = id

    # Getter
    @property
    def id(self):
        return self.__id

    # Setter
    def setId(id: str) -> 'Id_Ingredient':
        return Id_Ingredient(id)


""" 
    <<Value Object>>
    - nombre del ingrediente
"""


class Name_Ingredient:
    def __init__(self, name: str) -> None:
        if (len(name) <= 100):
            self.__name = name
        else:
            self.__name = name[0:100]

    # Getter
    @property
    def name(self):
        return self.__name

    # Setter
    def setName(name: str) -> 'Name_Ingredient':
        return Name_Ingredient(name)


""" 
    <<Value Object>>
    - cantidad del ingrediente
"""


class Amount_Ingredient:
    def __init__(self, amount: int) -> None:
        if (amount >= 0):
            self.__amount = amount
        else:
            self.__amount = 0

    # Getter
    @property
    def amount(self):
        return self.__amount

    # Setter
    def setAmount(amount: int) -> 'Amount_Ingredient':
        return Amount_Ingredient(amount)
