from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Menu.Menu import Menu
from app.Domain.Menu.Menu_VO import Id_Menu, Name_Menu, Dish_List_Menu

class Menu_Factory:
    def __init__(self) -> None:
        pass

    def create(self, idPO:str, name:str, dish_list:list[str]) -> Menu:
        idVO = Id_Dish(idPO)
        nameVO = Name_Menu(name)
        dish_listVO:list[Id_Dish] = []
        
        for id_dish in dish_list:
            dish_listVO.append(Id_Dish(id_dish))
        dish_listVO = Dish_List_Menu(dish_listVO) 

        return Menu(idVO, nameVO, dish_listVO)
    

    def createId(self,idPO:str)->Id_Menu:
        return Id_Menu(idPO)
    

    def createDishList(self, dish_list:list[str])->Dish_List_Menu:
        dish_listVO:list[Id_Dish] = []
        
        for id_dish in dish_list:
            dish_listVO.append(Id_Dish(id_dish))
        return Dish_List_Menu(dish_listVO) 