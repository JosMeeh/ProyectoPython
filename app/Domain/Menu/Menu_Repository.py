from abc import ABC, abstractmethod
from app.Domain.Menu.Menu import Menu
from app.Domain.Menu.Menu_VO import Id_Menu, Name_Menu, Dish_List_Menu
from app.Domain.Dish.Dish_VO import Id_Dish

class Menu_Repository(ABC):
    @abstractmethod
    async def searchMenubyId(self, id:Id_Menu) -> Menu:
        pass

    @abstractmethod
    async def searchAllMenus(self) -> list[Menu]:
        pass

    @abstractmethod
    async def addMenu(self, menu:Menu) -> Menu:
        pass

    @abstractmethod
    async def deleteMenu(self, id:Id_Menu) -> Menu:
        pass

    @abstractmethod
    async def updateMenu(self, id:Id_Menu, name:Name_Menu, dish_list:Dish_List_Menu) -> Menu:
        pass

    @abstractmethod
    async def addDish(self, id_menu:Id_Menu, id_dish:Id_Dish) -> Id_Dish:
        pass        
