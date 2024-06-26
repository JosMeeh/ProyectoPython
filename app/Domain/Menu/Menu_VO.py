from app.Domain.Dish.Dish_VO import Id_Dish

""" 
    <<Value Object>>
    - id del menu
"""
class Id_Menu:
    def __init__(self, id:int) -> None:
        self.__id = id

    @property
    def id(self):
        return self.__id
    
    def setId(id:int)  -> 'Id_Menu':
        return Id_Menu(id)
    
""" 
    <<Value Object>>
    - nombre del menu
"""
class Name_Menu:
    def __init__(self, name:str) -> None:
        if (len(name) <= 30):
            self.__name = name
        else:
            self.__name = name[0:30]

    @property
    def name(self):
        return self.__name
    
    def setName(name:str) -> 'Name_Menu':
        return Name_Menu(name)
    
""" 
    <<Value Object>>
    - lista de platos del menu
"""
class Dish_List_Menu:
    def __init__(self, dish_list:list[Id_Dish]) -> None:
        self.__dish_list = dish_list

    @property
    def dish_list(self):
        return self.__dish_list
    
    def setList(arr:list[Id_Dish]) -> 'Dish_List_Menu':
        return Dish_List_Menu(arr)
    
    def addDish(self, new_dish:Id_Dish) -> 'Dish_List_Menu':
        self.dish_list.append(new_dish)
        return self