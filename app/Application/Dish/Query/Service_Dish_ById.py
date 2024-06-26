from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Dish.Dish_Factory import Dish_Factory
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Id_Dish


class SearchById_Dish_Parameter(IService_Parameter):
    def __init__(self, id:str) -> None:
        super().__init__(Service_Type.Query_by_Id)
        self.id = id


class SearchById_Dish_Response(IService_Response):
    def __init__(self, id:str, name:str, description:str, price:float, recipe:tuple[list[tuple[str, int]],str]) -> None:
        super().__init__(Result_Type.Result)
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.recipe = recipe


""" 

"""
class SearchBy_Id_Dish_Service(IService):
    def __init__(self, repository:Dish_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__factory = Dish_Factory()

    async def execute(self, servicePO: SearchById_Dish_Parameter) -> IService_Response:
        # crear con fabrica el Id
        id_dish:Id_Dish = self.__factory.createId(servicePO.id)
        # buscar entidad en repositorio 
        saved_dish:Dish | Exception = await self.__repository.searchDishbyId(id_dish)
        #VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_dish,Exception):
            return Error_Response(saved_dish)
        #-----

        #CREAR RESPONSE
        response = SearchById_Dish_Response(
            servicePO.id,
            saved_dish.name.name,
            saved_dish.description.description,
            saved_dish.price.price,
            None
        )
        if saved_dish.recipe is not None:
            response.recipe = (saved_dish.recipe.ingredients, saved_dish.recipe.instructions)
        
        return response