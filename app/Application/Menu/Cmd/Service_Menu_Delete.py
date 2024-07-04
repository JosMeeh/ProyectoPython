from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Menu.Menu_Repository import Menu_Repository
from app.Domain.Menu.Menu_Factory import Menu_Factory
from app.Domain.Menu.Menu_VO import Id_Menu, Name_Menu, Dish_List_Menu
from app.Domain.Menu.Menu import Menu


class Delete_Menu_Parameter(IService_Parameter):
    def __init__(self, id:str) -> None:
        super().__init__(Service_Type.Command_Delete)
        self.id = id


class Delete_Dish_Response(IService_Response):
    def __init__(self, id:str, name:str, dish_list:list) -> None:
        super().__init__(Result_Type.Result)
        self.id = id
        self.name = name
        self.dish_list = dish_list


class Delete_Menu_Service():
    def __init__(self, repository:Menu_Repository, food_repository:Dish_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 
        self.__factory = Menu_Factory()

    async def execute(self, servicePO: Delete_Menu_Parameter) -> IService_Response:
        id_menu:Id_Menu = self.__factory.createId(servicePO.id)
        search_menu:Menu | None | Exception = await self.__repository.searchMenubyId(id_menu)
        #VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(search_menu,Exception):
            return Error_Response(search_menu)
        if search_menu is None:
            return NotFound_Response()
        #-----        
        
        #CREAR RESPONSE
        response = Delete_Dish_Response(
            servicePO.id,
            search_menu.name.name,
            []
        )
        
        #Buscar Ingredientes
        dish_list:list[str] = []
        for d in search_menu.dish_List.dish_list:
            dish:Dish | Exception = await self.__foodrepository.searchDishbyId(d)
            if not isinstance(dish,Exception):
                dish_list.append({
                    "name":dish.name.name,
                    "description":dish.description.description,
                    "price":dish.price.price
                })
        response.dish_list = dish_list

        deleted_menu:Dish | Exception = await self.__repository.deleteMenu(id_menu)
        #VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(deleted_menu,Exception):
            return Error_Response(deleted_menu)
        #-----    

        return response
