from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Menu.Menu import Menu
from app.Domain.Dish.Dish import Dish
from app.Domain.Menu.Menu_Factory import Menu_Factory
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Menu.Menu_Repository import Menu_Repository

"""
    IService_Parameter
    type = Command_Create

    Parameter Object para Servicio de Create de Menu.
    Recibe todos los valores primitivos de un menu excepto su id que es generada en el servicio
"""
class Create_Menu_Parameter(IService_Parameter):
    def __init__(self, name:str, dish_list:list[str]) -> None:
        super().__init__(Service_Type.Command_Create)
        self.name = name
        self.dish_list = dish_list

"""
    IService_Response
    type = Result

    Respuesta para resultado exitoso de crear un Menu
    Emite todos los valores primitivos de un platillo excepto su id
"""
class Create_Menu_Response(IService_Response):
    def __init__(self, name:str, dish_list:list) -> None:
        super().__init__(Result_Type.Result)
        self.name = name
        self.dish_list = dish_list


""" 
    IService
    type = Command_Create

    Servicio para crear un Menu
"""
class Create_Menu_Service(IService):
    def __init__(self, repository:Menu_Repository, food_repository:Dish_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 
        self.__factory = Menu_Factory()

    async def execute(self, servicePO: Create_Menu_Parameter) -> IService_Response:
        """ 
            Crear un menu en base de datos con los datos pasados por parametro
            En caso de alguna excepcion en base de datos retorna un "Error_Response"
        """
        # crear con fabrica el Agregado Menu
        new_menu:Menu = self.__factory.create(
            "--",
            servicePO.name,
            servicePO.dish_list
        )
        # guardar entidad en repositorio 
        saved_menu:Menu | Exception = await self.__repository.addMenu(new_menu)
        #Validar Respuesta
        if isinstance(saved_menu,Exception):
            return Error_Response(saved_menu)
        #-----

        #CREAR RESPONSE
        response = Create_Menu_Response(
            servicePO.name,
            servicePO.dish_list
        )
        
        #Buscar los datos de los platillos de un menu
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