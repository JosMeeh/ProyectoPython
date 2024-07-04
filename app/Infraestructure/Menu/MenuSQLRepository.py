from app.Infraestructure.Database.dataBaseConfig import dataBaseSession, MenuDB, Menu_DishesBD
from app.Domain.Menu.Menu import Menu
from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Menu.Menu_VO import Id_Menu, Name_Menu, Dish_List_Menu
from app.Domain.Menu.Menu_Repository import Menu_Repository
from app.Domain.Menu.Menu_Factory import Menu_Factory 

"""
    <<Repository Implementation>>

    Implementación del Menu_Repository
"""
class MenuSQLRepository(Menu_Repository):
    def __init__(self) -> None:
        super().__init__()
        self.__database = dataBaseSession
        self.__factory = Menu_Factory()

    async def searchDishes(self, id:str) -> Dish_List_Menu:
        list_dish:list[Menu_DishesBD] | None = self.__database.findDishesOfMenu(id)
        list_dish_aux:list[str] = []
        if list_dish is not None:
            for dish in list_dish:
                list_dish_aux.append(dish.id_Dish)
        dishes:Dish_List_Menu = self.__factory.createDishList(list_dish_aux)
        return dishes

    async def searchMenubyId(self, id:Id_Menu) -> Menu:
        try:
            db_menu:MenuDB = self.__database.findInDatabase(MenuDB, id.id)
            if db_menu is None:
                return None
            menu = self.__factory.create(db_menu.id, db_menu.name, [])
            dishes = await self.searchDishes(id.id)
            menu.dish_List = dishes
            return menu
        except Exception as e:
            return e

    async def searchAllMenus(self) -> list[Menu]:
        try:
            menus_db = self.__database.findAllInDatabase(MenuDB)
            menus:list[Menu] = []
            for db_menu in menus_db:
                menu:Menu = self.__factory.create(db_menu.id, db_menu.name, [])
                dish_list = await self.searchDishes(db_menu.id)
                menu.dish_List = dish_list
                menus.append(menu)
            return menus
        except Exception as e:
            print(e)
            return e


    async def addMenu(self, menu:Menu) -> Menu:
        new_menu = MenuDB(name= menu.name.name)
        try:
            
            saved_menu:MenuDB = self.__database.addInDatabase(new_menu)
            
            for dish in menu.dish_List.dish_list:
                dish_menu = Menu_DishesBD(
                    id_Dish = dish.id,
                    id_Menu = saved_menu.id
                )
                self.__database.addInDatabase(dish_menu)
            return menu
        except Exception as e:
            return e


    async def deleteMenu(self, id:Id_Menu) -> Menu:
        try:
            deleted_dishes = self.__database.deleteDishesOfMenu(id.id)
            delete_menu:Menu = await self.searchMenubyId(id)
            deleted = self.__database.deleteInDatabase(MenuDB, id.id)
            if deleted:
                return delete_menu
            else:
                return None
        except Exception as e:
            print(e)
            return e


    async def updateMenu(self, id:Id_Menu, name:Name_Menu, dish_list:Dish_List_Menu) -> Menu:
        try:
            deleted_dishes = self.__database.deleteDishesOfMenu(id.id)
            updated = self.__database.updateInDatabase(MenuDB, id.id, {'name':name.name})
            if updated:
                for dish in dish_list.dish_list:
                    await self.addDish(id, dish)
                update_menu:Menu = await self.searchMenubyId(id)
                return update_menu
            else:
                return None
        except Exception as e:
            print(e)
            return e  


    async def addDish(self, id_menu:Id_Menu, id_dish:Id_Dish) -> Id_Dish:
        try:
            dish_menu = Menu_DishesBD(
                    id_Dish = id_dish.id,
                    id_Menu = id_menu.id
                )
            self.__database.addInDatabase(dish_menu)
            return id_dish
        except Exception as e:
            return e  