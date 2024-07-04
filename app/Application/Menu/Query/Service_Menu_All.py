from app.Application.Menu.Query.Service_Menu_ById import SearchById_Menu_Response
from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Menu.Menu import Menu
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Menu.Menu_Repository import Menu_Repository

"""
    IService_Parameter
    type = Query_all

    Parameter Object para Servicio de mostrar todos los Menus.
"""
class SearchAll_Menu_Parameter(IService_Parameter):
    def __init__(self) -> None:
        super().__init__(Service_Type.Query_all)
        self.id = id

"""
    IService_Response
    type = Result

    Respuesta para resultado exitoso de mostrar todos los Menus
    Emite una lista con todos los menus y todos los valores primitivos
"""
class SearchAll_Menu_Response(IService_Response):
    def __init__(self, menus:list[SearchById_Menu_Response]) -> None:
        super().__init__(Result_Type.Result)
        self.menus = menus


""" 
    IService
    type = Query_all

    Servicio para mostrar todos los Menus
"""
class SearchAll_Menu_Service(IService):
    def __init__(self, repository:Menu_Repository, food_repository:Dish_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 

    async def execute(self, servicePO: SearchAll_Menu_Parameter) -> IService_Response:
        """ 
            Busca todos los menus guardados en la base de datos y los agrupa en una lista
            En caso de alguna excepcion en base de datos retorna un "Error_Response"
        """
        # buscar entidad en repositorio 
        saved_menus:list[Menu] | Exception = await self.__repository.searchAllMenus()
        #Validar Respuesta
        if isinstance(saved_menus,Exception):
            return Error_Response(saved_menus)
        #-----

        #CREAR RESPONSE
        menus_response:list[SearchById_Menu_Response] = []
        for menu in saved_menus:
            #Crear response individual
            response = SearchById_Menu_Response(
                menu.id.id,
                menu.name.name,
                []
            )

            #Buscar los datos de los platillos de un menu
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