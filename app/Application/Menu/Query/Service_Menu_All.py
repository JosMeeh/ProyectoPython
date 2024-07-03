from app.Application.Menu.Query.Service_Menu_ById import SearchById_Menu_Response
from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Menu.Menu_Repository import Menu_Repository
from app.Domain.Menu.Menu_Factory import Menu_Factory
from app.Domain.Menu.Menu_VO import Id_Menu, Name_Menu, Dish_List_Menu
from app.Domain.Menu.Menu import Menu


class SearchAll_Menu_Parameter(IService_Parameter):
    def __init__(self) -> None:
        super().__init__(Service_Type.Query_all)
        self.id = id


class SearchAll_Menu_Response(IService_Response):
    def __init__(self, menus:list[SearchById_Menu_Response]) -> None:
        super().__init__(Result_Type.Result)
        self.menus = menus


""" 

"""
class SearchAll_Menu_Service(IService):
    def __init__(self, repository:Menu_Repository, food_repository:Dish_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 
        self.__factory = Menu_Factory()

    async def execute(self, servicePO: SearchAll_Menu_Parameter) -> IService_Response:
        # buscar entidad en repositorio 
        saved_menus:list[Menu] | Exception = await self.__repository.searchAllMenus()
        #VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_menus,Exception):
            return Error_Response(saved_menus)
        #-----

        #CREAR RESPONSE
        menus_response:list[SearchById_Menu_Response] = []
        for menu in saved_menus:
            response = SearchById_Menu_Response(
                menu.id.id,
                menu.name.name,
                []
            )
            dish_list:list[str] = []
            
            for d in menu.dish_List.dish_list:
                dish:Dish | Exception = await self.__foodrepository.searchDishbyId(d)
                if not isinstance(dish,Exception):
                    dish_list.append({
                        "name":dish.name.name,
                        "description":dish.description.description,
                        "price":dish.price.price
                    })
            response.dish_list = dish_list

            menus_response.append(response)

        return SearchAll_Menu_Response(menus_response)