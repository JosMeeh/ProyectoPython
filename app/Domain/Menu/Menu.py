from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Menu.Menu_VO import Dish_List_Menu, Id_Menu, Name_Menu


class Menu:
    def __init__(self, id:Id_Menu, name:Name_Menu , dish_List:Dish_List_Menu = None):
        self.__id_Menu          = id
        self.__name_Menu        = name
        if dish_List is not None:
            self.__dish_List       = dish_List

    def getId(self) -> Id_Menu:
        return self.__id_Menu

    @property
    def dish_List(self) -> Dish_List_Menu:
        return self.__dish_List

    @dish_List.setter
    def dish_List(self, new_list:Dish_List_Menu):
        self.__dish_List = new_list

    def addDish(self, new_dish:Id_Dish) -> None:
        self.__dish_List = self.__dish_List.addDish(new_dish)