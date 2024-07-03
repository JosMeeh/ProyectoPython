from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Menu.Menu_Repository import Menu_Repository
from app.Domain.Menu.Menu_Factory import Menu_Factory
from app.Domain.Menu.Menu_VO import Id_Menu, Name_Menu, Dish_List_Menu
from app.Domain.Menu.Menu import Menu


class Update_Menu_Parameter(IService_Parameter):
    def __init__(self, id:str, name:str, dish_list:list) -> None:
        super().__init__(Service_Type.Command_Update)
        self.id = id
        self.name = name
        self.dish_list = dish_list


class Update_Menu_Response(IService_Response):
    def __init__(self, id:str, name:str, dish_list:list) -> None:
        super().__init__(Result_Type.Result)
        self.id = id
        self.name = name
        self.dish_list = dish_list

""" 

"""
class Update_Menu_Service(IService):
    def __init__(self, repository:Menu_Repository, food_repository:Dish_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 
        self.__factory = Menu_Factory()

    async def execute(self, servicePO: Update_Menu_Parameter) -> IService_Response:
        new_menu = self.__factory.create(
            servicePO.id,
            servicePO.name,
            servicePO.dish_list
        )

        updated_dish:Menu | None | Exception = await self.__repository.updateMenu(
            new_menu.id,
            new_menu.name,
            new_menu.dish_List
        )
        if isinstance(updated_dish,Exception):
            return Error_Response(updated_dish)
        if updated_dish is None:
            return NotFound_Response()
        
        #CREAR RESPONSE
        #CREAR RESPONSE
        response = Update_Menu_Response(
            servicePO.id,
            updated_dish.name.name,
            []
        )
        
        #Buscar Ingredientes
        dish_list:list[str] = []
        for d in updated_dish.dish_List.dish_list:
            dish:Dish | Exception = await self.__foodrepository.searchDishbyId(d)
            if not isinstance(dish,Exception):
                dish_list.append({
                    "name":dish.name.name,
                    "description":dish.description.description,
                    "price":dish.price.price
                })
        response.dish_list = dish_list

        return response
