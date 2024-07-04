from __future__ import annotations
from app.Domain.Menu.Menu import Menu
from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Menu.Menu_Factory import Menu_Factory
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Menu.Menu_Repository import Menu_Repository
from app.Domain.Dish.Dish import Dish


class Create_Menu_Parameter(IService_Parameter):
    def __init__(self, name:str, dish_list:list[str]) -> None:
        super().__init__(Service_Type.Command_Create)
        self.name = name
        self.dish_list = dish_list


class Create_Menu_Response(IService_Response):
    def __init__(self, name:str, dish_list:list) -> None:
        super().__init__(Result_Type.Result)
        self.name = name
        self.dish_list = dish_list


""" 

"""
class Create_Menu_Service(IService):
    def __init__(self, repository:Menu_Repository, food_repository:Dish_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 
        self.__factory = Menu_Factory()

    async def execute(self, servicePO: Create_Menu_Parameter) -> IService_Response:
        # crear con fabrica el Agregado Dish
        new_menu:Menu = self.__factory.create(
            "--",
            servicePO.name,
            servicePO.dish_list
        )
        # guardar entidad en repositorio 
        saved_menu:Menu | Exception = await self.__repository.addMenu(new_menu)
        #VALIDAR QUE SE HA GUARDADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_menu,Exception):
            return Error_Response(saved_menu)
        #-----

        #CREAR RESPONSE
        response = Create_Menu_Response(
            servicePO.name,
            servicePO.dish_list
        )
        dish_list:list[str] = []
        for d in saved_menu.dish_List.dish_list:
            dish:Dish | Exception = await self.__foodrepository.searchDishbyId(d)
            if not isinstance(dish,Exception):
                dish_list.append({
                    "name":dish.name.name,
                    "description":dish.description.description,
                    "price":dish.price.price
                })
        response.dish_list = dish_list
        return response